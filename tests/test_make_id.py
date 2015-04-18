from unittest import TestCase
from dicttoxml import make_id


class MakeIdTest(TestCase):

    def setUp(self):
        self.element = 'element'

    def test_id_name(self):
        generated_id = make_id(self.element)

        self.assertEqual('element_', self._get_id_prefix(generated_id))

    def test_id_sufix_is_int(self):
        generated_id = make_id(self.element)

        self.assertIsInstance(int(self._get_id_sufix(generated_id)), int)

    def _get_id_prefix(self, generated_id):
        return generated_id[:self._get_cut_position()]

    def _get_id_sufix(self, generated_id):
        return generated_id[self._get_cut_position():]

    def _get_cut_position(self):
        return len(self.element) + 1
