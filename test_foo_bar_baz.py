import pytest
from foo_bar_baz import foo_bar_baz

def testBasicSequence():
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(15) == expected

    expected = "1 2"
    assert foo_bar_baz(2) == expected

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
    thirdElement = result.split()[2]
    assert thirdElement == expectedEnd

    result = foo_bar_baz(n)
    fifthElement = result.split()[4]
    assert fifthElement == expectedEnd

    result = foo_bar_baz(n)
    fifthteenthElement = result.split()[14]
    assert fifthteenthElement == expectedEnd

    result = foo_bar_baz(n)
    lastElement = result.split()[-1]
    assert lastElement == expectedEnd

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
        foo_bar_baz(True)

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
