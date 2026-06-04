import pytest
import hashlib

from Question1 import push, pop, top, is_empty

push_testcases = [
    ([None, None, None, None, None], 1, [1, None, None, None, None]),
    ([1, None, None, None, None], 2, [1, 2, None, None, None]),
    ([1, 2, None, None, None], 3, [1, 2, 3, None, None]),
    ([1, 2, 3, None, None], 4, [1, 2, 3, 4, None]),
    ([1, 2, 3, 4, None], 5, [1, 2, 3, 4, 5])
]
pop_testcases = [
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, None]),
    ([1, 2, 3, 4, None], 4, [1, 2, 3, None, None]),
    ([1, 2, 3, None, None], 3, [1, 2, None, None, None]),    
    ([1, 2, None, None, None], 2, [1, None, None, None, None]),
    ([1, None, None, None, None], 1, [None, None, None, None, None]),
    ]

top_testcases = [
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, None], 4, [1, 2, 3, 4, None]),
    ([1, 2, 3, None, None], 3, [1, 2, 3, None, None]),
    ([1, 2, None, None, None], 2, [1, 2, None, None, None]),
    ([1, None, None, None, None], 1, [1, None, None, None, None]),
    ]

isempty_testcases = [
    ([None, None, None, None, None], True, [None, None, None, None, None]),
    ([1, None, None, None, None], False, [1, None, None, None, None]),
    ([1, 2, 3, 4, 5], False, [1, 2, 3, 4, 5])
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,value,result", push_testcases)
def test_push(list,value,result):
    assert push(list,value) == None
    assert list == result

@pytest.mark.parametrize("list,result,updatedList", pop_testcases)
def test_pop(list,result,updatedList):
    assert pop(list) == result
    assert list == updatedList

@pytest.mark.parametrize("list,result,updatedList", top_testcases)
def test_top(list,result,updatedList):
    assert top(list) == result
    assert list == updatedList


@pytest.mark.parametrize("list,result,updatedList", isempty_testcases)
def test_IsEmpty(list,result,updatedList):
    assert is_empty(list) == result
    assert list == updatedList
    assert type(is_empty(list)) == bool