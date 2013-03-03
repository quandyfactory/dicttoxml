#!/usr/bin/env python
# coding: utf-8
import logging
"""
Converts a native Python dictionary into an XML string. Supports int, float, str, unicode, list, dict and arbitrary nesting.
"""
__version__ = 1.0
# use logging.DEBUG for debugging
logging.basicConfig(level=logging.INFO)

def xml_escape(s):
    if type(s) == str:
        s = s.replace('"',  '&quot;')
        s = s.replace('\'', '&apos;')
        s = s.replace('<',  '&lt;')
        s = s.replace('>',  '&gt;')
        s = s.replace('&',  '&amp;')
    elif type(s) == str:
        s = s.replace('"',  '&quot;')
        s = s.replace('\'', '&apos;')
        s = s.replace('<',  '&lt;')
        s = s.replace('>',  '&gt;')
        s = s.replace('&',  '&amp;')
    return s

def convert(obj):
    """Routes the elements of an object to the right function to convert them based on their data type"""
    logging.debug("Inside convert(): obj=%(obj)s",obj=obj)
    if type(obj) in (int, float, str, str):
        return convert_kv('item', obj)
    if hasattr(obj, 'isoformat'):
        return convert_kv('item', obj.isoformat())
    if type(obj) == bool:
        return convert_bool('item', obj)
    if type(obj) == dict:
        return convert_dict(obj)
    if type(obj) in (list, set, tuple):
        return convert_list(obj)
    raise TypeError("Unsupported data type: %(obj)s (%(type)s)".format(obj=obj, type=type(obj).__name__))

def convert_dict(obj):
    """Converts a dict into an XML string."""
    logging.debug("Inside convert_dict(): obj=%(obj)s",obj=obj)
    output = []
    addline = output.append
    for k, v in list(obj.items()):
        logging.debug("Looping inside convert_dict(): k=%(key)s, v=%(value)s, type(v)=%(type)s", key=k, value=v, type=type(v))
        try:
            if k.isdigit():
                k = 'n%s' % (k)
        except:
            if type(k) in (int, float):
                k = 'n%s' % (k)
        if type(v) in (int, float, str, str):
            addline(convert_kv(k, v))
        elif hasattr(v, 'isoformat'): # datetime
            addline(convert_kv(k, v.isoformat()))
        elif type(v) == bool:
            addline(convert_bool(k, v))
        elif type(v) == dict:
            addline('<%s>%s</%s>' % (k, convert_dict(v), k))
        elif type(v) in (list, set, tuple):
            addline('<%s>%s</%s>' % (k, convert_list(v), k))
        elif v is None:
            addline('<%s></%s>' % (k, k))
        else:
            raise TypeError("Unsupported data type: %(obj)s (%(type)s)".format(obj=v, type=type(v).__name__))
    return ''.join(output)

def convert_list(items):
    """Converts a list into an XML string."""
    logging.debug("Inside convert_list(): items=%(items)s", items=items)
    output = []
    addline = output.append
    for item in items:
        logging.debug("Looping inside convert_list(): item=%(item)s, type(item)=%(type)s", item=item, type=type(item))
        if type(item) in (int, float, str, str):
            addline(convert_kv('item', item))
        elif hasattr(item, 'isoformat'): # datetime
            addline(convert_kv('item', v.isoformat()))
        elif type(item) == bool:
            addline(convert_bool('item', item))
        elif type(item) == dict:
            addline('<item>%s</item>' % (convert_dict(item)))
        elif type(item) in (list, set, tuple):
            addline('<item>%s</item>' % (convert_list(item)))
        else:
            raise TypeError('Unsupported data type: %s (%s)' % (item, type(item).__name__))
    return ''.join(output)

def convert_kv(k, v):
    """Converts an int, float or string into an XML element"""
    logging.debug("convert_kv(): k=%(key)s, v=%(value)s", key=k, value=v)
    return '<%s type="%s">%s</%s>' % (k, type(v).__name__ if type(v).__name__ != 'unicode' else 'str', xml_escape(v), k)

def convert_bool(k, v):
    """Converts a boolean into an XML element"""
    logging.debug("convert_bool): k=%(key)s, v=%(value)s", key=k, value=v)
    return '<%s type="bool">%s</%s>' % (k, str(v).lower(), k)

def dicttoxml(obj, root=True):
    """Converts a python object into XML"""
    logging.debug("dict2xml(): obj=%(obj)s", obj=obj)
    output = []
    addline = output.append
    if root == True:
        addline('<?xml version="1.0" encoding="UTF-8" ?>')
        addline('<root>%s</root>' % (convert(obj)))
    else:
        addline(convert(obj))
    return ''.join(output)
