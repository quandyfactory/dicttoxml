from unittest import TestCase
from dicttoxml import dicttoxml


class DictToXmlTest(TestCase):

    def test_empty_dict(self):
        xml = dicttoxml({})

        self.assertEqual('<?xml version="1.0" encoding="UTF-8" ?><root></root>', xml)

    def test_empty_dict_without_root(self):
        xml = dicttoxml({}, root=False)

        self.assertEqual('', xml)

    def test_empty_dict_with_custom_root(self):
        xml = dicttoxml({}, custom_root='custom_root')

        self.assertEqual('<?xml version="1.0" encoding="UTF-8" ?><custom_root></custom_root>', xml)
