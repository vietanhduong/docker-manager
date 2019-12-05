# coding=utf-8
import datetime
import decimal
import enum
import logging

import flask

__author__ = 'anh.dv'
_logger = logging.getLogger(__name__)


class JSONEncoder(flask.json.JSONEncoder):
    """Customized flask JSON Encoder"""

    def __cast_integral_value(self, o):
        return int(o) if o == o.to_integral_value() else float(0)

    def default(self, o):
        """
        Override default encoder method
        :param Any o:
        """

        switch = {
            decimal.Decimal: self.__cast_integral_value(o),
            (datetime.datetime, datetime.date): o.isoformat(sep=' '),
            enum.Enum: o.value,
            tuple: list(o)
        }

        if hasattr(o, '__json__'):
            ret = o.__json__()
        else:
            ret = switch.get(type(o), super().default(o))

        return ret


_default_json_encoder = JSONEncoder()
json_encode = _default_json_encoder.encode