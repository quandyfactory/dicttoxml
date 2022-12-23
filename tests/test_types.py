import pytest

from dicttoxml import default_item_func
from dicttoxml import dicttoxml


parametized_root = pytest.mark.parametrize(
    "root",
    [
        pytest.param(True, id="With root"),
        pytest.param(False, id="Without root"),
    ],
)

parametized_custom_root = pytest.mark.parametrize(
    "custom_root",
    [
        pytest.param("root", id="Default root"),
        pytest.param("a custom root", id="Custom root"),
    ],
)

parametized_xml_decl = pytest.mark.parametrize(
    "xml_declaration",
    [
        pytest.param(True, id="With XML declaration"),
        pytest.param(False, id="Without XML declaration"),
    ],
)

parametized_ids = pytest.mark.parametrize(
    "ids",
    [
        pytest.param(True, id="With unique IDs"),
        pytest.param(False, id="Without unique IDs"),
    ],
)

parametized_attr_type = pytest.mark.parametrize(
    "attr_type",
    [
        pytest.param(True, id="With attribute types"),
        pytest.param(False, id="Without attribute types"),
    ],
)

def custom_item_func(parent):
    """This function is the same as dicttoxml.default_item_func."""
    return 'item'

parametized_item_func = pytest.mark.parametrize(
    "item_func",
    [
        pytest.param(default_item_func, id="With default item func"),
        pytest.param(custom_item_func, id="Without custom item func"),
    ],
)

parametized_cdata = pytest.mark.parametrize(
    "cdata",
    [
        pytest.param(True, id="With CDATA sections"),
        pytest.param(False, id="Without CDATA sections"),
    ],
)

parametized_include_encoding = pytest.mark.parametrize(
    "include_encoding",
    [
        pytest.param(True, id="With include encoding"),
        pytest.param(False, id="Without include encoding"),
    ],
)

parametized_encoding = pytest.mark.parametrize(
    "encoding",
    [
        pytest.param("UTF-8", id="UTF-8 encoding"),
        pytest.param("Latin-1", id="Latin1 encoding"),
    ],
)

parametized_return_bytes = pytest.mark.parametrize(
    "return_bytes",
    [
        pytest.param(True, id="With return bytes"),
        pytest.param(False, id="Without return bytes"),
    ],
)


def _check_dicttoxml(
    data,
    type_str,
    value_str,
    root,
    custom_root,
    xml_declaration,
    ids,
    attr_type,
    item_func,
    cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    # Call the tested function
    res = dicttoxml(
        data,
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,
        attr_type=attr_type,
        item_func=item_func,
        cdata=cdata,
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )

    # Build expected result
    if cdata == True:
        a_xml = "<![CDATA[%s]]>" % value_str
    else:
        a_xml = "%s" % value_str

    div = "a"

    if attr_type == True:
        a_xml = '<%s type="%s">%s</%s>' % (div, type_str, a_xml, div)
    else:
        a_xml = "<%s>%s</%s>" % (div, a_xml, div)

    expected = ""
    if root == True:
        if xml_declaration == True:
            if include_encoding == False:
                expected += '<?xml version="1.0" ?>'
            else:
                expected += '<?xml version="1.0" encoding="%s" ?>' % (encoding, )
        expected += "<%s>%s</%s>" % (custom_root, a_xml, custom_root)
    else:
        expected += a_xml

    if return_bytes:
        assert res == expected.encode("UTF-8")
    else:
        assert res == expected


@parametized_root
@parametized_custom_root
@parametized_xml_decl
@parametized_attr_type
@parametized_item_func
@parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_str(
    root,
    custom_root,
    xml_declaration,
    attr_type,
    item_func,
    cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": "string"}

    _check_dicttoxml(
        a,
        "str",
        "string",
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not relevant for str
        attr_type=attr_type,
        item_func=item_func,
        cdata=cdata,
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )


@parametized_root
@parametized_custom_root
@parametized_xml_decl
@parametized_attr_type
@parametized_item_func
@parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_int(
    root,
    custom_root,
    xml_declaration,
    attr_type,
    item_func,
    cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": 1}

    _check_dicttoxml(
        a,
        "int",
        "1",
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not relevant for str
        attr_type=attr_type,
        item_func=item_func,
        cdata=cdata,
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )


@parametized_root
@parametized_custom_root
@parametized_xml_decl
@parametized_attr_type
@parametized_item_func
@parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_float(
    root,
    custom_root,
    xml_declaration,
    attr_type,
    item_func,
    cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": 1.2}

    _check_dicttoxml(
        a,
        "float",
        "1.2",
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not relevant for str
        attr_type=attr_type,
        item_func=item_func,
        cdata=cdata,
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )


@parametized_root
@parametized_custom_root
@parametized_xml_decl
# @parametized_ids
@parametized_attr_type
@parametized_item_func
# @parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_list(
    root,
    custom_root,
    xml_declaration,
    # ids,
    attr_type,
    item_func,
    # cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": [1, 2]}

    if attr_type == True:
        expected = '<item type="int">1</item><item type="int">2</item>'
    else:
        expected = "<item>1</item><item>2</item>"

    _check_dicttoxml(
        a,
        "list",
        expected,
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not tested for now
        attr_type=attr_type,
        item_func=item_func,
        cdata=False,  # Not tested for now
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )


@parametized_root
@parametized_custom_root
@parametized_xml_decl
# @parametized_ids
@parametized_attr_type
@parametized_item_func
# @parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_tuple(
    root,
    custom_root,
    xml_declaration,
    # ids,
    attr_type,
    item_func,
    # cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": (1, 2)}

    if attr_type == True:
        expected = '<item type="int">1</item><item type="int">2</item>'
    else:
        expected = "<item>1</item><item>2</item>"

    _check_dicttoxml(
        a,
        "list",
        expected,
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not tested for now
        attr_type=attr_type,
        item_func=item_func,
        cdata=False,  # Not tested for now
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )


@parametized_root
@parametized_custom_root
@parametized_xml_decl
# @parametized_ids
@parametized_attr_type
@parametized_item_func
# @parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_dict(
    root,
    custom_root,
    xml_declaration,
    # ids,
    attr_type,
    item_func,
    # cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": {"b": 1}}

    if attr_type == True:
        expected = '<b type="int">1</b>'
    else:
        expected = "<b>1</b>"

    _check_dicttoxml(
        a,
        "dict",
        expected,
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not tested for now
        attr_type=attr_type,
        item_func=item_func,
        cdata=False,  # Not tested for now
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )


@parametized_root
@parametized_custom_root
@parametized_xml_decl
# @parametized_ids
@parametized_attr_type
@parametized_item_func
# @parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_nested_dict_tuple(
    root,
    custom_root,
    xml_declaration,
    # ids,
    attr_type,
    item_func,
    # cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": {"b": (1, 2)}}

    if attr_type == True:
        expected = '<b type="list"><item type="int">1</item><item type="int">2</item></b>'
    else:
        expected = "<b><item>1</item><item>2</item></b>"

    _check_dicttoxml(
        a,
        "dict",
        expected,
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not tested for now
        attr_type=attr_type,
        item_func=item_func,
        cdata=False,  # Not tested for now
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )


@parametized_root
@parametized_custom_root
@parametized_xml_decl
# @parametized_ids
@parametized_attr_type
@parametized_item_func
# @parametized_cdata
@parametized_include_encoding
@parametized_encoding
@parametized_return_bytes
def test_nested_tuple_tuple(
    root,
    custom_root,
    xml_declaration,
    # ids,
    attr_type,
    item_func,
    # cdata,
    include_encoding,
    encoding,
    return_bytes,
):
    a = {"a": (1, 2, (3, 4))}

    if attr_type == True:
        expected = '<item type="int">1</item><item type="int">2</item><item type="list"><item type="int">3</item><item type="int">4</item></item>'
    else:
        expected = "<item>1</item><item>2</item><item><item>3</item><item>4</item></item>"

    _check_dicttoxml(
        a,
        "list",
        expected,
        root=root,
        custom_root=custom_root,
        xml_declaration=xml_declaration,
        ids=False,  # Not tested for now
        attr_type=attr_type,
        item_func=item_func,
        cdata=False,  # Not tested for now
        include_encoding=include_encoding,
        encoding=encoding,
        return_bytes=return_bytes,
    )
