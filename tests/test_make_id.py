from unittest import TestCase
from dicttoxml import make_id


class MakeIdTest(TestCase):

    def test_element_name(self):
        result = make_id('element')
        self.assertEqual('element_', result[:8])

    def test_rand_is_int(self):
        result = make_id('element')
        self.assertIsInstance(int(result[8:]), int)
