import pytest
from foo_bar_baz import foo_bar_baz

def testBasicSequence():
  expected = "1 2"
  assert foo_bar_baz(2) == expected

  expected = "1 2 Foo 4"
  assert foo_bar_baz(4) == expected

  expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar"
  assert foo_bar_baz(10) == expected

  expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
  assert foo_bar_baz(15) == expected

  expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
  assert foo_bar_baz(30) == expected

  expected = "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz 31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz 46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 Baz 61 62 Foo 64 Bar Foo 67 68 Foo Bar 71 Foo 73 74 Baz 76 77 Foo 79 Bar Foo 82 83 Foo Bar 86 Foo 88 89 Baz 91 92 Foo 94 Bar Foo 97 98 Foo"
  assert foo_bar_baz(99) == expected

def testSingleValues():
  assert foo_bar_baz(1) == "1"
  assert foo_bar_baz(3) == "1 2 Foo"
  assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

@pytest.mark.parametrize("n, expectedSequence", [
  (3, "1 2 Foo"),
  (5, "1 2 Foo 4 Bar"),
  (15, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"),
  (30, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz")
])

def testDivisibilityRules(n, expectedSequence):
  assert foo_bar_baz(n) == expectedSequence

def testFormatting():
  n = 10
  result = foo_bar_baz(n)
  assert result.count(" ") == n -1
  assert result == result.strip()
  assert "  " not in result

  n = 0
  result = foo_bar_baz(n)
  assert result.count(" ") == 0
  assert result == result.strip()
  assert "  " not in result

  n = -5
  result = foo_bar_baz(n)
  assert result.count(" ") == 0
  assert result == result.strip()
  assert "  " not in result

  n = 15
  result = foo_bar_baz(n)
  words = result.split(" ")

  assert len(words) == n

  for word in words:
    assert word in ["Foo", "Bar", "Baz"] or word.isdigit()

def testEdgeCaseZeroOrNegative():
  assert foo_bar_baz(0) == ""
  assert foo_bar_baz(-5) == ""

def testTypeError():
  with pytest.raises(TypeError):
    foo_bar_baz(0.5)

  with pytest.raises(TypeError):
    foo_bar_baz(5.0)

  with pytest.raises(TypeError):
    foo_bar_baz(None)

  with pytest.raises(TypeError):
    foo_bar_baz("5")

  with pytest.raises(TypeError):
    foo_bar_baz("abc")

  with pytest.raises(TypeError):
    foo_bar_baz("12.5")

  with pytest.raises(TypeError):
    foo_bar_baz()

  with pytest.raises(TypeError):
    foo_bar_baz(1, 2)

  with pytest.raises(TypeError):
    foo_bar_baz([1, 2, 3])

  with pytest.raises(TypeError):
    foo_bar_baz({"apple" : 1, "banana" : 2})

def testBoolType():
  assert foo_bar_baz(True) == "1"
  assert foo_bar_baz(False) == ""

def testInfiniteLoop():
  assert foo_bar_baz(-1) == ""

def testLargeNumberEfficiencyAndType():
  n = 100000
  result = foo_bar_baz(n)

  assert isinstance(result, str)
  assert result.startswith("1 2 Foo 4 Bar")
  assert result.endswith("Bar")
  assert result.count(" ") == n - 1

def testSneakyConversionsAndSpacing():
  with pytest.raises(TypeError):
    foo_bar_baz(5.9)

  result = foo_bar_baz(5)
  assert result == "1 2 Foo 4 Bar"
  assert len(result) == 13

def testDynamicLogic():
  n = 100
  result = foo_bar_baz(n).split(" ")

  assert len(result) == n

  for i in range(1, n + 1):
    word = result[i - 1]

    if i % 3 == 0 and i % 5 == 0:
      assert word == "Baz"
    elif i % 3 == 0:
      assert word == "Foo"
    elif i % 5 == 0:
      assert word == "Bar"
    else:
      assert word == str(i)

def testExhaustiveLoopAndKwargs():
  assert foo_bar_baz(n=5) == "1 2 Foo 4 Bar"

  for test_n in range(1, 101):
    result = foo_bar_baz(test_n).split(" ")

    assert len(result) == test_n

    for i, word in enumerate(result, start=1):
      if i % 15 == 0:
        assert word == "Baz"
      elif i % 3 == 0:
        assert word == "Foo"
      elif i % 5 == 0:
        assert word == "Bar"
      else:
        assert word == str(i)

def testTypeHints():
  annotations = foo_bar_baz.__annotations__

  assert annotations.get('n') == int
  assert annotations.get('return') == str

def testLargeNumberBazLogic():
  n = 300
  result = foo_bar_baz(n).split(" ")

  assert result[-1] == "Baz"
