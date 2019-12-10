# coding=utf-8
import logging

__author__ = 'anh.dv'
_logger = logging.getLogger(__name__)


def init_app(app, **kwargs):
    """
    Init views
    :param flask.app.Flask app:
    """
    from .index import index_bp

    app.register_blueprint(index_bp)
