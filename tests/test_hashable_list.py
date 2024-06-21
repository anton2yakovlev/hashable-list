from hashable_list.hashable_list import HashableList


def test_first():
    assert 1 == 1


def test_smoke_test():
    assert HashableList(1, 2, 3) == [1, 2, 3]
