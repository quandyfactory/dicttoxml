#!/usr/bin/env python
# coding: utf-8

"""
Converts a native Python dictionary into an XML string. Supports int, float, str, unicode, list, dict and arbitrary nesting.
"""
__version__ = 0.9
debug = False

def debug_notify(*args):
    """Prints debug information"""
    if debug == False: 
        return
    for arg in args:
        print '%s; ' % (str(arg))
    print '\n'

def xml_escape(s):
    if type(s) == str:
        s = s.replace('&',  '&amp;')
        s = s.replace('"',  '&quot;')
        s = s.replace('\'', '&apos;')
        s = s.replace('<',  '&lt;')
        s = s.replace('>',  '&gt;')
    elif type(s) == unicode:
        s = s.replace(u'&',  u'&amp;')
        s = s.replace(u'"',  u'&quot;')
        s = s.replace(u'\'', u'&apos;')
        s = s.replace(u'<',  u'&lt;')
        s = s.replace(u'>',  u'&gt;')
    return s

def convert(obj):
    """Routes the elements of an object to the right function to convert them based on their data type"""
    debug_notify('Inside convert(): obj=%s' % (str(obj)))
    if type(obj) in (int, float, str, unicode):
        return convert_kv('item', obj)
    if hasattr(obj, 'isoformat'):
        return convert_kv('item', obj.isoformat())
    if type(obj) == bool:
        return convert_bool('item', obj)
    if type(obj) == dict:
        return convert_dict(obj)
    if type(obj) in (list, set, tuple):
        return convert_list(obj)
    raise TypeError, 'Unsupported data type: %s (%s)' % (obj, type(obj).__name__)

def convert_dict(obj):
    """Converts a dict into an XML string."""
    debug_notify('Inside convert_dict(): obj=%s' % (str(obj)))
    output = []
    addline = output.append
    for k, v in obj.items():
        debug_notify('Looping inside convert_dict(): k=%s, v=%s, type(v)=%s' % (k, str(v), type(v)))
        try:
            if k.isdigit():
                k = 'n%s' % (k)
        except:
            if type(k) in (int, float):
                k = 'n%s' % (k)
        if type(v) in (int, float, str, unicode):
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
            raise TypeError, 'Unsupported data type: %s (%s)' % (v, type(v).__name__)
    return ''.join(output)

def convert_list(items):
    """Converts a list into an XML string."""
    debug_notify('Inside convert_list(): items=%s' % (str(items)))
    output = []
    addline = output.append
    for item in items:
        debug_notify('Looping inside convert_list(): item=%s, type(item)=%s' % (str(item), type(item)))
        if type(item) in (int, float, str, unicode):
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
            raise TypeError, 'Unsupported data type: %s (%s)' % (item, type(item).__name__)
    return ''.join(output)

def convert_kv(k, v):
    """Converts an int, float or string into an XML element"""
    debug_notify('Inside convert_kv(): k=%s, v=%s' % (k, str(v)))
    return '<%s type="%s">%s</%s>' % (k, type(v).__name__ if type(v).__name__ != 'unicode' else 'str', xml_escape(v), k)

def convert_bool(k, v):
    """Converts a boolean into an XML element"""
    debug_notify('Inside convert_bool(): k=%s, v=%s' % (k, str(v)))
    return '<%s type="bool">%s</%s>' % (k, str(v).lower(), k)

def dicttoxml(obj, root=True):
    """Converts a python object into XML"""
    debug_notify('Inside dict2xml(): obj=%s' % (str(obj)))
    output = []
    addline = output.append
    if root == True:
        addline('<?xml version="1.0" encoding="UTF-8" ?>')
        addline('<root>%s</root>' % (convert(obj)))
    else:
        addline(convert(obj))
    return ''.join(output)
