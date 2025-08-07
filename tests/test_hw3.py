import pytest
import hw3

@pytest.mark.parametrize(
    "arr, expected",
    [[[1,2,3,4,5],[5,4,3,2,1]],
     [[6,8,3,0,1],[8,6,3,1,0]],
     [[3,6,9,3,1,1], [9,6,3,3,1,1]]]
)

def tests_bubble_sort(arr, expected):
    assert expected == hw3.bubble_sort(arr)

def tests_bubble_sort_change_order():
    assert [1, 2, 3, 4, 5] == hw3.bubble_sort([1, 2, 3, 4, 5], order_by=lambda x, y: x > y)
    assert [0, 1, 3, 6, 8] == hw3.bubble_sort([6, 8, 3, 0, 1], order_by=lambda x, y: x > y)
    assert [1, 1, 3, 3, 6, 9] == hw3.bubble_sort([3, 6, 9, 3, 1, 1], order_by=lambda x, y: x > y)

@pytest.mark.parametrize(
    "arr, expected",
    [[[1,2,3,4,5],([5,4,3,2,1], 4, 10)],
     [[6,8,3,0,1],([8,6,3,1,0],4, 10)],
     [[3,6,9,3,1,1], ([9,6,3,3,1,1],5, 15)]]
)

def tests_selection_sort(arr, expected):
    assert expected == hw3.selection_sort(arr)

def tests_selection_sort_change_order():
    assert ([1, 2, 3, 4, 5], 4, 10) == hw3.selection_sort([1, 2, 3, 4, 5], order_by=lambda x, y: x < y)
    assert ([0, 1, 3, 6, 8], 4, 10) == hw3.selection_sort([6, 8, 3, 0, 1], order_by=lambda x, y: x < y)
    assert ([1, 1, 3, 3, 6, 9], 5, 15) == hw3.selection_sort([3, 6, 9, 3, 1, 1], order_by=lambda x, y: x < y)
