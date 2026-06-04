import pytest
import hashlib
from Question4 import *

question4_testcases = [
    (['a', 'b', 'c'], 2, "253850a2e327ae961242ad808aef20dc3d2dd13336801730e3b69c5613df846d"),
    ([1, 2, 3], 2, "244ed147cf0ebf5385e4b701d333eda7c18f11c09fe1a2e0828781d8f6591f5d"),
    ([2, 'a', False], 2, "50822226e42844100e405aebcf2f20ffaa126b11b73a7762f761d42b51fc481f"),
    ([10, 20], 4,"53badcf8cbe44d3b4c46bc6c4369e4064fe291dacc42aef08850862273fbed6c"),
    (["queue"], 10, "9155d1524e3cc7360e1595661dfb0b620d56d6b736042872446ed5eaf11d70d3")
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("A,n,result", question4_testcases)
def test_question4(A, n, result):
    assert hashcode(stutter(A, n)) == result