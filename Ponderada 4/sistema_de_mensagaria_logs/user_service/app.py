from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import requests
import datetime
import os

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

users_db = []

LOG_SERVICE_URL = os.getenv("LOG_SERVICE_URL", "http://log_service:8000/log")

def send_log(user_id: str, action: str, result: str, cause: Optional[str] = None):
    log_entry = {
        "service": "user_service",
        "user_id": user_id,
        "action": action,
        "result": result,
        "cause": cause,
        "timestamp": datetime.datetime.now().isoformat()
    }
    response = requests.post(LOG_SERVICE_URL, json=log_entry)
    if response.status_code != 200:
        print(f"Failed to send log: {response.content}")

@app.post("/users/", response_model=User)
def create_user(user: User):
    if any(u.id == user.id for u in users_db):
        send_log(str(user.id), "create_user", "failure", "User with this ID already exists")
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(user)
    send_log(str(user.id), "create_user", "success")
    return user

@app.get("/users/", response_model=List[User])
def get_users():
    send_log("N/A", "get_users", "success")
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if user is None:
        send_log(str(user_id), "get_user", "failure", "User not found")
        raise HTTPException(status_code=404, detail="User not found")
    send_log(str(user_id), "get_user", "success")
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    user_index = next((index for index, u in enumerate(users_db) if u.id == user_id), None)
    if user_index is None:
        send_log(str(user_id), "update_user", "failure", "User not found")
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_index] = updated_user
    send_log(str(user_id), "update_user", "success")
    return updated_user

@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    user_index = next((index for index, u in enumerate(users_db) if u.id == user_id), None)
    if user_index is None:
        send_log(str(user_id), "delete_user", "failure", "User not found")
        raise HTTPException(status_code=404, detail="User not found")
    removed_user = users_db.pop(user_index)
    send_log(str(user_id), "delete_user", "success")
    return removed_user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
