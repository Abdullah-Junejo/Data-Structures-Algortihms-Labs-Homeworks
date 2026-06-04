import pytest
import hashlib

from Question2 import enQueue, deQueue, front, is_empty

enQueue_testcases = [
    ([None, None, None, None, None], 1, [1, None, None, None, None]),
    ([1, None, None, None, None], 2, [1, 2, None, None, None]),
    ([1, 2, None, None, None], 3, [1, 2, 3, None, None]),
    ([1, 2, 3, None, None], 4, [1, 2, 3, 4, None]),
    ([1, 2, 3, 4, None], 5, [1, 2, 3, 4, 5])
]
deQueue_testcases = [
    ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, None]),
    ([2, 3, 4, 5, None], 2, [3, 4, 5, None, None]),
    ([3, 4, 5, None, None], 3, [4, 5, None, None, None]),
    ([4, 5, None, None, None], 4, [5, None, None, None, None]),
    ([5, None, None, None, None], 5, [None, None, None, None, None])    
    ]

front_testcases = [
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
    ([2, 3, 4, 5, None], 2, [2, 3, 4, 5, None]),
    ([3, 4, 5, None, None], 3, [3, 4, 5, None, None]),
    ([4, 5, None, None, None], 4, [4, 5, None, None, None]),
    ([5, None, None, None, None], 5, [5, None, None, None, None])
    ]

isempty_testcases = [
    ([None, None, None, None, None], True, [None, None, None, None, None]),
    ([1, None, None, None, None], False, [1, None, None, None, None]),
    ([1, 2, 3, 4, 5], False, [1, 2, 3, 4, 5]),
    ([None], True, [None]),
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,value,result", enQueue_testcases)
def test_enqueue(list,value,result):
    assert enQueue(list,value) == None
    assert list == result

@pytest.mark.parametrize("list,result,updatedList", deQueue_testcases)
def test_dequeue(list,result,updatedList):
    assert deQueue(list) == result
    assert list == updatedList

@pytest.mark.parametrize("list,result,updatedList", front_testcases)
def test_front(list,result,updatedList):
    assert front(list) == result
    assert list == updatedList


@pytest.mark.parametrize("list,result,updatedList", isempty_testcases)
def test_IsEmpty(list,result,updatedList):
    assert is_empty(list) == result
    assert list == updatedList
    assert type(is_empty(list)) == bool