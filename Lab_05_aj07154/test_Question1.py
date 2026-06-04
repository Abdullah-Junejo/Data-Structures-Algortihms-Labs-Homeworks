import pytest
import hashlib
from sys import stderr
from Question1 import *

question1_testcases = [
([54, 26, 93, 17, 77, 31, 44, 55, 20],'a75b94b61de6e84faec7674fa4b03d9153052a6b6c7b84d5345771bdfc43cd7e'),
(["Aisha", "Nadia", "Waqar", "Saleha", "Hasan", "Shahid", "Shah Jamal", "Abdullah", "Umair", "Taj"],'16b104558b22fd797fb7a5b456f214fc92839d659c7e27312ef873f31a2dc914'),
([4, 1, 3, 9, 7],'5b1e0514c89c7c9ed6a23422e36c6dfd2fe2e9f952c208452f4f7f076d20dd21'),
([10, 9, 8, 7, 6, 5, 4, 3, 2, 1],'8d27430825622d7996d6a71884d67c32203a3ee9b160640d59dadb133a0937f4'),
([12, 8, -6, 2, 4, 5, 3, 7, 4, 2],'ba129690677206dac411e51e3bc9fae423d110048c229ae40b0fc9ed614582c4'),
(["FunForFun", "Practice.FunForFun", "FunforFun"],'8071b45aae04fa6261ae7c76d929711092fef6ebf32b5940d8da93116bdb0264'),
([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54],'90bc463659241955f236354299232fa015dcb87e7604b0487437196053b4363e'),
([5, 2, 7, 10, 3, 5, 2, 1, 8, 9],'942c7ca6692bd6bf2030173e9c5655afe00d1a7c257aadf5ff2c1c2c45dc5b44'),
([7, 5, 5, 4, 3, 2, 1],'4ac92570c98238809d89a016b7f74510a96b74129cb0ad9ca98445f253a1998f'),
([2],'038966de9f6b9a901b20b4c6ca8b2a46009feebe031babc842d43690c0bc222b'),
([0, 1, -1],'ea65e2f03097ce7085c2b598d3da0f91f364d4bde50413d3fc1a90dc6ffecf02'),
([0, 1, 2, 3, 9, -1],'d3758a8d05775644ddf8c3526ded7f44ff14e65fd6ad328343b56c01a0568b15'),
([1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 0],'9fcdb28ab03fb9e33105a2d2a5e950dadb577d756842b8307e385b7bf359c800'),
([71, 32, 22, 19, 18, 1, 15, 40],'976932b2408bba5a94a78d28db828aaf101f9992e681fe31547cbd62482ae2bb')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,result",question1_testcases)
def test_question1(capsys,lst1,result):
    selection_sort(lst1)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    assert hashcode(captured) == result