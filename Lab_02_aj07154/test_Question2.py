import pytest
import hashlib
from Question2 import *

question1_testcases = [
([[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]],'5cdf3bef76904caa92ac20b15d533312c615dc3fe18ca06f41a5a43483b8e8c0'),
([[12,7,3],[4,5,6],[7,8,9]],[[5,8,1],[6,7,3],[4,5,9]],'a0a15fd17304cdfa8f689031b8fb300f36aeaf263e9753580bd5fd2dd2934441'),
([[1],[1],[1]],[[2],[2],[4]],'b2b5c1e8e915612b1a7b2ca51381a2a689ebae5222f8dd376da8f2d8ad0dc9ac'),
([[0,1,2],[9,8,7]],[[6,5,4],[3,4,5]],'bbc6b0272f2539e1e63d05ba1e63b28418562b82baa28e82376133ca6817f7e9'),
([[1,1,1]],[[2,2,4]],'85d0cd0d16d2e13bdf6a12b6b452ff4b36cd16b3a5234355d0d6754a9009ccf1'),
([[1],[2]],[[3,5],[4,6]],'c7b9fbc23c0c3916d13c4888b9b1630446059cfd7e079780be8ed788e1a4253b'),
([[1, 2], [0, 3]],[[4, 5, 6], [7, 8, 9]],'c7b9fbc23c0c3916d13c4888b9b1630446059cfd7e079780be8ed788e1a4253b') 
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,lst2,result",question1_testcases)
def test_question1(lst1,lst2,result):
    assert hashcode(matrix_subtraction(lst1,lst2)) == result