# coding=utf-8
import logging
from flask import Blueprint, url_for
from flask_restplus import Api, fields
from manager.utilities.exceptions import global_error_handler

__author__ = 'anh.dv'
_logger = logging.getLogger(__name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
api_bp = Blueprint('api', __name__, url_prefix='/api')


class CustomAPI(Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)

    def page_mode(self, model_name, model_cls):
        return self.model(model_name, {
            'total_record': fields.Integer,
            'content': fields.List(fields.Nested(model_cls))
        })


api = CustomAPI(
    app=api_bp,
    version='1.0',
    title='Docker Manager APIs',
    validate=False,
    authorizations=authorizations,
)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    from manager.api.container import ns as ns_container
    from manager.api.docker import ns as ns_docker
    # ADD NAMESPACE
    api.add_namespace(ns_container)
    api.add_namespace(ns_docker)

    app.register_blueprint(api_bp)
    api.error_handlers[Exception] = global_error_handler
