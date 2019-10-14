import os
import logging
from flask_compress import Compress
from flask_mail import Mail

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'sporty.log'
    LOGGING_LEVEL = logging.DEBUG
    SECURITY_PASSWORD_SALT = '8312hjf123'
    CACHE_TYPE = 'simple'
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml',
                          'application/json', 'application/javascript']
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500
    SUPPORTED_LANGUAGES = {'en': 'English'}

    APP_HOST = "0.0.0.0"
    APP_PORT = 3333

class GoogleConfig(BaseConfig):
    # Google Authentication
    GOOGLE_CLIENT_ID = "1066877482822-pj66le6imct9gr93qhcb6mbm137745mi.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "yCQSKwqRIyQHVERITU1BM1ll"
    REDIRECT_URI = 'https://localhost:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/v2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    #Mongo Connection
    Hostname = "localhost"
    DB_Port = 27017
    DB_NAME = "local"
    SECRET_KEY = '5f18df59bd0eaafc1f2d79c396d6108d7e96073eacd0776a'

class StagingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = 'staging'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

config = {
    "dev": "app.config.DevelopmentConfig",
    "staging": "app.config.StagingConfig",
    "prod": "app.config.ProductionConfig",
    "default": "app.config.DevelopmentConfig"
}

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
    #Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.config.update(dict(
        DEBUG = True,
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 587,
        MAIL_USE_TLS = True,
        MAIL_USE_SSL = False,
        MAIL_USERNAME = 'sportvolt0@gmail.com',
        MAIL_PASSWORD = '0308SDAssa',
        MAIL_FAIL_SILENTLY=False,
    ))
    print("mail server started")
    #Configure Compressing
    Compress(app)