import pytest
from my_list import MyList
from list_node import ListNode

def test_empty_list():
    lst = MyList()
    assert len(lst) == 0
    assert str(lst) == "None"
    assert lst.head is None

def test_single_element():
    lst = MyList(1)
    assert len(lst) == 1
    assert str(lst) == "(1) -> None"
    assert lst.head.value == 1
    assert lst.head.next is None

def test_append():
    lst = MyList()
    lst.append(1)
    lst.append(2)
    assert len(lst) == 2
    assert str(lst) == "(1) -> (2) -> None"

def test_contains():
    lst = MyList(1)
    lst.append(2)
    assert 1 in lst
    assert 2 in lst
    assert 3 not in lst

def test_remove():
    lst = MyList(1)
    lst.append(2)
    lst.append(3)
    lst.remove(2)
    assert str(lst) == "(1) -> (3) -> None"
    with pytest.raises(ValueError):
        lst.remove(4)

def test_pop():
    lst = MyList(1)
    lst.append(2)
    lst.append(3)
    assert lst.pop() == 3
    assert lst.pop(0) == 1
    assert str(lst) == "(2) -> None"

def test_extend():
    lst1 = MyList(1)
    lst2 = MyList(2)
    lst1.extend(lst2)
    assert str(lst1) == "(1) -> (2) -> None"

def test_insert():
    lst = MyList(1)
    lst.insert(0, 0)
    lst.insert(2, 2)
    lst.insert(2, 1.5)
    assert str(lst) == "(0) -> (1) -> (1.5) -> (2) -> None"

def test_reverse():
    lst = MyList(1)
    lst.append(2)
    lst.append(3)
    lst.reverse()
    assert str(lst) == "(3) -> (2) -> (1) -> None"

def test_index():
    lst = MyList(1)
    lst.append(2)
    lst.append(1)
    assert lst.index(1) == 0
    assert lst.index(2) == 1
    with pytest.raises(ValueError):
        lst.index(3)

def test_count():
    lst = MyList(1)
    lst.append(2)
    lst.append(1)
    assert lst.count(1) == 2
    assert lst.count(2) == 1
    assert lst.count(3) == 0

def test_equality():
    lst1 = MyList(1)
    lst1.append(2)
    lst2 = MyList(1)
    lst2.append(2)
    assert lst1 == lst2
    lst2.append(3)
    assert lst1 != lst2

def test_copy():
    lst1 = MyList(1)
    lst1.append(2)
    lst2 = lst1.copy()
    assert lst1 == lst2
    lst2.append(3)
    assert lst1 != lst2

def test_clear():
    lst = MyList(1)
    lst.append(2)
    lst.clear()
    assert len(lst) == 0
    assert lst.head is None
