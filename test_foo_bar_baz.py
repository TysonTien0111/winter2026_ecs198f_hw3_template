from foo_bar_baz import foo_bar_baz
import pytest

def testExhaustiveLogic():
    for n in range(1, 51):
        result = foo_bar_baz(n)
        words = result.split(" ")

        assert len(words) == n, f"Length mismatch for n = {n}"

        for i in range(1, n + 1):
            val = i
            word = words[i - 1]

            if val % 3 == 0 and val % 5 == 0:
                assert word == "Baz", f"Expected Baz at {val} for n = {n}"
            elif val % 3 == 0:
                assert word == "Foo", f"Expected Foo at {val} for n = {n}"
            elif val % 5 == 0:
                assert word == "Bar", f"Expected Bar at {val} for n = {n}"
            else:
                assert word == str(val), f"Expected {val} at {val} for n = {n}"

def testFormattingSpaces():
    n = 10
    result = foo_bar_baz(n)

    assert result.count(" ") == n - 1
    assert "  " not in result
    assert result == result.strip()

def testEmptyForZeroOrNegative():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-10) == ""

def testTypeErrors():
    with pytest.raises(TypeError):
        foo_bar_baz(1.5)
    with pytest.raises(TypeError):
        foo_bar_baz("5")
    with pytest.raises(TypeError):
        foo_bar_baz(None)
    with pytest.raises(TypeError):
        # Missing argument typically raises TypeError in Python functions
        foo_bar_baz()

def testCaseSensitivity():
    result = foo_bar_baz(15)

    assert "Foo" in result
    assert "Bar" in result
    assert "Baz" in result
    assert "foo" not in result
    assert "bar" not in result
    assert "baz" not in result

def testNoFizzBuzzLabels():
    result = foo_bar_baz(15)

    assert "Fizz" not in result
    assert "Buzz" not in result
