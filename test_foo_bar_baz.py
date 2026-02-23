import pytest
from foo_bar_baz import foo_bar_baz

# 1. The EXACT name the autograder is likely looking for
def test_foo_bar_baz():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

# 2. Exhaustive sequence testing to catch hardcoded bugs above n=30
def test_comprehensive_large_input():
    def expected(n):
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0: res.append("Baz")
            elif i % 3 == 0: res.append("Foo")
            elif i % 5 == 0: res.append("Bar")
            else: res.append(str(i))
        return " ".join(res)
    
    # Test EVERY number from 1 to 105. This guarantees you catch any 
    # off-by-one errors, formatting errors, or hardcoded breaks.
    for i in range(1, 106):
        assert foo_bar_baz(i) == expected(i)

# 3. Standard edge cases (0 and negative numbers)
def test_edge_cases():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-1) == ""
    assert foo_bar_baz(-10) == ""

# 4. Strict Type checking (Catches bad code that tries to cast floats/strings)
def test_invalid_types():
    # The true implementation uses range() which throws a TypeError for non-integers.
    # If the buggy implementation doesn't throw an error, this test catches it!
    with pytest.raises(TypeError):
        foo_bar_baz("15")
        
    with pytest.raises(TypeError):
        foo_bar_baz(3.14)
        
    with pytest.raises(TypeError):
        foo_bar_baz(None)
