Summary
=======

Converts a Python dictionary or other native data type into a valid XML string. 

Details
=======

Supports item (`int`, `float`, `long`, `decimal.Decimal`, `bool`, `str`, `unicode`, `datetime`, `none` and other number-like objects) and collection (`list`, `set`, `tuple` and `dict`, as well as iterable and dict-like objects) data types, with arbitrary nesting for the collections. Items with a `datetime` type are converted to ISO format strings. Items with a `None` type become empty XML elements.

The root object passed into the `dicttoxml` method can be any of the supported data types.

To satisfy XML syntax, the method prepends an `<?xml version="1.0" encoding="UTF-8" ?>` element and wraps the output in a `<root> ... </root>` element. However, this can be disabled to create XML snippets. Alternately, a custom root element can be specified by passing in the optional `custom_root=foobar` argument.

For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

Each element includes an optional `type` attribute with the data type. By default, the type attribute it included but it can be excluded by passing an optional `attr_type=False` argument when calling the `dicttoxml` method.

Note: `datetime` data types are converted into ISO format strings, and `unicode` and `datetime` data types get a `str` attribute.

    Python -> XML
    integer   int
    long      long
    float     float
    Decimal   number
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

Installation
============

The dicttoxml module is [published on the Python Package Index](https://pypi.python.org/pypi/dicttoxml), so you can install it using `pip` or `easy_install`.

    pip install dicttoxml
    
Or:

    easy_install dicttoxml

Alternately, you can download the tarballed installer - `dicttoxml-[VERSION].tar.gz` - for this package from the [dist](https://github.com/quandyfactory/dicttoxml/tree/master/dist) directory on github and uncompress it. Then, from a terminal or command window, navigate into the unzipped folder and type the command:

    python setup.py install
    
That should be all you need to do.

Basic Usage
===========

Once installed, import the library into your script and convert a dict into xml by running the `dicttoxml` function:

    >>> import dicttoxml
    >>> xml = dicttoxml.dicttoxml(some_dict)

Alternately, you can import the `dicttoxml()` function from the library.

    >>> from dicttoxml import dicttoxml
    >>> xml = dicttoxml(some_dict)

That's it!

JSON to XML
===========

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

Disable Type Attributes
=======================

By default, dicttoxml includes a type attribute for each element. Starting in version 1.4, you can turn this off by passing an optional `attr_type=False` argument to the `dicttoxml` method. 

Using our example:

    >>> xml = dicttoxml.dicttoxml(obj, attr_type=False)
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><root><mydict><foo>bar</foo><baz>1</baz></mydict><mylist><item>foo</item><item>bar</item><item>baz</item></mylist><ok>true</ok></root>

As you can see, the only difference is that the type attributes are now absent.

Custom Root
===========

By default, dicttoxml wraps all the elements in a `<root> ... </root>` element. Starting in version 1.5, you can change the name of the root element to something else by passing an optional `custom_root=some_custom_root` argument to the `dicttoxml` method.

Using our example:

    >>> xml = dicttoxml.dicttoxml(obj, custom_root='some_custom_root')
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><some_custom_root><mydict><foo>bar</foo><baz>1</baz></mydict><mylist><item>foo</item><item>bar</item><item>baz</item></mylist><ok>true</ok></some_custom_root>

As you can see, the name of the root element has changed to `some_custom_root`.

XML Snippet
===========

You can also create an XML snippet for inclusion into another XML document, rather than a full XML document itself.

Continuing with the example from above:

    >>> xml_snippet = dicttoxml.dicttoxml(obj, root=False)
    >>> print(xml_snippet)
    <mylist><item type="str">foo</item><item type="str">bar</item><item type="str">baz</item></mylist><mydict><foo type="str">bar</foo><baz type="int">1</baz></mydict><ok type="bool">true</ok>

With the optional `root` argument set to `False`, the method converts the dict into XML without including an `<?xml>` prolog or a `<root>` element to enclose all the other elements.

Pretty-Printing
===============

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

Unique ID Attributes
====================

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

Dict-Like and Iterable Objects
==============================

Starting in version 1.3, dicttoxml accepts dict-like objects that are derived from the `dict` base class and treats them like dicts. For example:

    >>> import collections
    >>> dictlike = collections.OrderedDict({'foo': 1, 'bar': 2, 'baz': 3})
    >>> xml = dicttoxml.dicttoxml(dictlike)
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><root><baz type="int">3</baz><foo type="int">1</foo><bar type="int">2</bar></root>

Also starting in version 1.3, dicttoxml accepts iterable objects and treats them like lists. For example:

    >>> myiterator = xrange(1,11)
    >>> xml = dicttoxml.dicttoxml(myiterator)
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><root><item type="int">1</item><item type="int">2</item><item type="int">3</item><item type="int">4</item><item type="int">5</item><item type="int">6</item><item type="int">7</item><item type="int">8</item><item type="int">9</item><item type="int">10</item></root>

As always, this remains compatible with arbitrary nesting of objects and types.

Define Custom Item Names
========================

Starting in version 1.7, if you don't want item elements in a list to be called 'item', you can specify the element name using a function that takes the parent element name (i.e. the list name) as an argument.

    >>> import dicttoxml
    >>> obj = {u'mylist': [u'foo', u'bar', u'baz'], u'mydict': {u'foo': u'bar', u'baz': 1}, u'ok': True}
    >>> my_item_func = lambda x: 'list_item'
    >>> xml = dicttoxml.dicttoxml(obj, item_func=my_item_func)
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><root><mydict type="dict"><foo type="str">bar</foo><baz type="int">1</baz></mydict><mylist type="list"><list_item type="str">foo</list_item><list_item type="str">bar</list_item><list_item type="str">baz</list_item></mylist><ok type="bool">True</ok></root>

The benefit of taking the parent element name as an argument is that you can write the function to do something with it. Let's say you have an object with some lists of specific items:

    >>> obj = {'shrubs': ['abelia', 'aralia', 'aucuba', 'azalea', 'bamboo', 'barberry', 'bluebeard', 'boxwood', 'camellia', 'dogwood', 'elderberry', 'enkianthus', 'firethorn', 'fuchsia', 'hazel', 'heath', 'heather', 'holly', 'honeysuckle', 'hydrangea', 'laurel', 'lilac', 'mock orange', 'rhododendron', 'rose', 'rose of sharon', 'rosemary', 'smokebush', 'spirea', 'sweetbox', 'viburnum', 'weigela', 'yucca'], 'trees': ['ash', 'aspen', 'birch', 'butternut', 'cedar', 'cottonwood', 'elm', 'fir', 'hawthorn', 'larch', 'locust', 'maple', 'oak', 'pine', 'spruce', 'sycamore', 'willow']}

You can define each item name to be the singular of its parent name by returning all but the last character.

    >>> my_item_func = lambda x: x[:-1]
    >>> xml = dicttoxml.dicttoxml(obj, item_func=my_item_func)
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><root><shrubs type="list"><shrub type="str">abelia</shrub><shrub type="str">aralia</shrub><shrub type="str">aucuba</shrub><shrub type="str">azalea</shrub><shrub type="str">bamboo</shrub><shrub type="str">barberry</shrub><shrub type="str">bluebeard</shrub><shrub type="str">boxwood</shrub><shrub type="str">camellia</shrub><shrub type="str">dogwood</shrub><shrub type="str">elderberry</shrub><shrub type="str">enkianthus</shrub><shrub type="str">firethorn</shrub><shrub type="str">fuchsia</shrub><shrub type="str">hazel</shrub><shrub type="str">heath</shrub><shrub type="str">heather</shrub><shrub type="str">holly</shrub><shrub type="str">honeysuckle</shrub><shrub type="str">hydrangea</shrub><shrub type="str">laurel</shrub><shrub type="str">lilac</shrub><shrub type="str">mock orange</shrub><shrub type="str">rhododendron</shrub><shrub type="str">rose</shrub><shrub type="str">rose of sharon</shrub><shrub type="str">rosemary</shrub><shrub type="str">smokebush</shrub><shrub type="str">spirea</shrub><shrub type="str">sweetbox</shrub><shrub type="str">viburnum</shrub><shrub type="str">weigela</shrub><shrub type="str">yucca</shrub></shrubs><trees type="list"><tree type="str">ash</tree><tree type="str">aspen</tree><tree type="str">birch</tree><tree type="str">butternut</tree><tree type="str">cedar</tree><tree type="str">cottonwood</tree><tree type="str">elm</tree><tree type="str">fir</tree><tree type="str">hawthorn</tree><tree type="str">larch</tree><tree type="str">locust</tree><tree type="str">maple</tree><tree type="str">oak</tree><tree type="str">pine</tree><tree type="str">spruce</tree><tree type="str">sycamore</tree><tree type="str">willow</tree></trees></root>

Of course, this can be combined with other optional arguments, like disabling type attributes or custom root element names.

CDATA
=====

Starting in version 1.7.1, you can wrap values in CDATA by setting the optional `cdata` argument to `True`.

    >>> import dicttoxml
    >>> obj = {u'mylist': [u'foo', u'bar', u'baz'], u'mydict': {u'foo': u'bar', u'baz': 1}, u'ok': True}
    >>> xml = dicttoxml.dicttoxml(obj, cdata=True)
    >>> print(xml)
    <?xml version="1.0" encoding="UTF-8" ?><root><mydict type="dict"><foo type="str"><![CDATA[bar]]></foo><baz type="int"><![CDATA[1]]></baz></mydict><mylist type="list"><item type="str"><![CDATA[foo]]></item><item type="str"><![CDATA[bar]]></item><item type="str"><![CDATA[baz]]></item></mylist><ok type="bool"><![CDATA[True]]></ok></root>

If you do not set `cdata` to `True`, the default value is `False` and values are not wrapped.

Adding Custom Attributes
========================

You can add custom attributes to nodes by adding a child `dict` named `@attrs` to a parent `dict` like so:

```python3
my_dict = {
    "Family": {
        "@attrs": {
            "Tree": "Menelaws"
        },
        "Name": "Lewis Menelaws",
        "Occupation": "Programmer",
        "Programming Language": "Python"
    }
}
```
The key will be the name of the custom attribute while the value will be the value of that custom attribute.

Running a standard `dicttoxml` you will get a result like this:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<FamilyTree>
    <Family Tree="Menelaws">
        <Name>Lewis Menelaws</Name>
        <Occupation>Programmer</Occupation>
        <Programming_Language>Python</Programming_Language>
    </Family>
</FamilyTree>
```




Debugging
=========

You can enable debugging information.

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

If you encounter any errors in the code, please file an issue on github: [https://github.com/quandyfactory/dicttoxml/issues](https://github.com/quandyfactory/dicttoxml/issues).

Author
======

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/dicttoxml](http://github.com/quandyfactory/dicttoxml)

Version
=======

* Version: 1.7.5
* Release Date: 2022-06-06

Revision History
================

Version 1.7.5
-------------

* Release Date: 2022-06-06
* Changes:
    * Fixed [isue #91](https://github.com/quandyfactory/dicttoxml/issues/91) on github. 

Version 1.7.4
-------------

* Release Date: 2016-07-08
* Changes:
    * Fixed [bug #46](https://github.com/quandyfactory/dicttoxml/issues/46) on github. Thanks to [robbincatz](https://github.com/robbincatz) for identifying and reporting the issue.

Version 1.7.3
-------------

* Release Date: 2016-07-07
* Changes:
    * Updated README.markdown

Version 1.7.2
-------------

* Release Date: 2016-07-07
* Changes:
    * XML-encodes values to avoid XML injection. Big thanks to [thomaskonrad](https://github.com/thomaskonrad) on Github, via [issue #41](https://github.com/quandyfactory/dicttoxml/issues/41).

Version 1.7.1
-------------

* Release Date: 2016-07-06
* Changes:
    * Added ability to wrap values with CDATA. Big thanks to [LeviTaule](https://github.com/LeviTaule) on Github, via [pull request #45](https://github.com/quandyfactory/dicttoxml/pull/45/files).

Version 1.7
-----------

* Release Date: 2016-06-13
* Changes:
    * First of all, sorry for such a log delay between releases! I have not been a responsible steward of this project and I aim to change that from now on. This is the first in a series of updates I will be pushing over the next couple of months to get caught up on the backlog of issues and pull requests.
    * Added ability to customize `list` and `dict` item names via a function argument passed into the `dicttoxml()` function. Customizeable item name function takes the item's parent element as an argument. Big thanks to [viktor-zireael](https://github.com/viktor-zireael) on Github, via [pull request #40](https://github.com/quandyfactory/dicttoxml/pull/40/files).
    * Updated code style to more closely follow PEP8.

Version 1.6.6
-------------

* Release Date: 2015-04-09
* Changes:
    * PyPi does not want to upload version 1.6.5. It's returning an `Upload failed (500): Internal Server Error` message when I try to upload the code. I'm incrementing the version by one and reinstalling it to see if that fixes the issue.

Version 1.6.5
-------------

* Release Date: 2015-04-09
* Changes:
    * Fixed [issue #37](https://github.com/quandyfactory/dicttoxml/issues/37), elements with boolean values were getting a "number" type attribute. The issue was that `isinstance(True, numbers.Number)` returns `True`. I modified the `get_xml_type()` function to test for `boolean` before testing for `numbers.Number`. Thanks to [badsequel](https://github.com/badsequel) for identifying and reporting the issue.

Version 1.6.4
-------------

* Release Date: 2015-03-11
* Changes:
    * Fixed [issue #36](https://github.com/quandyfactory/dicttoxml/issues/36), logging was throwing an UnicodeDecodeError on non-ASCII characters in dictionary values. Thanks to [beef9999](https://github.com/beef9999) for identifying and reporting the issue.

Version 1.6.3
-------------

* Release Date: 2015-03-05
* Changes:
    * Updated README.markdown to reflect changes made in v. 1.6.2.

Version 1.6.2
-------------

* Release Date: 2015-03-05
* Changes:
    * Fixed [issue #35](https://github.com/quandyfactory/dicttoxml/issues/35), dicttoxml fails to identify a `decimal.Decimal` as a number. This is done by replacing `type(val).__name__ in ('int', 'long')` with the more generic `isinstance(val, number.Number)`. Thanks to [jmagnusson](https://github.com/jmagnusson) for finding and fixing the error.

Version 1.6.1
-------------

* Release Date: 2015-03-05
* Changes:
    * Merged [pull request #34](https://github.com/quandyfactory/dicttoxml/pull/34), fix misleading TypeError in `convert_dict()`. Thanks to [jmagnusson](https://github.com/jmagnusson) for finding and fixing the error.

Version 1.6.0
-------------

* Release Date: 2015-02-23
* Changes:
    * Fixed [issue #32](https://github.com/quandyfactory/dicttoxml/issues/32), duplication in test for list-like data types.

Version 1.5.9
-------------

* Release Date: 2015-02-23
* Changes:
    * Merged [pull request #33](https://github.com/quandyfactory/dicttoxml/pull/33) to replace invocations of `logging` with `LOG`. Thanks to [mfriedenhagen ](https://github.com/mfriedenhagen) for identifying the issue with the logger, and to [seyhuns](https://github.com/seyhuns) for supplying a pull request that could be merged automatically.

Version 1.5.8
-------------

* Release Date: 2015-01-06
* Changes:
    * Fixed [issue #30](https://github.com/quandyfactory/dicttoxml/issues/30) via [pull request #31](https://github.com/quandyfactory/dicttoxml/pull/31). Thanks to [isaac-councill](https://github.com/isaac-councill) for identifying the issue and providing a fix.

Version 1.5.7
-------------

* Release Date: 2014-12-09
* Changes:
    * Fixed [issue #29](https://github.com/quandyfactory/dicttoxml/issues/29). Thanks to [birdsarah](https://github.com/birdsarah) for identifying this performance issue and providing a fix.

Version 1.5.6
-------------

* Release Date: 2014-08-18
* Changes:
    * Fixed [issue #24](https://github.com/quandyfactory/dicttoxml/issues/24). Thanks to [gdude2002](https://github.com/gdude2002) for identifying the issue.
    * Abstracted all XML validity tests to a single function `make_valid_xml_name(key, attr)`

Version 1.5.5
-------------

* Release Date: 2014-06-16
* Changes:
    * Fixed [issue #21](https://github.com/quandyfactory/dicttoxml/pull/21). Thanks to [lichenbo](https://github.com/lichenbo) for identifying the issue and providing a fix.
    * Abstracted setting XML type attribute into a function, `get_xml_type()`.
    * Standardized variable names inside functions (e.g. `k` -> `key`, `v` -> `val`).
    * Cleaned up README so it works as both Markdown (for github) and ReStructuredText (for PyPi)

Version 1.5.4
-------------

* Release Date: 2014-06-03
* Changes:
    * Fixed [issue #20](https://github.com/quandyfactory/dicttoxml/issues/20).  Thanks to [lichenbo](https://github.com/lichenbo) for identifying the issue and providing a fix.

Version 1.5.3
-------------

* Release Date: 2014-06-08
* Changes:
    * Minor updates to README.markdown

Version 1.5.2
-------------

* Release Date: 2014-06-03
* Changes:
    * Minor updates to README.markdown

Version 1.5.1
-------------

* Release Date: 2014-06-03
* Changes:
    * Minor updates to README.markdown

Version 1.5
-----------

* Release Date: 2014-06-03
* Changes:
    * Added ability to set a custom root element, as per [issue #18](https://github.com/quandyfactory/dicttoxml/issues/18) by [murielsilveira](https://github.com/murielsilveira).

Version 1.4
-----------

* Release Date: 2014-06-03
* Changes:
    * Element type attribute made optional via pull request from [gauravub](https://github.com/gauravub] to resolve [issue #17](https://github.com/quandyfactory/dicttoxml/pull/17).

Version 1.3.7
-------------

* Release Date: 2014-04-21
* Changes:
    * Updated `MANIFEST.in` and `setup.py` so the licence and readme are properly included in the distribution.

Version 1.3.6
-------------

* Release Date: 2014-04-21
* Changes:
    * Added `MANIFEST.in` to include the `LICENCE.txt` and `README.markdown` files in the distribution, as per [issue #15](https://github.com/quandyfactory/dicttoxml/issues/15).

Version 1.3.5
-------------

* Release Date: 2014-04-14
* Changes:
    * `dicttoxml()` accepts `[None]` as a parameter and returns a valid XML object, as per [issue #13](https://github.com/quandyfactory/dicttoxml/issues/13).

Version 1.3.4
-------------

* Release Date: 2014-04-14
* Changes:
    * `dicttoxml()` now accepts `None` as a parameter and returns a valid XML object, as per [issue #13](https://github.com/quandyfactory/dicttoxml/issues/13).

Version 1.3.3
-------------

* Release Date: 2014-04-14
* Changes:
    * Automatically converts spaces in key names to underscores, as per [issue #12](https://github.com/quandyfactory/dicttoxml/pull/12).

Version 1.3.2
-------------

* Release Date: 2014-04-14
* Changes:
    * Added convert_none() function to convert a null value into XML
    * Added `key_is_valid_xml()` function to test if a key is valid XML
    * Updated `convert_kv()`, `convert_bool()` and `convert_none()` functions to test whether the key is a valid XML name and, if it is not, to render it as `<key name="{invalidname}">value</key>`. This addresses [issue 10](https://github.com/quandyfactory/dicttoxml/issues/10).

Version 1.3.1
-------------

* Release Date: 2013-07-12
* Changes:
    * Updated README to note support for dict-like and iterable objects.

Version 1.3
-----------

* Release Date: 2013-07-12
* Changes:
    * changed test for dict type from `type(x)=dict` to `isinstance(x,dict)` to include dict-like subclases derived from dict, as per [issue 9](https://github.com/quandyfactory/dicttoxml/issues/9).
    * Added test for `isinstance(x,collections.Iterable)` to test for list, set, tuple to accommodate iterable objects, as per [issue 9](https://github.com/quandyfactory/dicttoxml/issues/9).

Version 1.2
-----------

* Release Date: 2013-07-11
* Changes:
    * Fixed typo in convert_list() exception raise as per [issue 8](https://github.com/quandyfactory/dicttoxml/issues/8).

Version 1.1.2
-------------

* Release Date: 2013-05-06
* Changes:
    * Renamed github repo from dict2xml to dicttoxml to match PyPI name.

Version 1.1.1
-------------

* Release Date: 2013-05-06
* Changes:
    * Fixed README.markdown

Version 1.1
-----------

* Release Date: 2013-05-06
* Changes:
    * Added an optional `ids` argument to give each element a unique, randomly generated id attribute.
    * All elements now inlcude a `type` attribute.
    * Updated readme with more examples and Python 3 compatible syntax.
    * Thanks to [cpetz](https://github.com/cpetz) for [suggesting](https://github.com/quandyfactory/dicttoxml/issues/7) this feature.

Verson 1.0
----------

* Release Date: 2013-03-04
* Changes:
    * Replaced debug function with `logging` module.
    * Converted code to work in Python 2.6+ and Python 3.
    * Fixed unresolved isoformat reference in `convert_list`.
    * Bug thanks to [regisd](https://github.com/regisd) for forking code and making several important fixes!

Version 0.9.1
-------------

* Release Date: 2013-03-03
* Changes:
    * Merged [pull request](https://github.com/quandyfactory/dicttoxml/pull/5) from [regisd](https://github.com/regisd) to fix [issue #5](https://github.com/quandyfactory/dicttoxml/issues/5), in which special XML characters were not being escaped properly.

Version 0.9
-----------

* Release Date: 2013-02-27
* Changes:
    * Added support for tuples.

Version 0.8
-----------

* Release Date: 2013-02-23
* Changes:
    * Changed name to dicttoxml and published to the Python Package Index (PyPI).

Version 0.7
-----------

* Release Date: 2012-09-12
* Changes:
    * Fixed [issue #4](https://github.com/quandyfactory/dicttoxml/issues/4) - thanks to PaulMdx for finding it and suggesting a fix.

Version 0.6
-----------

* Release Date: 2012-07-13
* Changes: 
    * Merged pull request from [0902horn](https://github.com/0902horn/dicttoxml) on github to escape special XML characters.

Version 0.5
-----------

* Release Date: 2012-02-28
* Changes: 
    * Added support for datetime objects (converts them into ISO format strings) and sets (converts them into lists).
    * Fixed [bug 2](https://github.com/quandyfactory/dicttoxml/issues/2) by raising an exception on unsupported data types.

Version 0.4
-----------

* Release Date: 2012-01-26
* Changes: 
    * Added optional `root` argument (default `True`) on whether to wrap the generated XML in an XML declaration and a root element.
    * Added ability to convert a root object of other data types - int, float, str, unicode, list - as well as dict.
    * Corrected `license` attribute in `setup.py`.
    * Renamed `notify()` function to `debug_notify()` and made it more comprehensive.

Version 0.3
-----------

* Release Date: 2012-01-24
* Changes: 
    * Fixed inconsistent str/string attributes.

Version 0.2
-----------

* Release Date: 2012-01-24
* Changes: 
    * Fixed bug in list items.
    * Added element attribute with data type.

Version 0.1
-----------

* Release Date: 2012-01-24
* Changes: 
    * First commit.

Copyright and Licence
=====================

Copyright 2012 by Ryan McGreal. 

Released under the GNU General Public Licence, Version 2:  
<http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>

