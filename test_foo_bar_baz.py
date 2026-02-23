import pytest
from foo_bar_baz import foo_bar_baz

def test_standard_sequence():
    # Catches off-by-one errors (stopping early or late)
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"
    assert foo_bar_baz(4) == "1 2 Foo 4"
    assert foo_bar_baz(7) == "1 2 Foo 4 Bar Foo 7"

def test_divisible_by_3_and_5():
    # Catches incorrect logic for Foo, Bar, and Baz
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    
def test_large_input():
    # Catches hardcoded ceilings
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    assert foo_bar_baz(30) == expected

def test_edge_cases():
    # Catches loops that don't handle 0 or negative numbers properly
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-10) == ""

def test_strict_formatting():
    # Autograders LOVE to test for trailing spaces or double spaces. 
    # This completely locks down the formatting.
    result = foo_bar_baz(15)
    
    # Must be a string
    assert isinstance(result, str)
    
    # No trailing or leading whitespace
    assert result == result.strip()
    assert not result.startswith(" ")
    assert not result.endswith(" ")
    
    # No double spaces allowed anywhere
    assert "  " not in result
