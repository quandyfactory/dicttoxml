from unittest import TestCase
from dicttoxml import xml_escape


class XmlEscapeTest(TestCase):

    def test_non_str_or_unicode(self):
        result = xml_escape(1)

        self.assertEqual(1, result)

    def test_ampersand(self):
        result = xml_escape('&')

        self.assertEqual(u'&amp;', result)

    def test_quotation_mark(self):
        result = xml_escape('"')

        self.assertEqual(u'&quot;', result)

    def test_apostrophe(self):
        result = xml_escape('\'')

        self.assertEqual(u'&apos;', result)

    def test_less_than(self):
        result = xml_escape('<')

        self.assertEqual(u'&lt;', result)

    def test_greater_than(self):
        result = xml_escape('>')

        self.assertEqual(u'&gt;', result)
