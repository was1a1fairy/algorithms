import pytest
from hw2 import *

@pytest.mark.parametrize(
    "arr, start, end, expected",
    [[[1,2,3,4,5,6], 2, 4, (5, 2, 4)],
    [[1,2,3,4,5,6], 1, 1, (2, 0, 1)],
    [[1,2,3,4,5,6], 0, 5, (6, 5, 5)],
    [[1,2,3,4,5,6], 0, 8, (6, 5, 5)],
    [[1,2,3,4,5,6], -2, 4, (5, 4, 4)],
    [[0,0,0], 1, 4, (0, 0, 1)],
    [[-1,-8,-6,-3], 8, 4, (-1, 0, 0)]
    ]
)

def test_max_in_range(arr, start, end, expected):
    assert max_in_range(arr, start,end) == expected

def test_negative_max_in_range():
    with pytest.raises(TypeError):
        max_in_range("123", 1, 2)
        max_in_range([1,2,3], [1], 0)
        max_in_range([1,2,3], 0, "dd")

@pytest.mark.parametrize(
    "arr, k, expected",
    [[[1,2,3,4], 1, [3,2,1,4]],
    [[1,2,3,4], 2, [2,1,4,3]],
    [[1,2,3,4], 8, [4,3,2,1]],
    [[1,2,3,4], 9, [3,2,1,4]]
    ]
)

def tests_rotate_and_reverse(arr, k, expected):
    assert rotate_and_reverse(arr, k) == expected

def test_negative_rotate_and_reverse():
    with pytest.raises(TypeError):
        rotate_and_reverse("123", 5)
        rotate_and_reverse([1], "k")

@pytest.mark.parametrize(
    "arr, expected",
    [[[2,4,6,8], [8,6,4,2]],
     [[1,3,5,7], [1,3,5,7]],
     [[1,2,3,4,5], [1,4,3,2,5]],
     [[2,3,4,5,6], [6,3,4,5,2]],
     [[1,1,1,2,4,1,1,1], [1,1,1,4,2,1,1,1]],
     [[2,3,4,2], [2,3,4,2]],
     [[1,2,4,5], [1,4,2,5]]
     ]
)

def tests_reverse_even_elems(arr, expected):
    assert reverse_even_elements(arr) == expected

def tests_negative_reverse_even():
    pass

