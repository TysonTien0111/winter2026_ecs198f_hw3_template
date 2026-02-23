from foo_bar_baz import foo_bar_baz
import pytest

def testBaseCases():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"

def testFooAndBar():
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

def testBaz():
    expected_output = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(15) == expected_output

def testEdgeCases():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-10) == ""
