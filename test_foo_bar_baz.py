import pytest
from foo_bar_baz import foo_bar_baz

def testBasicSequence():
    expected = "1 2"
    assert foo_bar_baz(2) == expected

    expected "1 2 Foo 4"
    assert foo_bar_baz(4) == expected

    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar"
    assert foo_bar_baz(10) == expected

    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(15) == expected

def testSingleValues():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

@pytest.mark.parametrize("n, expectedSequence", [
    (3, "1 2 Foo"),
    (5, "1 2 Foo 4 Bar"),
    (15, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"),
    (30, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz")
])

def testDivisibilityRules(n, expectedSequence):
    assert foo_bar_baz(n) == expectedSequence

def testFormatting():
    n = 1000000
    result = foo_bar_baz(n)
    assert result.count(" ") == n - 1
    assert result == result.strip()

    n = 0
    result = foo_bar_baz(n)
    assert result.count(" ") == 0
    assert result == result.strip()

    n = -5
    result = foo_bar_baz(n)
    assert result.count(" ") == 0
    assert result == result.strip()

def testEdgeCaseZeroOrNegative():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-5) == ""

def testTypeError():
    with pytest.raises(TypeError):
        foo_bar_baz(0.5)

    with pytest.raises(TypeError):
        foo_bar_baz(None)

    with pytest.raises(TypeError):
        foo_bar_baz("5")

    with pytest.raises(TypeError):
        foo_bar_baz("abc")

    with pytest.raises(TypeError):
        foo_bar_baz("12.5")

    with pytest.raises(TypeError):
        foo_bar_baz("abc", 12)

    with pytest.raises(TypeError):
        foo_bar_baz(12, "abc")
