import pytest
import hashlib
from sys import stderr
from Question4 import *

question1_testcases = [
([[5, 8, 1], [6, 7, 3], [5, 4, 9]],0,'8d2d5f3953fb0bb08386d3bdbf9934d5bc62994bc1404c8b6048680e5758c467'),
([['square', 'rectangle', 'triangle'], ['chair','table', 'house'], ['motor cycle', 'car', 'truck']],2,'b6a6f9140d75a1dda49f0244332b32d72b7f1d411f1a4e8ab105ac6b2fcc67c4'),
([[75, 28, 12], [63, 37, 23], [84, 15, 49]],1,'b6ac76a4ac5388d81110af83b5c027e3a2d4ef36761a1c40031a7caab5d53048')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,dimension,result",question1_testcases)
def test_question1(capsys,dimension,lst1,result):
    assert hashcode(sort_matrix_by_columnNumber(lst1,dimension)) == result