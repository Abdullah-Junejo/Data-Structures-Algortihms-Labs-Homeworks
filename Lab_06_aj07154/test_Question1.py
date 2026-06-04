import pytest
import hashlib
from Question1 import *

question1_testcases = [
([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42],15,'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683'),
([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42],14,'1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464'),
([0, 1, 2, 8, 13, 17, 19, 32, 42],1,'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 32, '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451'),
([0, 1, 2, 3, 8, 13, 17, 19, 32, 42],-1,'1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,item,result",question1_testcases)
def test_question1(lst,item,result):
    assert hashcode(binary_search_iterative(lst,item)) == result