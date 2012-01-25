#!/usr/bin/env python
# coding: utf-8

"""
Converts a native Python dictionary into an XML string. 

* Supports item (int, float, bool, str, unicode) and collection (list and dict) data types with arbitrary nesting for the collections.

* Currently requires that the root object passed into the `dict2xml` function is a dict. In a later version, I'll probably revisit this to make it more generic (e.g. you can pass in a list or other data type).

* To satisfy XML syntax, it wraps all the dict keys/elements and values in a `<root> ... </root>` element.

* For lists of items, if each item is also a collection data type (lists, dict), the elements of that item are wrapped in a generic `<item> ... </item>` element.

* Item elements include an attribute with the data type (bool, int, float, string). Note: unicode elements get a `string` data type.

Copyright 2012 by Ryan McGreal. 

Released under the GNU General Public Licence, Version 2:  
<http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>
"""
debug = False

def notify(*args):
    """Prints debug information"""
    if debug == False: return
    for arg in args:
        print arg,
    print


def convert_dict(obj):
    """Converts a dict into an XML string."""
    output = []
    addline = output.append
    for k, v in obj.items():
        notify(k, v, type(v))
        if type(v) in (int, float, str, unicode):
            addline(convert_kv(k, v))
        elif type(v) == bool:
            addline(convert_bool(k, v))
        elif type(v) == dict:
            addline('<%s>%s</%s>' % (k, convert_dict(v), k))
        elif type(v) == list:
            addline('<%s>%s</%s>' % (k, convert_list(v), k))
    return ''.join(output)


def convert_list(items):
    """Converts a list into an XML string."""
    output = []
    addline = output.append
    for item in items:
        notify(item, type(item))
        if type(item) in (int, float, str, unicode):
            addline(convert_kv('item', item))
        elif type(item) == bool:
            addline(convert_bool('item', item))
        elif type(item) == dict:
            addline('<item>%s</item>' % (convert_dict(item)))
        elif type(item) == list:
            addline('<item>%s</item>' % (convert_list(item)))
    return ''.join(output)

def convert_kv(k, v):
    """Converts an int, float or string into an XML element"""
    return '<%s type="%s">%s</%s>' % (k, type(v).__name__ if type(v).__name__ != 'unicode' else 'str', v, k)

def convert_bool(k, v):
    """Converts a boolean into an XML element"""
    return '<%s type="bool">%s</%s>' % (k, str(v).lower(), k)

def dict2xml(obj):
    """Converts a python object into XML"""
    if type(obj) != dict:
        raise TypeError('Object to be converted to XML must be a dict.')
    output = []
    addline = output.append
    addline('<?xml version="1.0" encoding="UTF-8" ?>')
    addline('<root>%s</root>' % (convert_dict(obj)))
    return ''.join(output)
