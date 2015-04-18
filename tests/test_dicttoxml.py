from unittest import TestCase
from dicttoxml import dicttoxml


class DictToXmlTest(TestCase):

    def test_empty_dict(self):
        result = dicttoxml({})
        self.assertEqual('<?xml version="1.0" encoding="UTF-8" ?><root></root>', result)

    def test_empty_dict_without_root(self):
        result = dicttoxml({}, root=False)
        self.assertEqual('', result)

    def test_empty_dict_with_custom_root(self):
        result = dicttoxml({}, custom_root='custom_root')
        self.assertEqual('<?xml version="1.0" encoding="UTF-8" ?><custom_root></custom_root>', result)
