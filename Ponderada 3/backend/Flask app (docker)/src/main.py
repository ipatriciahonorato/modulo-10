import io
from flask import Flask, jsonify, request, send_file
from flask_jwt_extended import JWTManager
from database.database import db
from logs.logger import setup_logger
from services.image_service import process_image_file
from services.user_service import get_token, register
from PIL import Image
from rembg import remove 

app = Flask(__name__, template_folder="templates")
logger = setup_logger('main')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

app.config["JWT_SECRET_KEY"] = "goku-vs-vegeta" 
app.config['JWT_TOKEN_LOCATION'] = ['cookies', 'headers']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)

def create_database():
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully")

with app.app_context():
    db.create_all()

# Token verification serves as login endpoint
@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # return token in json format
    token = get_token(username, password) 
    return jsonify(token=token)

@app.route("/register", methods=["POST"])
def user_register():
    username = request.form.get("username")
    password = request.form.get("password")
    return register(username, password)

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img_io = process_image_file(file.stream)
        return send_file(img_io, mimetype='image/png')
    except ValueError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
