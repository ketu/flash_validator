# /usr/bin/env python
# -*- coding:utf8 -*-
import re


class BaseRule(object):
    error_message = "%s can not pass the rule"

    def __init__(self, pattern=None):
        self.pattern = pattern

    def validate(self, value):
        return True


class RequiredRule(BaseRule):
    error_message = "%s is required"

    def validate(self, value):
        if not value:
            return False
        return True


class RegexRule(BaseRule):
    def __init__(self, pattern):

        if isinstance(pattern, str):
            pattern = re.compile(pattern)

        super(RegexRule, self).__init__(pattern)

    def validate(self, value):
        group = self.pattern.fullmatch(str(value))
        if not group:
            return False
        return True


