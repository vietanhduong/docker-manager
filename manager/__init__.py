# coding=utf-8
import flask
import logging
import logging.config
import os

from manager.utilities import common, json_encoder

__author__ = 'anh.dv'


def _before_request():
    pass


def _after_request(response):
    request = flask.request
    origin = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, ' \
                                                       'Accept, Authorization, Content-Disposition'

    return response


def setup_logging(default_level=logging.INFO):
    path = os.path.join(common.ETC, 'logging.ini')
    common.mkdir(os.path.join(common.ROOT, "logs"))
    if os.path.exists(path):
        logging.config.fileConfig(path, disable_existing_loggers=True)
    else:
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default configs')


def create_app(conf):
    from manager import api, views
    _app = flask.Flask(__name__, static_folder="statics/dist", template_folder="statics")
    _app.config.from_object(conf)
    _app.json_encoder = json_encoder.JSONEncoder

    # setup logging
    _app.config['PROPAGATE_EXCEPTIONS'] = True
    setup_logging()

    _app.before_request(_before_request)
    _app.after_request(_after_request)
    _app.secret_key = conf.FLASK_APP_SECRET_KEY

    api.init_app(_app)
    views.init_app(_app)
    return _app
