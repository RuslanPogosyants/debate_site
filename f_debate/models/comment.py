from datetime import datetime

from f_debate import db


class Comment(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    body: str = db.Column(db.String(140))
    timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    post_id: int = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    username: str = db.Column(db.String, db.ForeignKey('user.username'), nullable=False)
