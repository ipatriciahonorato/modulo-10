from fastapi import FastAPI, Request, Depends, HTTPException, status, Response, Form, Cookie
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from database import models, schemas
from database.database import SessionLocal, engine 
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurações
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///fallback.db")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-secret-key")
templates = Jinja2Templates(directory="templates")

# Dependências
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Request, HTTPException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
from starlette.requests import Request

async def get_current_user(request: Request, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = getattr(request.state, 'auth_token', None)
    if not token:
        raise credentials_exception

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        user = db.query(models.User).filter(models.User.email == user_id).first()
        if not user:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user

# Rotas
@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<p>Hello, World!</p>"

@app.get("/users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for var, value in user.dict().items():
        setattr(db_user, var, value) if value else None
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/user-login", response_class=HTMLResponse)
def user_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/user-register", response_class=HTMLResponse)
def user_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/error", response_class=HTMLResponse)
def error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/content", response_class=HTMLResponse)
def content(request: Request, user: schemas.User = Depends(get_current_user)):
    return templates.TemplateResponse("content.html", {"request": request, "user": user})

import logging

logger = logging.getLogger(__name__)

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class AuthTokenExtractorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.cookies.get('access_token')
        if token:
            # Armazena apenas o token sem o prefixo "Bearer "
            token = token.split(" ")[1]
            request.state.auth_token = token
        response = await call_next(request)
        return response

app.add_middleware(AuthTokenExtractorMiddleware)


@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == username, models.User.password == password).first()
    if not user:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Invalid username or password"})
    access_token = create_access_token(data={"sub": user.email})
    response = RedirectResponse(url="/content", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True, path="/")
    return response


@app.post("/register", response_class=HTMLResponse)
def register(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == username).first()
    if existing_user:
        return templates.TemplateResponse("error.html", {"request": Request, "message": "Username already exists"})
    new_user = models.User(name=username, email=username, password=password)
    db.add(new_user)
    db.commit()
    return RedirectResponse(url="/user-login", status_code=status.HTTP_302_FOUND)

@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    db_task = models.Task(**task.dict(), user_id=user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/view", response_class=HTMLResponse)
def view_tasks(request: Request, db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    tasks = db.query(models.Task).filter(models.Task.user_id == user.id).all()
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db), user: schemas.User = Depends
(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for var, value in task.dict().items():
        setattr(db_task, var, value) if value else None
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user.id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Funções adicionais
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.email == username, models.User.password == password).first()
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm="HS256")
    return encoded_jwt