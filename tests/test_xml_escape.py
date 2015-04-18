from unittest import TestCase
from dicttoxml import xml_escape


class XmlEscapeTest(TestCase):

    def test_non_str_or_unicode(self):
        escaped_result = xml_escape(1)

        self.assertEqual(1, escaped_result)

    def test_ampersand(self):
        escaped_result = xml_escape('&')

        self.assertEqual(u'&amp;', escaped_result)

    def test_quotation_mark(self):
        escaped_result = xml_escape('"')

        self.assertEqual(u'&quot;', escaped_result)

    def test_apostrophe(self):
        escaped_result = xml_escape('\'')

        self.assertEqual(u'&apos;', escaped_result)

    def test_less_than(self):
        escaped_result = xml_escape('<')

        self.assertEqual(u'&lt;', escaped_result)

    def test_greater_than(self):
        escaped_result = xml_escape('>')

        self.assertEqual(u'&gt;', escaped_result)
