# /usr/bin/env python
# -*- coding:utf8 -*-
from .source import DictSource
from .error import ValidationError


class Condition(object):

    find_field_value_func_name = 'find_field_value'

    def __init__(self, field, rules, source):
        self.field = field
        self.rules = rules
        self.source = source

    def get_source_data(self):

        if isinstance(self.source, dict):
            return DictSource(self.source)

        if hasattr(self.source, self.find_field_value_func_name)\
                and callable(getattr(object, self.find_field_value_func_name)):
            return self.source

        raise ValueError('unknown data source')

    def get_value_from_source(self):
        source = self.get_source_data()
        if not source:
            return None

        find_field_value_func = getattr(source, self.find_field_value_func_name)
        return find_field_value_func(self.field)

    def apply(self):
        value = self.get_value_from_source()
        for r in self.rules:
            is_passed = r.validate(value)
            if not is_passed:
                raise ValidationError(r, self.field)



