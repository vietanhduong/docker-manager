# coding=utf-8
import logging
import os
from manager import create_app, config
from flask import Flask

__author__ = 'anh.dv'
_logger = logging.getLogger(__name__)

app: Flask = create_app(config.config.get(os.getenv("FLASK_ENV") or "development"))

if __name__ == '__main__':
    app.run()
