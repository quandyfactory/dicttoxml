#!/usr/bin/env python

import os, sys
import unittest
import dicttoxml

class UnitTests(unittest.TestCase):

    def test_xmltodict(self):
        input = {
            'string' : "This is a string with special characters",
            'empty_string' : '',
            'int' : 1002,
            'float' : 12.56,
            'other_float' : float(80),
            'boolean' : False,
            'none_type' : None,
            'list' : [99, 'sheep', 'dog'],
            'empty_list' : [],
            'list_of_dicts' : [{}, {'hi_there': 7, 'owl': 'exterminator'}, {'foo': 56.2, 'ok': True}],
            'dict_of_lists' : {'list1': [3, 6, 'dog', 'cat', False], 'empty_list': []},
            'nested_lists' : [[4, 5, 6, 7], [1, 2, 3, 4, [5, 6, 7, 8]]]
        }
        xml = dicttoxml.dicttoxml(input)
        output = dicttoxml.xmltodict(xml)
        self.assertEqual({'root': input}, output)

if __name__== "__main__":
    unittest.main()