from functools import wraps

from flask import has_app_context, current_app, request
from flask_restplus import Namespace as OriginalNamespace, marshal, Mask
from flask_restplus._http import HTTPStatus
from flask_restplus.utils import merge, unpack

from manager.utilities.model import Model, OrderedModel
from manager.utilities.response_wrapper import wrap_response


class Namespace(OriginalNamespace):

    def expect(self, *inputs, **kwargs):
        """
        A decorator to Specify the expected input model

        :param ModelBase|Parse inputs: An expect model or request parser
        :param bool validate: whether to perform validation or not

        """
        expect = []
        params = {
            'validate': kwargs.get('validate', None) or self._validate,
            'expect': expect
        }

        for param in inputs:
            expect.append(param)

        return self.doc(**params)

    def model(self, name=None, model=None, mask=None, **kwargs):
        '''
        Register a model

        .. seealso:: :class:`Model`
        '''
        cls = OrderedModel if self.ordered else Model
        model = cls(name, model, mask=mask)
        model.__apidoc__.update(kwargs)
        return self.add_model(name, model)

    def marshal_with(self, fields, as_list=False,
                     code=HTTPStatus.OK, description=None, **kwargs):
        """
        A decorator specifying the fields to use for serialization.
        :param dict fields: expected fields to use for serialization
        :param bool as_list: Indicate that the return type
        is a list (for the documentation)
        :param int code: Optionally give the expected HTTP response code
        if its different from 200
        :param description: optional description
        """

        def wrapper(func):
            doc = {
                'responses': {
                    code: (description, [fields]) if as_list else (
                        description, fields)
                },
                '__mask__': kwargs.get('mask', True),
                # Mask values can't be determined outside app context
            }
            func.__apidoc__ = merge(getattr(func, '__apidoc__', {}), doc)

            kwargs['ordered'] = self.ordered

            return marshal_with(fields, **kwargs)(func)

        return wrapper


class marshal_with(object):
    """A decorator that apply marshalling to the return values of your methods.
    """

    def __init__(self, fields, **kwargs):
        """
        :param fields: a dict of whose keys will make up the final
                       serialized response output
        """
        self.fields = fields
        self.envelope = kwargs.get('envelope')
        self.skip_none = kwargs.get('skip_none', False)
        self.ordered = kwargs.get('ordered', False)
        self.mask = Mask(kwargs.get('mask'), skip=True)

    def __is_tuple(self, resp, mask):
        if isinstance(resp, tuple):
            data, code, headers = unpack(resp)
            return (
                wrap_response(marshal(
                    data,
                    self.fields,
                    self.envelope,
                    self.skip_none,
                    mask,
                    self.ordered)
                ),
                code,
                headers
            )
        else:
            return wrap_response(
                marshal(resp, self.fields, self.envelope, self.skip_none,
                        mask, self.ordered))

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            mask = self.mask
            if has_app_context():
                mask_header = current_app.config['RESTPLUS_MASK_HEADER']
                mask = request.headers.get(mask_header) or mask
            return self.__is_tuple(resp, mask)

        return wrapper
