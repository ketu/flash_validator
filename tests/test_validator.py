from flash_validator import validator, Condition, rules, ValidationError, extra_source
from unittest import TestCase
import flask



app = flask.Flask(__name__)
app.testing = True

@app.route('/<path:sku>')
@validator(
    Condition('sku', [rules.RegexRule("\d+")], extra_source.flask.FlaskViewArgsSource())
)
def main(sku):
    print(sku)
    print('ik')
    return 'ok'
class TestValidator(TestCase):

    def test_required_rule(self):

        c = Condition('sku', [rules.RegexRule("\d+")], {
            "name":"asdfasdsadfa",
            'sku': "345435ddff123"
        })

        with self.assertRaises(ValidationError):
            c.apply()


    def test_flask_data_source(self):
        with app.test_client() as client:
            with self.assertRaises(ValidationError):
                client.get('/234sdfa3242')


