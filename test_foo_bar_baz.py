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

def test_larger_sequence():
    """Strictly test a sequence up to 30 to catch mid-sequence and formatting bugs."""
    # Replaces the old divisibility test that only checked the last element
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    assert foo_bar_baz(30) == expected

def test_strict_formatting():
    """Ensure no trailing, leading, or double spaces exist."""
    # Replaces the old space-counting test
    result = foo_bar_baz(5)
    
    # It should exactly match this, proving no trailing/leading spaces
    assert result == "1 2 Foo 4 Bar"
    
    # There should be no double spaces anywhere in the string
    assert "  " not in result

def test_edge_case_zero_or_negative():
    """Verify behavior with n <= 0 (should return an empty string based on range logic)."""
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-5) == ""

def test_invalid_types():
    """Ensure the function raises a TypeError for non-integer inputs."""
    invalid_inputs = ["15", 15.5, None, [3]]
    
    for val in invalid_inputs:
        with pytest.raises(TypeError):
            foo_bar_baz(val)
