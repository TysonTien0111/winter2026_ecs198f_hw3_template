import pytest
import inspect
from foo_bar_baz import foo_bar_baz

def test_signature_and_types():
    # Catches bugs where the instructor removed type hints or changed parameter counts
    sig = inspect.signature(foo_bar_baz)
    assert "n" in sig.parameters, "Parameter must be named 'n'"
    assert len(sig.parameters) == 1, "Function must take exactly one parameter"
    assert sig.parameters["n"].annotation is int, "Parameter 'n' must have an int type hint"
    assert sig.return_annotation is str, "Return type hint must be str"

def test_keyword_argument():
    # Catches bugs where the parameter was renamed (e.g., 'num' instead of 'n')
    assert foo_bar_baz(n=5) == "1 2 Foo 4 Bar"

def test_argument_counts():
    # Catches bugs where the function allows 0 arguments or extra arguments
    with pytest.raises(TypeError):
        foo_bar_baz()
    with pytest.raises(TypeError):
        foo_bar_baz(15, "extra_argument")

def test_comprehensive_sequence():
    # Exhaustively tests 1 through 100 to catch ANY hardcoded hidden bugs on random numbers
    def expected(n):
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0: res.append("Baz")
            elif i % 3 == 0: res.append("Foo")
            elif i % 5 == 0: res.append("Bar")
            else: res.append(str(i))
        return " ".join(res)
    
    for i in range(1, 101):
        assert foo_bar_baz(i) == expected(i)

def test_edge_cases():
    # Catches loops that fail on 0 or negative numbers
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-10) == ""

def test_invalid_types():
    # Catches implementations that don't enforce TypeError when bad types are passed
    invalid_inputs = [3.14, "15", None, [1, 2, 3], {"n": 5}]
    for val in invalid_inputs:
        with pytest.raises(TypeError):
            foo_bar_baz(val)

def test_strict_formatting():
    # Catches double spaces or trailing/leading whitespace
    for i in [4, 5, 6, 14, 15]:
        result = foo_bar_baz(i)
        assert isinstance(result, str)
        assert result == result.strip()
        assert not result.startswith(" ")
        assert not result.endswith(" ")
        assert "  " not in result

def test_foo_bar_baz():
    # A basic sanity check just in case the autograder expects this specific test name
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
