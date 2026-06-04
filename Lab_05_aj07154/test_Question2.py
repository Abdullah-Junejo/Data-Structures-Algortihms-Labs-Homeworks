import pytest
import hashlib
from sys import stderr
from Question2 import *

question1_testcases = [
([54, 26, 93, 17, 77, 31, 44, 55, 20],'15e585bd4d7ef560e58aa12fa410025ecb35eef709b3702cab72a7fee52bb4ff'),
(["Aisha", "Nadia", "Waqar", "Saleha", "Hasan", "Shahid", "Shah Jamal", "Abdullah", "Umair", "Taj"],'53c2ec840dd0a1fbf8dab99c96d5f570da6fa7e7976572b5c1cbd412a698fc16'),
([4, 1, 3, 9, 7],'c8ad64a47e35e1029fe0e5bb902b13ecb468bd3380597cfa40856074a53eceec'),
([10, 9, 8, 7, 6, 5, 4, 3, 2, 1],'93a0816b46226bdc04f0f1452a45ab34a5a19a8c4204386dfe22473ce1b08f20'),
([12, 8, -6, 2, 4, 5, 3, 7, 4, 2],'48c13279050ec1faa98fc47afad1bc4ee77d37a612c55bd462fe49c201f92d80'),
(["FunForFun", "Practice.FunForFun", "FunforFun"],'58ab6c59741137986f7052f207711b5c91af1abbc2e899774a3b61be6be67f3e'),
([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54],'ee72d76e6e2f05728ebba6dbdad74bedc29854e545c7cde519c37b9b80c07da2'),
([5, 2, 7, 10, 3, 5, 2, 1, 8, 9],'0d01791eb7c76b6c98505c97890ff721bf790dd3da9f1ed3594f1cc719ab9906'),
([7, 5, 5, 4, 3, 2, 1],'af4f9e488658c96b37455be14e5ef85afda38b5192327345b66af03f7e217fd7'),
([0, 1, -1],'c64a7316f0c0f5a95b34595561842dac2df05de71720e7efcb9e38f58f8f49df'),
([0, 1, 2, 3, 9, -1],'8752e80f3066d5353ca5419af042b4520ad65fdaea39edf6e77578d5a3d9c00d'),
([1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 0],'128babfcd962a17e0649e29adcaa0cac232a379fbfd34f8b8090887bc5e11a59'),
([71, 32, 22, 19, 18, 1, 15, 40],'2e005af087ad6733f591a9efb26adf3bd2da99f939e2c6114027e2e3d98aa808')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,result",question1_testcases)
def test_question1(capsys,lst1,result):
    insertion_sort(lst1)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    assert hashcode(captured) == result