from unittest import TestCase
from dicttoxml import get_unique_id


class GetUniqueIdTest(TestCase):

    def test_get_id(self):
        unique_id = get_unique_id('element')

        self.assertIsNotNone(unique_id)
