# coding=utf-8
import logging
from flask import render_template, Blueprint

__author__ = 'anh.dv'
_logger = logging.getLogger(__name__)

index_bp = Blueprint('view', __name__, url_prefix='/')


@index_bp.route('')
def index():
    return render_template("index.html")