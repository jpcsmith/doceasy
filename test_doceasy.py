"""Tests for doceasy."""
import schema
import pytest
from doceasy import Mapping


def test_mapping_str():
    """It should create a mapping of strings when provided no arguments."""
    assert Mapping().validate("a=b") == {"a": "b"}
    assert Mapping().validate("a=b,c=d") == {"a": "b", "c": "d"}


def test_mapping_with_single_type():
    """If provided a single type, it should convert the values to that
    type.
    """
    assert Mapping(int).validate("a=1") == {"a": 1}
    assert Mapping(int).validate("a=1,c=2") == {"a": 1, "c": 2}

    with pytest.raises(schema.SchemaError):
        Mapping(int).validate("a=b,c=d")


def test_mapping_with_two_types():
    """It should convert both the key and value."""
    assert Mapping(int, int).validate("1=2") == {1: 2}
    assert Mapping(int, int).validate("1=2,3=4") == {1: 2, 3: 4}


def test_mapping_to_string():
    """It should create a string of the dict."""
    assert Mapping.to_string({"a": 1, "b": 2}) == "a=1,b=2"
    assert Mapping(int).validate(Mapping.to_string({"a": 1, "b": 2})) == {
        "a": 1, "b": 2}
