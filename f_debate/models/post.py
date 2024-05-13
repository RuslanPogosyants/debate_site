from datetime import datetime
from f_debate import db


class Post(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    date_posted: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content: str = db.Column(db.Text, nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    comments = db.relationship('Comment', backref='title', lazy='select', cascade='all, delete-orphan')
