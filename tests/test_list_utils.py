import pytest
from list_utils import remove_duplicates, find_max, flatten_list, count_occurrences


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]


def test_remove_duplicates_invalid():
    with pytest.raises(TypeError):
        remove_duplicates("not a list")


def test_find_max():
    assert find_max([1, 5, 3]) == 5


def test_find_max_empty():
    with pytest.raises(ValueError):
        find_max([])


def test_flatten_list():
    assert flatten_list([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_flatten_list_invalid():
    with pytest.raises(TypeError):
        flatten_list("invalid")


def test_count_occurrences():
    assert count_occurrences([1, 2, 2, 3], 2) == 2