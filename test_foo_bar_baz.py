import pytest
from foo_bar_baz import foo_bar_baz

def test_single_value_1():
    assert foo_bar_baz(1) == "1"

def test_single_value_2():
    assert foo_bar_baz(2) == "1 2"

def test_divisible_by_3_only():
    # n=3 should end with Foo
    result = foo_bar_baz(3)
    assert result == "1 2 Foo"

def test_divisible_by_5_only():
    # n=5 should end with Bar
    result = foo_bar_baz(5)
    assert result == "1 2 Foo 4 Bar"

def test_divisible_by_both_3_and_5():
    # n=15 is the first Baz
    result = foo_bar_baz(15)
    expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert result == expected

def test_divisible_by_both_3_and_5_extended():
    # n=30 should have two Baz occurrences
    result = foo_bar_baz(30)
    words = result.split()
    assert words[14] == "Baz"
    assert words[29] == "Baz"

def test_sequence_up_to_10():
    assert foo_bar_baz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"

def test_formatting_no_trailing_space():
    result = foo_bar_baz(5)
    assert result == result.strip()
    assert len(result.split(" ")) == 5

def test_formatting_spaces_between_words():
    result = foo_bar_baz(10)
    assert "  " not in result
    assert result.count(" ") == 9

def test_edge_case_zero():
    assert foo_bar_baz(0) == ""

def test_edge_case_negative():
    assert foo_bar_baz(-5) == ""

def test_type_error_float():
    with pytest.raises(TypeError):
        foo_bar_baz(5.5)

def test_type_error_string():
    with pytest.raises(TypeError):
        foo_bar_baz("10")

def test_type_error_none():
    with pytest.raises(TypeError):
        foo_bar_baz(None)

def test_case_sensitivity():
    # Ensure it's not "foo", "bar", "baz"
    result = foo_bar_baz(15)
    assert "Foo" in result
    assert "Bar" in result
    assert "Baz" in result
    assert "foo" not in result
    assert "bar" not in result
    assert "baz" not in result

def test_no_fizz_buzz():
    # Ensure it's not the standard FizzBuzz words
    result = foo_bar_baz(15)
    assert "Fizz" not in result
    assert "Buzz" not in result
