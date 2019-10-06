import os
import logging
from flask_compress import Compress

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
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    #Mongo Connection
    Hostname = "localhost"
    Port = 27017
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
    #Configure Compressing
    Compress(app)