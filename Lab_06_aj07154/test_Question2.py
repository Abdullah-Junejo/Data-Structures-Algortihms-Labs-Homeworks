import pytest
import hashlib
from Question2 import *

question2_testcases = [
([0, 1, 2, 8, 13, 17, 19, 32, 42], 2,'d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 17,'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d'),
([0, 1, 2, 8, 13, 17, 19, 32, 42],1,'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 42, '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 3,'4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,item,result",question2_testcases)
def test_question1(lst,item,result):
    assert hashcode(binary_search_iterative_modified(lst,item)) == result