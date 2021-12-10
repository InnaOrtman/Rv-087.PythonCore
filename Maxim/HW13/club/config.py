import os
import conf_ignor
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = conf_ignor.SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = "[Reader Club]"
    FLASKY_MAIL_SENDER = conf_ignor.FLASKY_MAIL_SENDER
    FLASKY_ADMIN = conf_ignor.FLASKY_ADMIN

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = conf_ignor.MAIL_USERNAME
    MAIL_PASSWORD = conf_ignor.MAIL_PASSWORD
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app/db/db.sqlite")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('TEST_DATABASE_URL') or \
        "sqlite:///" + os.path.join(basedir, "app/db/test.sqlite")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}
