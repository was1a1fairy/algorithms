from hw1 import *
import pytest

@pytest.mark.parametrize(
    "n, expected",
    [[20, 2_432_902_008_176_640_000],
    [0, 1],
    [1, 1],
    [2, 2],
    [3, 6]
])

def test_factorial(n, expected):
    assert factorial(n) == expected

@pytest.mark.parametrize(
    "n, expected",
    [
    [0, [0]],
    [1, [0,1,1]],
    [2, [0,1,1,2]],
    [15, [0,1,1,2,3,5,8,13]]
])

def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [[1, 1],
     [2, 1],
     [3, 2],
     [0, 0],
     [100, 3]]
)

def test_count_ones(n,expected):
    assert count_ones(n) == expected

@pytest.mark.parametrize(
    "n, expected",
    [[1, True],
     [100, False],
     [303, True],
     [6116, True],
     [34543, True]]
)

def test_is_palindrome(n, expected):
    assert is_palindrome(n) == expected

def test_negative_input():
    with pytest.raises(TypeError):
        factorial("nnnn")
        factorial(6.7)
        fibonacci("mmm")
        fibonacci(4.4)
        count_ones(6.6)
        count_ones("(((")
        is_palindrome("))")
        is_palindrome(7.7)