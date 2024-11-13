from flask import request
from user_app.services.user_service import UserService
from user_app.views.user_view import UserView


class UserController:
    @staticmethod
    def get_all_users():
        users = UserService.get_all_users()
        return UserView.render_users(users), 200

    @staticmethod
    def get_user(username):
        user = UserService.get_user_by_username(username)
        if not user: # if user is None:
            return UserView.render_error('User not found'), 404
        return UserView.render_user(user), 200

    @staticmethod
    def create_user():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('full_name', '')
        bio = data.get('bio', '')

        user = UserService.create_user(username, email, password, full_name, bio)
        return UserView.render_success('User created successfully', user.user_id), 201

    @staticmethod
    def login_user():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = UserService.verify_user(username, password)
        if user:
            return UserView.render_success('Login successful', user.user_id), 200
        return UserView.render_error('Invalid username or password'), 401

    @staticmethod
    def tag_post(hashtag):
        data = request.get_json()
        post_id = data.get('post_id')
        user_id = data.get('user_id')

        # Input validation
        if not post_id or not user_id or not hashtag:
            return UserView.render_error('Post ID, user ID, and hashtag are required'), 400

        success = UserService.tag_post(hashtag, post_id, user_id)
        if success:
            return UserView.render_success('Post tagged successfully'), 200
        return UserView.render_error('Failed to tag post'), 400