from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from flask_login import UserMixin

from f_debate import db, login_manager

@login_manager.user_loader
def load_user(user_id: int) -> 'User':
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(20), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    image_file: str = db.Column(db.String(20), nullable=False, default='default.jpg')
    password: str = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec: int = 1800) -> str:
        with Serializer(current_app.config['SECRET_KEY'], expires_sec) as s:
            return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token: str) -> 'User':
        with Serializer(current_app.config['SECRET_KEY']) as s:
            try:
                user_id = s.loads(token)['user_id']
            except Exception:
                return None
            return User.query.get(user_id)

    def __repr__(self) -> str:
        return f"Пользователь('{self.username}', '{self.email}', '{self.image_file}')"