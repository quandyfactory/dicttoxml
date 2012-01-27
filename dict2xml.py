#!/usr/bin/env python
# coding: utf-8

"""
Converts a native Python dictionary into an XML string. Supports int, float, str, unicode, list, dict and arbitrary nesting.
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
