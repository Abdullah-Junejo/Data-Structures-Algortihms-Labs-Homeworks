import pytest
import hashlib
from Question3 import *

question2_testcases = [
([[12,7],[4 ,5],[3 ,8]],'d479c7966e919fc29bcad1413d347a9da319449d7f8e1a8962ecc522cf54f9d9'),
([[12, 4, 3],[7, 5, 8]],'794c3881966741e61d18414fe4fcfb79faf68daa67e8e7be2278739a89287914'),
([[5, 4, 3], [4, 0, 4], [7, 10, 3]],'b42a5b24b21f70e1906e2f299eecd64cf614586d2a5356a2bd6609e08e39b92f'),
([[5, 4], [4, 0], [7, 10], [-1, 8]],'b4b7293a64bc6e2389d49b9ac72d844c6f090e2078fb6de49781164d5afb2e1b'),
([[1, 2, 3], [4, 5, 6]],'3821d19d25b6f8e539ad60f5beac15e6f2870d88244123ffebf5c9b56cff14ce') 
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,result",question2_testcases)
def test_question1(lst1,result):
    assert hashcode(matrix_transpose(lst1)) == result