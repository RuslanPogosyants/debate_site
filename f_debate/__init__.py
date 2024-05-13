from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from f_debate.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from f_debate.blueprint import main, posts, users
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)

    return app
