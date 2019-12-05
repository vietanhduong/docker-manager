# coding=utf-8
import os
from logging import handlers
from manager.utilities.common import mkdir, ROOT

__author__ = 'anh.dv'


_LOG_PATH = os.path.join(ROOT, "logs")


class RotatingFileHandler(handlers.RotatingFileHandler):

    def __init__(self, filename, mode='a', max_bytes=0, backup_count=0, encoding=None, delay=False):
        mkdir(_LOG_PATH)

        dest = os.path.join(_LOG_PATH, filename)

        super().__init__(dest, mode, max_bytes, backup_count, encoding, delay)

    def doRollover(self):
        super().doRollover()

    def shouldRollover(self, record):
        return super().shouldRollover(record)
