from flask import jsonify, make_response
from flask_jwt_extended import create_access_token
from database.models import User
from database.database import db
from logs.logger import setup_logger

logger = setup_logger('user_service')

def register(user, password):
    logger.info(f"Registering user {user}")

    if not user or not password:
        logger.error("Missing username or password")
        return make_response("Missing username or password", 400)

    existing_user = User.query.filter_by(email=user).first()
    if existing_user:
        logger.error(f"Username: {user} already exists")
        return make_response("Username already exists", 409)

    new_user = User(name=user, email=user, password=password)
    db.session.add(new_user)
    db.session.commit()

    logger.info(f"User {user} created successfully")
    return make_response("User created successfully", 200)

def get_token(user, password):
    logger.info(f"Getting token for user {user}")
    user = User.query.filter_by(email=user, password=password).first()
    if user is None:
        logger.error("Bad username or password")
        return jsonify({"msg": "Bad username or password"}), 401
    
    logger.info(f"Token for user {user} created successfully")
    access_token = create_access_token(identity=user.id)
    return access_token