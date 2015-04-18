from unittest import TestCase
from dicttoxml import make_attrstring


class MakeAttrstringTest(TestCase):

    def test_empty_dict(self):
        attributes_string = make_attrstring({})

        self.assertEqual(u'', attributes_string)

    def test_dict_with_one_key(self):
        attributes_string = make_attrstring({
            'one': 1
        })

        self.assertEqual(u' one="1"', attributes_string)

    def test_dict_with_more_than_one_key(self):
        attributes_string = make_attrstring({
            'one': 1,
            'two': 2
        })

        self.assertEqual(u' two="2" one="1"', attributes_string)
