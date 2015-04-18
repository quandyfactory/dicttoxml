from unittest import TestCase
from decimal import Decimal
from dicttoxml import get_xml_type
from helpers import long_compatibility

long = long_compatibility()


class GetXmlTypeTest(TestCase):
    def test_str_type(self):
        self.assertEqual(u'str', get_xml_type(''))

    def test_unicode_type(self):
        self.assertEqual(u'str', get_xml_type(u''))

    def test_int_type(self):
        self.assertEqual(u'int', get_xml_type(1))
        self.assertEqual(u'int', get_xml_type(int(1)))

    def test_long_type(self):
        self.assertEqual(u'int', get_xml_type(long(1)))

    def test_float_type(self):
        self.assertEqual(u'float', get_xml_type(1.1))
        self.assertEqual(u'float', get_xml_type(float(1)))

    def test_decimal_type(self):
        self.assertEqual(u'number', get_xml_type(Decimal(1)))

    def test_number_type(self):
        self.assertEqual(u'number', get_xml_type(complex(1)))

    def test_bool_type(self):
        self.assertEqual(u'bool', get_xml_type(True))

    def test_none_type(self):
        self.assertEqual(u'null', get_xml_type(None))

    def test_dict_type(self):
        self.assertEqual(u'dict', get_xml_type({}))

    def test_list_type(self):
        self.assertEqual(u'list', get_xml_type([]))

    def test_set_type(self):
        self.assertEqual(u'list', get_xml_type(set([])))

    def test_tuple_type(self):
        self.assertEqual(u'list', get_xml_type(()))

    def test_custom_type(self):
        class CustomType(object):
            pass

        self.assertEqual('CustomType', get_xml_type(CustomType()))
