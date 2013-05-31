## dicttoxml

### Summary

Converts a Python dictionary or other native data type into a valid XML string. 

### Details

Supports item (`int`, `float`, `bool`, `str`, `unicode`, `datetime`, `none`) and collection (`list`, `set`, `tuple` and `dict`) data types with arbitrary nesting for the collections. Items with a `datetime` type are converted to ISO format strings. Items with a `none` type become empty XML elements.

The root object passed into the `dicttoxml` method can be any of the supported data types.

To satisfy XML syntax, the method prepends an `<?xml version="1.0" encoding="UTF-8" ?>` element and wraps the output in a `<root> ... </root>` element. However, this can be disabled to create XML snippets.

For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

Each element includes a `type` attribute with the data type. Note: `datetime` data types are converted into ISO format strings, and `unicode` and `datetime` data types get a `str` attribute.

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

**This module should work in Python 2.6+ and Python 3.**

### Installation

The dicttoxml module is [published on the Python Package Index](https://pypi.python.org/pypi/dicttoxml), so you can install it using `pip` or `easy_install`.

    pip install dicttoxml
    
Or:

    easy_install dicttoxml

Alternately, you can download the tarballed installer - `dicttoxml-[VERSION].tar.gz` - for this package from the [dist](https://github.com/quandyfactory/dicttoxml/tree/master/dist) directory on github and uncompress it. Then, from a terminal or command window, navigate into the unzipped folder and type the command:

    python setup.py install
    
That should be all you need to do.

### Basic Usage

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
    >>> print(obj)
    {u'mylist': [u'foo', u'bar', u'baz'], u'mydict': {u'foo': u'bar', u'baz': 1}, u'ok': True}
    >>> xml = dicttoxml.dicttoxml(obj)
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><root><mylist><item type="str">foo</item><item type="str">bar</item><item type="str">baz</item></mylist><mydict><foo type="str">bar</foo><baz type="int">1</baz></mydict><ok type="bool">true</ok></root>

It's that simple.

#### XML Snippet

You can also create an XML snippet for inclusion into another XML document, rather than a full XML document itself.

Continuing with the example from above:

    >>> xml_snippet = dicttoxml.dicttoxml(obj, root=False)
    >>> print(xml_snippet)
    <mylist><item type="str">foo</item><item type="str">bar</item><item type="str">baz</item></mylist><mydict><foo type="str">bar</foo><baz type="int">1</baz></mydict><ok type="bool">true</ok>

With the optional `root` argument set to `False`, the method converts the dict into XML without including an `<?xml>` prolog or a `<root>` element to enclose all the other elements.

### Pretty-Printing

As they say, Python comes with batteries included. You can easily syntax-check and pretty-print your XML using Python's `xml.dom.minidom` module. 

Again, continuing with our example:

    >>> from xml.dom.minidom import parseString
    >>> dom = parseString(xml)
    >>> print(dom.toprettyxml())
    <?xml version="1.0" ?>
    <root>
        <mylist type="list">
            <item type="str">foo</item>
            <item type="str">bar</item>
            <item type="str">baz</item>
        </mylist>
        <mydict type="dict">
            <foo type="str">bar</foo>
            <baz type="int">1</baz>
        </mydict>
        <ok type="bool">true</ok>
    </root>

This makes the XML easier to read. If it is not well-formed, the xml parser will raise an exception.

### Unique ID Attributes

Starting in version 1.1, you can set an optional `ids` parameter so that dicttoxml gives each element a unique `id` attribute. 

With the `ids` flag on, the function generates a unique randomly-generated ID for each element based on the parent element in the form `parent_unique`. For list items, the id is in the form `parent_unique_index`.

Continuing with our example:

    >>> xml_with_ids = dicttoxml.dicttoxml(obj, ids=True)
    >>> print(parseString(xml_with_ids).toprettyxml())
    <?xml version="1.0" ?>
    <root>
            <mylist id="root_160980" type="list">
                    <item id="mylist_609405_1" type="str">foo</item>
                    <item id="mylist_609405_2" type="str">bar</item>
                    <item id="mylist_609405_3" type="str">baz</item>
            </mylist>
            <mydict id="root_140407" type="dict">
                    <foo id="mydict_260437" type="str">bar</foo>
                    <baz id="mydict_111194" type="int">1</baz>
            </mydict>
            <ok id="root_612831" type="bool">true</ok>
    </root>

Note that the default XML output remains the same as previous, so as not to break compatibility for existing uses.

#### Debugging

You can also enable debugging information.

    >>> import dicttoxml
    >>> dicttoxml.set_debug()
    Debug mode is on. Events are logged at: dicttoxml.log
    >>> xml = dicttoxml.dicttoxml(some_dict)

By default, debugging information is logged to `dicttoxml.log`, but you can change this:

    >>> dicttoxml.set_debug(filename='some_other_filename.log')
    Debug mode is on. Events are logged at: some_other_filename.log

To turn debug mode off, just call `set_debug` with an argument of `False`:

    >>> dicttoxml.set_debug(False)
    Debug mode is off.

If you encounter any errors in the code, please file an issue: <https://github.com/quandyfactory/dicttoxml/issues>

### Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/dicttoxml](http://github.com/quandyfactory/dicttoxml)

### Version

* Version: 1.1.2
* Release Date: 2013-05-30

### Revision History

#### Version 1.1.1

* Release Date: 2013-05-06
* Changes:
    * Renamed github repo from dict2xml to dicttoxml to match PyPI name.

#### Version 1.1.1

* Release Date: 2013-05-06
* Changes:
    * Fixed README.markdown

#### Version 1.1

* Release Date: 2013-05-06
* Changes:
    * Added an optional `ids` argument to give each element a unique, randomly generated id attribute.
    * All elements now inlcude a `type` attribute.
    * Updated readme with more examples and Python 3 compatible syntax.
    * Thanks to [cpetz](https://github.com/cpetz) for [suggesting](https://github.com/quandyfactory/dicttoxml/issues/7) this feature.

#### Verson 1.0

* Release Date: 2013-03-04
* Changes:
    * Replaced debug function with `logging` module.
    * Converted code to work in Python 2.6+ and Python 3.
    * Fixed unresolved isoformat reference in `convert_list`.
    * Bug thanks to [regisd](https://github.com/regisd) for forking code and making several important fixes!

#### Version 0.9.1

* Release Date: 2013-03-03
* Changes:
    * Merged [pull request](https://github.com/quandyfactory/dicttoxml/pull/5) from [regisd](https://github.com/regisd) to fix [issue #5](https://github.com/quandyfactory/dicttoxml/issues/5), in which special XML characters were not being escaped properly.

#### Version 0.9

* Release Date: 2013-02-27
* Changes:
    * Added support for tuples.


#### Version 0.8

* Release Date: 2013-02-23
* Changes:
    * Changed name to dicttoxml and published to the Python Package Index (PyPI).

#### Version 0.7

* Release Date: 2012-09-12
* Changes:
    * Fixed [issue #4](https://github.com/quandyfactory/dicttoxml/issues/4) - thanks to PaulMdx for finding it and suggesting a fix.

#### Version 0.6

* Release Date: 2012-07-13
* Changes: 
    * Merged pull request from [0902horn](https://github.com/0902horn/dicttoxml) on github to escape special XML characters.

#### Version 0.5

* Release Date: 2012-02-28
* Changes: 
    * Added support for datetime objects (converts them into ISO format strings) and sets (converts them into lists).
    * Fixed [bug 2](https://github.com/quandyfactory/dicttoxml/issues/2) by raising an exception on unsupported data types.

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

