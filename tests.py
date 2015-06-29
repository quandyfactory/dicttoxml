import unittest
from dicttoxml import dicttoxml


class TestDictToXmlWithCustomItems(unittest.TestCase):

    _src_dict = {'Tests': [1, 2, 3]}

    def test_custom_items(self):
        xml = dicttoxml(self._src_dict, custom_item_func=lambda x: x[:-1])
        self.assertEqual(xml, '<?xml version="1.0" encoding="UTF-8" ?><root><Tests type="list"><Test type="int">1</Test><Test type="int">2</Test><Test type="int">3</Test></Tests></root>')

    def test_default_items(self):
        xml = dicttoxml(self._src_dict)
        self.assertEqual(xml, '<?xml version="1.0" encoding="UTF-8" ?><root><Tests type="list"><item type="int">1</item><item type="int">2</item><item type="int">3</item></Tests></root>')

if __name__ == '__main__':
    unittest.main()
