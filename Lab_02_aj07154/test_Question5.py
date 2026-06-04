import pytest
import hashlib
from Question5 import *

question4_testcases = [
([[10, 20, 20], [10, 10, 10], [20, 10, 20]],'95eed4f6718ed5b7b6822d310c0e3b4b8b15dae8598e53ef577a4e2baeb69693'),
([[10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [80, 80, 80, 80, 80], [60, 60, 60, 60, 60], [70, 70, 70, 70, 70]],'41849a37549a987d1fb395ed0d67c09d5a4b32430cc4c109ce301d32151d4335'),
([[1, 2, 3], [4, 5, 6], [7, 8, 9]],'f75b80dea45e4ae99c9fcdd6db9c6ae4404ff3ce1ab09793ab856186664688da'),
([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],'7af1e9003c25d598c87f6192c311892c6916a751e8a683ed928950cf32815592'),
([[1, 2], [1, 2]],'b5c9692f78a3d180d4d0ca952259cc0bd40dfff2db4b14fd0fc4ebf10c431a46'),
([[1, 5, 61, 35], [4, 3, 2, 74], [10, 11, 100, 42], [48, 7, 65, 27], [81, 200, 9, 99]],'5b403b95455d3bec607f6efd73379f363569c4bdbfa4531f8de61889927725b1'),
([[1, 4, 10, 48, 81], [5, 3, 11, 7, 200], [61, 2, 100, 65, 9], [35, 74, 42, 27, 99]],'3ae09b6cba6f040be210a2809d2d8bcbf3e07a57120be4e858215d41b078cccb')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,result",question4_testcases)
def test_question1(lst1,result):
    assert hashcode(reduce_image(lst1)) == result