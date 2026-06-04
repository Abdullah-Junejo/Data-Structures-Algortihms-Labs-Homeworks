import pytest
import hashlib
from Question3 import *

question3_testcases = [
([0, 1, 2, 8, 13, 17, 19, 32, 42], 13, 0, 8,'4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 0, 0, 8,'5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 8, 0, 8,'4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 42, 0, 8,'2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3'),
([0, 1, 2, 8, 13, 17, 19, 32, 42], 0, 0, 0,'5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,item,low,high,result",question3_testcases)
def test_question1(lst,item,result,low,high):
    assert hashcode(binary_search_recursive(lst,item,low,high)) == result
