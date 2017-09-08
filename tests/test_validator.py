from flash_validator import RequiredRule, RegexRule, Condition, ValidationError
from unittest import TestCase



class TestValidator(TestCase):

    def test_required_rule(self):

        c = Condition('sku', [RequiredRule(), RegexRule("\d+")], {
            "name":"asdfasdsadfa",
            'sku': "345435ff123"
        })

        with self.assertRaises(ValidationError):
            c.apply()



