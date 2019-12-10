# coding=utf-8
import os
import sys
import errno
import re

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


_under_scorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_under_scorer2 = re.compile('([a-z0-9])([A-Z])')


def to_snake_case(s):
    subbed = _under_scorer1.sub(r'\1_\2', s)
    return _under_scorer2.sub(r'\1_\2', subbed).lower()


def __convert(src, f):
    if not isinstance(src, list) and not isinstance(src, dict):
        return src

    if isinstance(src, list):
        return [__convert(item, f) for item in src]

    ret = {}

    for k, v in src.items():
        new_v = v
        ret[f(k)] = __convert(new_v, f)

    return ret


def convert_camel_to_snake(src):
    return __convert(src, to_snake_case)
