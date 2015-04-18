from unittest import TestCase
from decimal import Decimal
from dicttoxml import get_xml_type
from helpers import long_compatibility

long = long_compatibility()


class GetXmlTypeTest(TestCase):
    def test_str_type(self):
        value = ''

        self.assertEqual(u'str', get_xml_type(value))

    def test_unicode_type(self):
        value = u''

        self.assertEqual(u'str', get_xml_type(value))

    def test_int_type(self):
        value = 1
        value = int(1)

        self.assertEqual(u'int', get_xml_type(value))
        self.assertEqual(u'int', get_xml_type(value))

    def test_long_type(self):
        value = long(1)

        self.assertEqual(u'int', get_xml_type(value))

    def test_float_type(self):
        value = 1.1
        value = float(1)

        self.assertEqual(u'float', get_xml_type(value))
        self.assertEqual(u'float', get_xml_type(value))

    def test_decimal_type(self):
        value = Decimal(1)

        self.assertEqual(u'number', get_xml_type(value))

    def test_number_type(self):
        value = complex(1)

        self.assertEqual(u'number', get_xml_type(value))

    def test_bool_type(self):
        value = True

        self.assertEqual(u'bool', get_xml_type(value))

    def test_none_type(self):
        value = None

        self.assertEqual(u'null', get_xml_type(value))

    def test_dict_type(self):
        value = {}

        self.assertEqual(u'dict', get_xml_type(value))

    def test_list_type(self):
        value = []

        self.assertEqual(u'list', get_xml_type(value))

    def test_set_type(self):
        value = set([])

        self.assertEqual(u'list', get_xml_type(value))

    def test_tuple_type(self):
        value = ()

        self.assertEqual(u'list', get_xml_type(value))

    def test_custom_type(self):
        class CustomType(object):
            pass
        value = CustomType()

        self.assertEqual('CustomType', get_xml_type(value))
