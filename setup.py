from distutils.core import setup

version = '0.4'

setup(
    name = 'dict2xml',
    version = version,
    description = 'Converts a native Python dictionary into an XML string.',
    long_description = """ * Supports item (`int`, `float`, `bool`, `str`, `unicode`) and collection (`list` and `dict`) data types with arbitrary nesting for the collections.

* The root object passed into the `dict2xml` function can be any of the following data types: `int`, `float`, `str`, `unicode`, `list`, `dict`.

* To satisfy XML syntax, by default it wraps all the dict keys/elements and values in a `<root> ... </root>` element. However, this can be disabled to create XML snippets.

* For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

* Elements with an item data type (`int`, `float`, `bool`, `str`, `unicode`) include a `type` attribute with the data type. Note: `unicode` data types get a `str` attribute.    
    """,
    author = 'Ryan McGreal',
    author_email = 'ryan@quandyfactory.com',
    license = 'GNU General Public Licence, Version 2',
    url = 'https://github.com/quandyfactory/dict2xml',
    py_modules = ['dict2xml'],
    download_url = 'https://github.com/quandyfactory/dict2xml/blob/master/dist/dict2xml-%s.tar.gz?raw=true' % (version),
)
