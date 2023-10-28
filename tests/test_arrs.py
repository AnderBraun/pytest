import pytest

from utils.arrs import get
from utils.arrs import my_slice
@pytest.fixture()
def test_get_existing_index():
    array = [1, 2, 3, 4]
    index = 2
    assert get(array, index) == 3

def test_get_non_existing_index():
    array = [1, 2, 3, 4]
    index = 5
    default = 'Not found'
    assert get(array, index, default) == default

def test_get_negative_index():
    array = [1, 2, 3, 4]
    index = -1
    assert get(array, index) == None

def test_get_empty_array():
    array = []
    index = 0
    default = 'Empty'
    assert get(array, index, default) == default


def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5], start=2) == [3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5], start=-3) == [3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5], end=3) == [1, 2, 3]
    assert my_slice([1, 2, 3, 4, 5], end=-2) == [1, 2, 3]
    assert my_slice([1, 2, 3, 4, 5], start=1, end=4) == [2, 3, 4]

    assert my_slice([]) == []
    assert my_slice([], start=3, end=5) == []

    assert my_slice([1, 2, 3, 4, 5], start=10) == []
    assert my_slice([1, 2, 3, 4, 5], end=10) == [1, 2, 3, 4, 5]

    assert my_slice([1, 2, 3, 4, 5], start=-5, end=-2) == [1, 2, 3]
    assert my_slice([1, 2, 3, 4, 5], start=-5, end=-1) == [1, 2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5], start=-5, end=-6) == []

    assert my_slice("Hello, World!") == "Hello, World!"
    assert my_slice("Hello, World!", start=7) == "World!"
    assert my_slice("Hello, World!", start=-6) == "World!"
    assert my_slice("Hello, World!", end=5) == "Hello"
    assert my_slice("Hello, World!", end=-8) == "Hello"
    assert my_slice("Hello, World!", start=1, end=9) == "ello, Wo"


pytest.main()