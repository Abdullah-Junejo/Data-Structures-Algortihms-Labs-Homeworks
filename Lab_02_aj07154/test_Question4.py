import pytest
import hashlib
from Question4 import *

question3_testcases = [
([[12,7,3],[4 ,5,6],[7 ,8,9]],[[5,8,1,2],[6,7,3,0], [4,5,9,1]],'85c7d0fa4cb82523bd7f65fa58a2cb17734918b30803da5c831dedafad62d698'),
([[34,1,77],[2,14,8],[3 ,17,11]],[[6,8,1],[9,27,5],[2,43,31]],'ae7e7128fb06dabb76701ba3c3ebb8b033a4ec3bef6a9f24afb2a5c0642ee0b5'),

([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]],'36915bbce54481d802a42c727d1b140f222a560f35f33d539369083770977f90'),
([[3,4,2]],[[13,9,7,15],[8,7,4,6],[6,4,0,3]],'6c41e8bf9f18d796b09465f9a4de6194e8caa66f25fb256cab53f59cd1b860cc'),
([[-1, 3, 4, -3], [2, -2, 6, 0]],[[5, 7, -1], [8, 9, -4], [4, -2, 6], [2, 3, 1]],'eac14bcfffed9d76473a948ef5804db3ecfc1751d2ec72e5af65b6b090008ca8'),
([[1, 2, -1], [2, 0, 1]],[[3, 1], [0, -1], [-2, 3]],'fdda4d5cfc00db23e3792c06d0f52edffef9a9721ffd11b7f3146796a2bea523'),
([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],[[-2], [1], [0]],'812dd3f4e07326125efa54ae462c88c0f41d59969703ebdda6dcffae22f936c9'),
([[7, 3], [2, 5], [6, 8], [9, 0]],[[8, 14, 0, 3, -1], [7, 11, 5, 91, 3], [8, -4, 19, 5, 57]],'519b7d5fc632a6bb595c7ec91f3d1f4adfa285e0baae1f051e30b04e248c7b7a'),
([[1, 4, 6, 10], [2, 7, 5, 3]],[[1, 4, 6, 10], [2, 7, 5, 3], [9, 0, 11, 8]],'519b7d5fc632a6bb595c7ec91f3d1f4adfa285e0baae1f051e30b04e248c7b7a'),
([[1, 4, 6, 10], [2, 7, 5, 3], [9, 0, 11, 8]],[[1, 4, 6, 10], [2, 7, 5, 3]],'519b7d5fc632a6bb595c7ec91f3d1f4adfa285e0baae1f051e30b04e248c7b7a') 
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,lst2,result",question3_testcases)
def test_question1(lst1,lst2,result):
    assert hashcode(matrix_multiplication(lst1,lst2)) == result