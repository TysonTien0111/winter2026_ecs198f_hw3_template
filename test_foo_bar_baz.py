import pytest
from foo_bar_baz import foo_bar_baz

def testBaseCases():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"
    assert foo_bar_baz(4) == "1 2 Foo 4" 
    assert foo_bar_baz(7) == "1 2 Foo 4 Bar Foo 7"

def testFooAndBar():
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"
    assert foo_bar_baz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"

def testBaz():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    expected_30 = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    assert foo_bar_baz(30) == expected_30

def testEdgeCases():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-10) == ""

def testStrictFormatting():
    result = foo_bar_baz(15)
    assert result == result.strip()
    assert "  " not in result
