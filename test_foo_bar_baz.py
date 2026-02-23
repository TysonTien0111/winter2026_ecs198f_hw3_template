import pytest
from foo_bar_baz import foo_bar_baz

def testBasicSequence():
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(15) == expected

def testSingleValues():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

@pytest.mark.parametrize("n, expectedEnd", [
    (3, "Foo"),
    (5, "Bar"),
    (15, "Baz"),
    (30, "Baz"),
])

def testDivisibilityRules(n, expectedEnd):
    result = foo_bar_baz(n)
    lastElement = result.split()[-1]
    assert lastElement == expectedEnd

def testFormatting():
    n = 1000000
    result = foo_bar_baz(n)
    assert result.count(" ") == n - 1
    assert result == result.strip()

def testEdgeCaseZeroOrNegative():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-5) == ""
