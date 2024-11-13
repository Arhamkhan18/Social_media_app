from shared.models.user_model import User
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash
from shared.models.post_model import  Post

class UserService:
    @staticmethod
    def create_user(username, email, password, full_name, bio):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password, full_name=full_name, bio=bio)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def verify_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

  
    @staticmethod
    def tag_post(hashtag, post_id, user_id):
        
        post = Post.query.filter_by(post_id=post_id, user_id=user_id).first()
        if post:
            
            if post.content and hashtag not in post.content:
                post.content += f" #{hashtag}"  
                db.session.commit()
                return post
            return None  
        return None  
    
