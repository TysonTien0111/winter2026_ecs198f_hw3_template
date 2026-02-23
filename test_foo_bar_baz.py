import pytest
from foo_bar_baz import foo_bar_baz

def test_foo_bar_baz_comprehensive():
    # 1. Edge Cases: Zero and Negative Numbers 
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-100) == ""

    # 2. Algorithmic check for a massive range of numbers
    # This loop ensures we catch ANY hardcoded ceilings or random skipped numbers
    for n in range(1, 101):
        expected_parts = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                expected_parts.append("Baz")
            elif i % 3 == 0:
                expected_parts.append("Foo")
            elif i % 5 == 0:
                expected_parts.append("Bar")
            else:
                expected_parts.append(str(i))
        
        expected_str = " ".join(expected_parts)
        result = foo_bar_baz(n)
        
        # Verifies the mathematical correctness 
        assert result == expected_str, f"Failed at n={n}"
        
        # 3. Ensures the output is a correctly formatted space-delimited string 
        assert type(result) is str, "Output must strictly be a string"
        assert result == result.strip(), "Contains leading or trailing whitespace"
        if n > 0:
            assert "  " not in result, "Contains double spaces"

def test_foo_bar_baz_type_exceptions():
    # 4. Edge Cases: Invalid Types 
    # Since it strictly takes an integer n as input, 
    # wrong types should trigger a TypeError.
    with pytest.raises(TypeError):
        foo_bar_baz(1.5)
    with pytest.raises(TypeError):
        foo_bar_baz("10")
    with pytest.raises(TypeError):
        foo_bar_baz() # Missing argument entirely
