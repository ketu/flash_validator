from functools import wraps
from .condition import Condition
from . import rule
from .error import ValidationError

__all__ = ["Condition", "rule", "ValidationError", "validator"]

def validator(*params):
    def validate_request(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args = apply_validation(params)
            return func(*args)
        return wrapper

    return validate_request


def apply_validation(params):
    values = []
    for cond in params:
        value = cond.apply()
        values.append(value)
    return values



