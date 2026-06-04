import pytest
import hashlib
from Question1 import *

question1_testcases = [
(3,3,[[0,0,0],[0,0,0],[0,0,0]]),
(2,5,[[0,0,0,0,0],[0,0,0,0,0]]),
(7,3,[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]),
(5,5,[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]),
(6,2,[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]),
(4,5,[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("rows,cols,result",question1_testcases)
def test_question1(rows,cols,result):
    assert initialize_matrix(rows,cols) == result