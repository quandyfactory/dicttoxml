import unittest
from collections import OrderedDict

from dicttoxml import dicttoxml


class TestDictToXml(unittest.TestCase):
    def test_primitive_types(self):
        data = OrderedDict()
        data['true'] = True
        data['false'] = False
        data['int'] = 42
        data['float'] = 42.0
        data['None'] = None
        data['string'] = 'str_value'

        xml = dicttoxml(data, root=False, attr_type=False)
        self.assertEqual(
            xml, 
            (
                '<true>true</true>'
                '<false>false</false>'
                '<int>42</int>'
                '<float>42.0</float>'
                '<None></None>'
                '<string>str_value</string>'
            )
        )


if __name__ == '__main__':
    unittest.main()
