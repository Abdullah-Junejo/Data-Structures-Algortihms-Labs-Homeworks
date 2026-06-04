import pytest
import hashlib
from sys import stderr
from Question3 import *

question1_testcases = [
([54, 26, 93, 17, 77, 31, 44, 55, 20],'17ef74dc745853345c313e7703a6eb0cf477e92bc2056c4c5e5c021254727973'),
(["Aisha", "Nadia", "Waqar", "Saleha", "Hasan", "Shahid", "Shah Jamal", "Abdullah", "Umair", "Taj"],'7147882e9d7757b20c12c110fbe8a2453df63be475c0c1d3407ecafec6f82709'),
([4, 1, 3, 9, 7],'ead336dbc13fe37401b6bb995d43307ad560a17a4056d28c3b673b921fe478ea'),
([10, 9, 8, 7, 6, 5, 4, 3, 2, 1],'9167534625dcece55c548a52bb20e77887a219b3fb8e23082b8482c1a99b864a'),
([12, 8, -6, 2, 4, 5, 3, 7, 4, 2],'c2e5afa841c18ec07d40ecca938c512bdb03c83cad2552338fa68eeb621a901f'),
(["FunForFun", "Practice.FunForFun", "FunforFun"],'2f058ed3d930bc0bb7d797e69f708a29b152ab05f988ca81b90fcac4a8598a6c'),
([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54],'df79ea7e62f20a74bd50691406ac29d5daeb2a93ae0dd6a848aabe913b739915'),
([5, 2, 7, 10, 3, 5, 2, 1, 8, 9],'2529fac619ca0215ada6639c39feb4f1d53e0d82f20de358dc12692891fba99a'),
([7, 5, 5, 4, 3, 2, 1],'113f7afdc0fc9049bf7feede893688885f2c02ef5f24722556e391e885c10a2f'),
([2],'038966de9f6b9a901b20b4c6ca8b2a46009feebe031babc842d43690c0bc222b'),
([0, 1, -1],'e5b851fc9277ec870a13985722e20c97d60e5049d9925ee8992a64aec5c8c0eb'),
([0, 1, 2, 3, 9, -1],'fe7e646314fb7d66ac7ce6614e6b810c0227754a8d67a4a9661e9af2a6ac9338'),
([1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 0],'db078c0eb2a88397eca2a5ff53015912603c6a81aeb427391005b1efb8e8a514'),
([71, 32, 22, 19, 18, 1, 15, 40],'211971955d96c47119ea023c499d1587fd63df16a6536fac1399226805f24956')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,result",question1_testcases)
def test_question1(capsys,lst1,result):
    bubble_sort(lst1)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    assert hashcode(captured) == result