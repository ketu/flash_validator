from flash_validator import validator, Condition, rule, ValidationError
from flash_validator.extra_source.flask import FlaskViewArgsSource, FlaskJsonSource, FlaskQuerySource, FlaskFormSource
from unittest import TestCase
import flask
import requests



app = flask.Flask(__name__)
app.testing = True

@app.route('/<path:sku>', methods=['POST', 'GET'])
@validator(
    Condition('sku', [rule.RegexRule("\d+")], FlaskViewArgsSource()),
    Condition('name', [rule.RegexRule("\d+")], FlaskQuerySource())
)
def main(sku):
    print(sku)
    print('ik')
    return 'ok'
class TestValidator(TestCase):

    def test_required_rule(self):

        c = Condition('sku', [rule.RegexRule("\d+")], {
            "name":"asdfasdsadfa",
            'sku': "345435ddff123"
        })

        with self.assertRaises(ValidationError):
            c.apply()


    def test_flask_data_source(self):
        with app.test_client() as client:
            #with self.assertRaises(ValidationError):
                #client.post('/23432423', data={"name":"12sdasad3"})
            data = dict(name="Jesse")
            client.get('/234332442?name=sdfa')


