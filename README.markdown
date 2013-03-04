## dicttoxml

### Summary

Converts a Python dictionary or other simple data type into a valid XML string. 

### Details

* Supports item (`int`, `float`, `bool`, `str`, `unicode`, `datetime`, `none`) and collection (`list`, `set`, `tuple` and `dict`) data types with arbitrary nesting for the collections. Items with a `datetime` type are converted to ISO format strings. Items with a `none` type become empty XML elements.

* The root object passed into the `dicttoxml` function can be any of the supported data types.

* To satisfy XML syntax, the method wraps all the dict keys/elements and values in a `<root> ... </root>` element. However, this can be disabled to create XML snippets.

* For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

* Elements with an item data type (`int`, `float`, `bool`, `str`, `datetime`, `unicode`) include a `type` attribute with the data type. Note: `datetime` data types are converted into ISO format strings, and `unicode` and `datetime` data types get a `str` attribute.

* Elements with an unsupported data type raise a TypeError exception.

### Installation

The dicttoxml module is [published on the Python Package Index](https://pypi.python.org/pypi/dicttoxml), so you can install it using `pip` or `easy_install`.

    pip install dicttoxml
    
Or:

    easy_install dicttoxml

Alternately, you can download the tarballed installer - `dicttoxml-[VERSION].tar.gz` - for this package from the [dist](https://github.com/quandyfactory/dict2xml/tree/master/dist) directory on github and uncompress it. Then, from a terminal or command window, navigate into the unzipped folder and type the command:

    python setup.py install
    
That should be all you need to do.

### Usage

Once installed, import the library into your script and convert a dict into xml by running the `dicttoxml` function:

    >>> import dicttoxml
    >>> xml = dicttoxml.dicttoxml(some_dict)

Alternately, you can import the `dicttoxml()` function from the library.

    >>> from dicttoxml import dicttoxml
    >>> xml = dicttoxml(some_dict)

That's it!

### Examples

#### JSON to XML

Let's say you want to fetch a JSON object from a URL and convert it into XML. Here's how you can do that:

    >>> import json
    >>> import urllib
    >>> import dicttoxml
    >>> page = urllib.urlopen('http://quandyfactory.com/api/example')
    >>> content = page.read()
    >>> obj = json.loads(content)
    >>> print obj
    {u'mylist': [u'foo', u'bar', u'baz'], u'mydict': {u'foo': u'bar', u'baz': 1}, u'ok': True}
    >>> xml = dicttoxml.dicttoxml(obj)
    >>> print xml
    <?xml version="1.0" encoding="UTF-8" ?><root><mylist><item type="str">foo</item><item type="str">bar</item><item type="str">baz</item></mylist><mydict><foo type="str">bar</foo><baz type="int">1</baz></mydict><ok type="bool">true</ok></root>

It's that simple.

#### XML Snippet

You can also create an XML snippet for inclusion into another XML document, rather than a full XML document itself.

Continuing with the example from above:

    >>> xml_snippet = dicttoxml.dicttoxml(obj, root=False)
    >>> print xml_snippet
    <mylist><item type="str">foo</item><item type="str">bar</item><item type="str">baz</item></mylist><mydict><foo type="str">bar</foo><baz type="int">1</baz></mydict><ok type="bool">true</ok>

With the optional `root` argument set to `False`, the method converts the dict into XML without including an `<?xml>` prolog or a `<root>` element to enclose all the other elements.

#### Debugging

You can also enable debugging information.

    >>> import dicttoxml
    >>> dicttoxml.debug = True # the console will print debug information for each function as it executes.  
    
    >>> xml = dicttoxml.dicttoxml(some_dict)

If you encounter any errors in the code, please file an issue: <https://github.com/quandyfactory/dict2xml/issues>

### Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/dict2xml](http://github.com/quandyfactory/dicttoxml)

### Version

* Version: 0.9.1
* Release Date: 2013-03-03

### Revision History

### Version 0.9.1

* Release Date: 2013-03-03
* Changes:
    * Merged [pull request](https://github.com/quandyfactory/dict2xml/pull/5) from [regisd](https://github.com/regisd) to fix [issue #5](https://github.com/quandyfactory/dict2xml/issues/5), in which special XML characters were not being escaped properly.

### Version 0.9

* Release Date: 2013-02-27
* Changes:
    * Added support for tuples.


### Version 0.8

* Release Date: 2013-02-23
* Changes:
    * Changed name to dicttoxml and published to the Python Package Index (PyPI).

### Version 0.7

* Release Date: 2012-09-12
* Changes:
    * Fixed [issue #4](https://github.com/quandyfactory/dict2xml/issues/4) - thanks to PaulMdx for finding it and suggesting a fix.

#### Version 0.6

* Release Date: 2012-07-13
* Changes: 
    * Merged pull request from [0902horn](https://github.com/0902horn/dict2xml) on github to escape special XML characters.

#### Version 0.5

* Release Date: 2012-02-28
* Changes: 
    * Added support for datetime objects (converts them into ISO format strings) and sets (converts them into lists).
    * Fixed [bug 2](https://github.com/quandyfactory/dict2xml/issues/2) by raising an exception on unsupported data types.

#### Version 0.4

* Release Date: 2012-01-26
* Changes: 
    * Added optional `root` argument (default `True`) on whether to wrap the generated XML in an XML declaration and a root element.
    * Added ability to convert a root object of other data types - int, float, str, unicode, list - as well as dict.
    * Corrected `license` attribute in `setup.py`.
    * Renamed `notify()` function to `debug_notify()` and made it more comprehensive.

#### Version 0.3

* Release Date: 2012-01-24
* Changes: 
    * Fixed inconsistent str/string attributes.

#### Version 0.2

* Release Date: 2012-01-24
* Changes: 
    * Fixed bug in list items.
    * Added element attribute with data type.

#### Version 0.1

* Release Date: 2012-01-24
* Changes: 
    * First commit.

### Copyright and Licence

Copyright 2012 by Ryan McGreal. 

Released under the GNU General Public Licence, Version 2:  
<http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>

