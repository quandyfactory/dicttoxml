## dict2xml

### Summary

Converts a native Python dictionary into an XML string. 

### Details

* Supports item (`int`, `float`, `bool`, `str`, `unicode`, `datetime`) and collection (`list`, `set` and `dict`) data types with arbitrary nesting for the collections. Datetime objects are converted to ISO format strings.

* The root object passed into the `dict2xml` function can be any of the following data types: `int`, `float`, `str`, `unicode`, `datetime`, `list`, `set`, `dict`.

* To satisfy XML syntax, by default it wraps all the dict keys/elements and values in a `<root> ... </root>` element. However, this can be disabled to create XML snippets.

* For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

* Elements with an item data type (`int`, `float`, `bool`, `str`, `datetime`, `unicode`) include a `type` attribute with the data type. Note: `datetime` data types are converted into ISO format strings, and `unicode` and `datetime` data types get a `str` attribute.

* Elements with an unsupported data type raise a TypeError exception.

### Installation

Download the tarballed installer - `dict2xml-[VERSION].tar.gz` - for this package from the [dist](https://github.com/quandyfactory/dict2xml/tree/master/dist) directory and uncompress it. Then, from a terminal or command window, navigate into the unzipped folder and type the command:

    python setup.py install
    
That should be all you need to do.

### Usage

Once installed, import the library into your script and convert a dict into xml by running the `dict2xml` function:

    >>> import dict2xml
    >>> xml = dict2xml.dict2xml(some_dict)

Alternately, you can import the `dict2xml()` function from the library.

    >>> from dict2xml import dict2xml
    >>> xml = dict2xml(some_object)

That's it!

#### Debugging

You can also enable debugging information.

    >>> import dict2xml
    >>> dict2xml.debug = True # the console will print debug information for each function as it executes.  
    
    >>> xml = dict2xml.dict2xml(some_object)

If you encounter any errors in the code, please file an issue: <https://github.com/quandyfactory/dict2xml/issues>

### Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/dict2xml](http://github.com/quandyfactory/dict2xml)

### Version

* Version: 0.7
* Release Date: 2012-09-12

### Revision History

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

