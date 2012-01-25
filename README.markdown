## dict2xml

### Summary

Converts a native Python dictionary into an XML string. 

### Details

* Supports item (int, float, bool, str, unicode) and collection (list and dict) data types with arbitrary nesting for the collections.

* Currently requires that the root object passed into the `dict2xml` function is a dict. In a later version, I'll probably revisit this to make it more generic (e.g. you can pass in a list or other data type).

* To satisfy XML syntax, it wraps all the dict keys/elements and values in a `<root> ... </root>` element.

* For lists of items, if each item is also a collection data type (lists, dict), the elements of that item are wrapped in a generic `<item> ... </item>` element.

* Item elements include an attribute with the data type (bool, int, float, string).

### Installation

Download the installation file `dict2xml-[version].tar.gz` and unzip it. Then, from a terminal or command window, type the command:

    python setup.py install
    
That should be all you need to do.

### Usage

Once installed, import the library into your script:

    import dict2xml

Convert a dict into xml by running the `dict2xml` function:

    xml = dict2xml.dict2xml(some_dict)

That's it!

### Author

* Author: Ryan McGreal
* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/dict2xml](http://github.com/quandyfactory/dict2xml)

### Version

* Version: 0.3
* Release Date: 2012-01-24

### Revision History

#### Version 0.2

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


