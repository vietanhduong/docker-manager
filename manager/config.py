# coding=utf-8
import logging
import os

__author__ = 'AnhDV'
_logger = logging.getLogger(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__)
))


class Config(object):
    # APP
    FLASK_APP_SECRET_KEY = os.environ.get('SECRET_KEY') or 'something-very-secret'
    REVERSE_PROXY_SETUP = True
    # ENV
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    # LOG CONFIG
    LOGGING_CONFIG_FILE = os.path.join(ROOT_DIR, 'etc', 'logging.ini')


class TestingConfig(Config):
    TESTING = True
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
