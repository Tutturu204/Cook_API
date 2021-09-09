

class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://Mik:Suren1997@localhost/Smilecock_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "secret-key"
    JWT_ERROR_MESSAGE_KEY = "msg"


    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]