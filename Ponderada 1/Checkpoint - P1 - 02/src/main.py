from flask import Flask
from database.database import db
from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
from flask_jwt_extended import JWTManager, set_access_cookies
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import User, Task
import requests as http_request
import os

app = Flask(__name__, template_folder="templates")
# Configuração da URI do banco de dados usando variável de ambiente
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///fallback.db")
# initialize the app with the extension
db.init_app(app)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default-secret-key")
# Seta o local onde o token será armazenado
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

# Verifica se o parâmetro create_db foi passado na linha de comando
import sys
def create_database():
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
        create_database()
    else:
        app.run()
        
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Adicionando as rotas CRUD para a entidade User
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return_users = []
    for user in users:
        return_users.append(user.serialize())
    return jsonify(return_users)

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return jsonify(user.serialize())

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = User(name=data["name"], email=data["email"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    user = User.query.get(id)
    user.name = data["name"]
    user.email = data["email"]
    user.password = data["password"]
    db.session.commit()
    return jsonify(user.serialize())

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize())

@app.route("/user-login", methods=["GET"])
def user_login():
    return render_template("login.html")

@app.route("/user-register", methods=["GET"])
def user_register():
    return render_template("register.html")

@app.route("/error", methods=["GET"])
def error():
    return render_template("error.html")

@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    user = User.query.filter_by(email=username, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })

@app.route("/content", methods=["GET"])
@jwt_required()
def content():
    return render_template("content.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)

    # Check if username and password are provided
    if not username or not password:
        return render_template("error.html", message="Both username and password are required.")

    # Make a call to create the token
    try:
        token_response = http_request.post(
            "http://localhost:5000/token", 
            json={"username": username, "password": password}
        )
    except Exception as e:
        # Log the exception or handle it appropriately
        return render_template("error.html", message="Failed to connect to the token service.")

    # Check if the token was successfully created
    if token_response.status_code != 200:
        return render_template("error.html", message="Invalid username or password.")

    # Extract the token and redirect to the task viewing page
    token = token_response.json().get('token')
    if not token:
        return render_template("error.html", message="Failed to retrieve token.")

    # Set the access cookies and redirect to the task listing
    response = make_response(redirect(url_for('view_tasks')))
    set_access_cookies(response, token)
    return response

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username or not password:
        return render_template("error.html", message="Missing username or password"), 400

    existing_user = User.query.filter_by(email=username).first()
    if existing_user:
        return render_template("error.html", message="Username already exists"), 409

    new_user = User(name=username, email=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    # Após registro, redirecionar para a página de login
    return redirect(url_for('user_login'))

@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    current_user_id = get_jwt_identity()
    data = request.json
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        user_id=current_user_id
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.serialize()), 201


@app.route('/tasks/view', methods=['GET'])
@jwt_required()
def view_tasks():
    current_user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=current_user_id).all()
    return render_template("tasks.html", tasks=tasks)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(user_id=current_user_id, id=task_id).first()
    if task:
        data = request.json
        task.title = data['title']
        task.description = data.get('description', task.description)
        task.is_complete = data.get('is_complete', task.is_complete)
        db.session.commit()
        return jsonify(task.serialize())
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(user_id=current_user_id, id=task_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})
    return jsonify({"error": "Task not found"}), 404
