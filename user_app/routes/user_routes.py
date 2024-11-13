from flask import Blueprint,request
from user_app.controllers.user_controller import UserController


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/api/users', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@user_bp.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    return UserController.get_user(username)

@user_bp.route('/api/users', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_bp.route('/api/users/login', methods=['POST'])
def login_user():
    return UserController.login_user()

@user_bp.route('/api/posts/tag', methods=['POST'])  
def tag_post():
    hashtag = request.json.get('hashtag')  
    return UserController.tag_post(hashtag)