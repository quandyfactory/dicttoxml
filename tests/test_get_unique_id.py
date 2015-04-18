from unittest import TestCase
from dicttoxml import get_unique_id


class GetUniqueIdTest(TestCase):

    def test_get_id(self):
        result = get_unique_id('element')

        self.assertIsInstance(int(result[8:]), int)

    # def test_get_existing_id(self):
    # needs a refactor to be able to test
