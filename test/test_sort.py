import pytest
from libraly import bubble_sort

def test_bubble_sort():

    arr1 = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr1)
    assert arr1 == [11, 12, 22, 25, 34, 64, 90]


    arr2 = [1, 2, 3, 4, 5]
    bubble_sort(arr2)
    assert arr2 == [1, 2, 3, 4, 5]


    arr3 = [5, 4, 3, 2, 1]
    bubble_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    pytest.main()
