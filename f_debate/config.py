
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///debate.db'
    SECRET_KEY = 'secret_key_for_debate'

    MAIL_SERVER = ...
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ...
    MAIL_PASSWORD = ...
