import logging
import os

from werkzeug.exceptions import HTTPException as BaseHTTPException

from manager.utilities.response_wrapper import wrap_response

_logger = logging.getLogger(__name__)

FLASK_ENV = os.getenv("FLASK_ENV", "development")


class HTTPException(BaseHTTPException):
    def __init__(self, code=400, message=None, errors=None):
        super().__init__(description=message, response=None)
        self.code = code
        self.errors = errors
        self.message = message
        _logger.error(f'code: {code}, message: {message}, errors: {errors}')


class BadRequestException(HTTPException):
    def __init__(self, message='Bad Request', errors=None):
        super().__init__(code=400, message=message, errors=errors)


class NotFoundException(HTTPException):
    def __init__(self, message='Resource Not Found', errors=None):
        super().__init__(code=404, message=message, errors=errors)


class UnAuthorizedException(HTTPException):
    def __init__(self, message='UnAuthorized', errors=None):
        super().__init__(code=401, message=message, errors=errors)


class ForbiddenException(HTTPException):
    def __init__(self, message='Permission Denied', errors=None):
        super().__init__(code=403, message=message, errors=errors)


class NotImplementedException(HTTPException):
    def __init__(self, message='Server does not support', errors=None):
        super().__init__(code=501, message=message, errors=errors)


def global_error_handler(e):
    _logger.exception(e)

    code = 500
    errors = None
    message = str(e)
    if isinstance(e, BaseHTTPException):
        code = e.code
        message = e.description
    if isinstance(e, HTTPException):
        errors = e.errors
        message = e.message

    res = wrap_response(None, message, code)
    if errors:
        res[0]['errors'] = errors if FLASK_ENV != "production" else "System failed."
    return res
