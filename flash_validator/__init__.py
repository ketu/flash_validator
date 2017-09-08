from functools import wraps
from .condition import Condition
from .rule import BaseRule, RequiredRule, RegexRule
from .error import ValidationError
from . import extra_source

def validator(*params):
    def validate_request(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            errors, args = validate(params)
            return func(*args)
        return wrapper

    return validate_request


def validate(params):
    for condition in params:
        condition.apply()

