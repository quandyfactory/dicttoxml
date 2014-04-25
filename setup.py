from distutils.core import setup

version = '1.3.6'

setup(
    name = 'dicttoxml',
    version = version,
    description = 'Converts a Python dictionary or other native data type into a valid XML string. ',
    long_description = """Supports item (`int`, `float`, `bool`, `str`, `unicode`, `datetime`, `none`) and  collection (`list`, `set`, `tuple` and `dict`, as well as iterable and dict-like objects) data types with arbitrary nesting for the collections. Items with a `datetime` type are converted to ISO format strings. Items with a `none` type become empty XML elements.

The root object passed into the `dicttoxml` function can be any of the supported data types.

To satisfy XML syntax, the method wraps all the dict keys/elements and values in a `<root> ... </root>` element. However, this can be disabled to create XML snippets.

For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

Each elements includes a `type` attribute with the data type. Note: `datetime` data types are converted into ISO format strings, and `unicode` and `datetime` data types get a `str` attribute.

    Python -> XML
    integer   int
    float     float
    string    str
    unicode   str
    datetime  str
    None      null
    boolean   bool
    list      list
    set       list
    tuple     list
    dict      dict

Elements with an unsupported data type raise a TypeError exception. 

If an element name is invalid XML, it is rendered with the name "key" and the invalid name is included as a `name` attribute. E.g. `{ "^.{0,256}$": "foo" }` would be rendered `<key name="^.{0,256}$">foo</key>`. An exception is element names with spaces, which are converted to underscores.

**This module should work in Python 2.6+ and Python 3.**
    """,
    author = 'Ryan McGreal',
    author_email = 'ryan@quandyfactory.com',
    license = 'GNU General Public Licence, Version 2',
    url = 'https://github.com/quandyfactory/dicttoxml',
    py_modules = ['dicttoxml'],
    download_url = 'https://github.com/quandyfactory/dicttoxml/blob/master/dist/dicttoxml-%s.tar.gz?raw=true' % (version),
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3'
  ],
)
