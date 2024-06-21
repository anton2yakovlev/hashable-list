from functools import wraps
from typing import Any, Callable
from hashable_list.hashable_list import HashableList


def test_smoke_test():
    assert HashableList(1, 2, 3) == [1, 2, 3]


def test_empty_list():
    hashable_list = HashableList()
    assert hashable_list == []


def test_isinstance():
    assert isinstance(HashableList(), HashableList)


def test_hashable_list_as_key_in_dict():
    hashable_list = HashableList(1, 2, 3)
    dictionary = dict()
    dictionary[hashable_list] = hashable_list


def test_add_value_to_dict_key():
    hashable_list = HashableList(1, 2, 3)
    dictionary = dict()
    dictionary[hashable_list] = hashable_list.copy()
    hashable_list.append(4)


def test_it_has_hash():
    hashable_list = HashableList()
    assert hash(hashable_list) is not None


def test_contains():
    hashable_list = HashableList(1, 2, 3)
    assert 1 in hashable_list


def test_len():
    hashable_list = HashableList(1, 2, 3, 4, 5)
    assert len(hashable_list) == 5


def test_multitypes():
    hashable_list = HashableList(1, "2", [3, 4], {5: 6}, 7.0)
    assert hashable_list


def test_append():
    hashable_list = HashableList(1, 2)
    hashable_list.append(3)
    assert hashable_list == [1, 2, 3]


def test_pop():
    hashable_list = HashableList(1, 2, 3)
    assert hashable_list.pop() == 3


def test_init_from_iterable_object():
    hashable_list = HashableList([1, 2, 3])
    assert hashable_list == [1, 2, 3]


def test_init_from_few_iterable_objects():
    hashable_list = HashableList([1, 2, 3], [4, 5, 6])
    assert hashable_list == [[1, 2, 3], [4, 5, 6]]


def test_sort():
    hashable_list = HashableList([3, 1, 2])
    hashable_list.sort(reverse=True)
    assert hashable_list == [3, 2, 1]
