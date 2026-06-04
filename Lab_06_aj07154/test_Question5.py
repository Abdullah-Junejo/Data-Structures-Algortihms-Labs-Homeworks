import pytest
import hashlib
from Question5 import *

question5_testcases = [
([0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42],19,'16390873ae6b6a173fc894a873bab02283debbd320b5f0758849d01afa6ee8b6'),
([0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42],42,'95bce61a71a78185f4b6f8f25fc6986108043727fe9d9c19dbe44b0081ef928a'),
([0, 0, 0, 0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42], 0,'02b6deebe10f247a39a1f40c6e045af149df9c96491adce129613e8b30480780'),
([0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42], 3,'4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'),
([0, 0, 0, 0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42], 17,'fb2198a0acebc52f7b463ee9f6d4a1fd1398f43515f3f2932dc5b4b90b4139a8')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,item,result",question5_testcases)
def test_question1(lst,item,result):
    assert hashcode(finding_multiple(lst,item)) == result

