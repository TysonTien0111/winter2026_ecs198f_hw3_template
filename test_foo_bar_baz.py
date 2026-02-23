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

def testTypeError():
    with pytest.raises(TypeError):
        foo_bar_baz(0.5)
        foo_bar_baz(True)
        foo_bar_baz(None)
        foo_bar_baz("5")
        foo_bar_baz("abc")
        foo_bar_baz("12.5")
        foo_bar_baz("abc", 12)
        foo_bar_baz(12, "abc")

def test_returns_and_does_not_print(capsys):
    """Ensure the function returns a string and does not print to stdout."""
    # 1. Call the function
    result = foo_bar_baz(5)
    
    # 2. Capture any console output
    captured = capsys.readouterr()
    
    # 3. Assert absolutely nothing was printed to the console
    assert captured.out == "", "Function should not print anything!"
    
    # 4. Assert the function actually returned the correct string
    assert result == "1 2 Foo 4 Bar", "Function must return the string, not None."
