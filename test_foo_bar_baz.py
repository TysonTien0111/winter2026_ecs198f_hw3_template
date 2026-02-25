import pytest
import foo_bar_baz

def test_exhaustive_logic():
    """Check every value from 1 to 50 for correct sequence logic."""
    for n in range(1, 51):
        result = foo_bar_baz.foo_bar_baz(n)
        words = result.split(" ")
        
        # Check length
        assert len(words) == n, f"Length mismatch for n={n}"
        
        # Check each word
        for i in range(1, n + 1):
            val = i
            word = words[i-1]
            if val % 3 == 0 and val % 5 == 0:
                assert word == "Baz", f"Expected Baz at {val} for n={n}"
            elif val % 3 == 0:
                assert word == "Foo", f"Expected Foo at {val} for n={n}"
            elif val % 5 == 0:
                assert word == "Bar", f"Expected Bar at {val} for n={n}"
            else:
                assert word == str(val), f"Expected {val} at {val} for n={n}"

def test_formatting_spaces():
    """Ensure exactly one space between words and no trailing spaces."""
    n = 10
    result = foo_bar_baz.foo_bar_baz(n)
    # n words should have n-1 spaces
    assert result.count(" ") == n - 1
    # Ensure no double spaces
    assert "  " not in result
    # Ensure no leading/trailing whitespace
    assert result == result.strip()

def test_empty_for_zero_or_negative():
    assert foo_bar_baz.foo_bar_baz(0) == ""
    assert foo_bar_baz.foo_bar_baz(-1) == ""
    assert foo_bar_baz.foo_bar_baz(-10) == ""

def test_type_errors():
    with pytest.raises(TypeError):
        foo_bar_baz.foo_bar_baz(1.5)
    with pytest.raises(TypeError):
        foo_bar_baz.foo_bar_baz("5")
    with pytest.raises(TypeError):
        foo_bar_baz.foo_bar_baz(None)
    with pytest.raises(TypeError):
        # Missing argument
        foo_bar_baz.foo_bar_baz()

def test_case_sensitivity():
    result = foo_bar_baz.foo_bar_baz(15)
    # Requirement says "Foo", "Bar", "Baz"
    assert "Foo" in result
    assert "Bar" in result
    assert "Baz" in result
    # Ensure no lowercase versions
    assert "foo" not in result
    assert "bar" not in result
    assert "baz" not in result

def test_no_fizzbuzz_labels():
    result = foo_bar_baz.foo_bar_baz(15)
    # Make sure we didn't use common FizzBuzz words
    assert "Fizz" not in result
    assert "Buzz" not in result
