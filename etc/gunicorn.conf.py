# coding=utf-8
import os
import logging

__author__ = 'anh.dv'

_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
))

_ETC = os.path.join(_ROOT, 'etc')

bind = '0.0.0.0:5000'

workers = 9

timeout = 180  # 3 minutes
keepalive = 24 * 3600  # 1 day

logconfig = os.path.join(_ETC, 'logging.ini')
