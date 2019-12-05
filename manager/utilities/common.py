# coding=utf-8
import os
import sys
import errno

__author__ = 'anh.dv'

ROOT = os.path.abspath(os.path.join(os.path.dirname(sys.modules['manager'].__file__), ".."))
ETC = os.path.join(ROOT, "etc")


def mkdir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise
