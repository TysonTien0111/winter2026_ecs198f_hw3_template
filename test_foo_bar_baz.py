import pytest
from foo_bar_baz import foo_bar_baz

def test_basic_sequence():
    """Test a small sequence to verify basic Foo, Bar, and Baz logic."""
    # 1, 2, 3(Foo), 4, 5(Bar) ... 15(Baz)
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(15) == expected

def test_single_values():
    """Test individual edge cases and small n values."""
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

@pytest.mark.parametrize("n, expected_end", [
    (3, "Foo"),
    (5, "Bar"),
    (15, "Baz"),
    (30, "Baz"),
])
def test_divisibility_rules(n, expected_end):
    """Ensure the nth element correctly identifies Foo, Bar, or Baz."""
    result = foo_bar_baz(n)
    last_element = result.split()[-1]
    assert last_element == expected_end

def test_formatting():
    """Verify that the output is space-delimited with no trailing spaces."""
    n = 10
    result = foo_bar_baz(n)
    # Ensure there are exactly n-1 spaces for n elements
    assert result.count(" ") == n - 1
    # Ensure no leading or trailing whitespace
    assert result == result.strip()

def test_edge_case_zero_or_negative():
    """Verify behavior with n <= 0 (should return an empty string based on range logic)."""
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-5) == ""
