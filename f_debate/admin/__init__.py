from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from f_debate.models import User, Post
from f_debate import db
from f_debate import create_app

app = create_app()

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
