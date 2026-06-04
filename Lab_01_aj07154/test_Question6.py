import pytest
import hashlib
from Question6 import num_toppings

question6_testcases = [
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},700,'4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},550,'5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},650,'d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},750,'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},800,'2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},850,'19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},900, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},950, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},1000, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5'),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300},400,'5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'),

]
def hashcode(n):
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("prices,budget,result",question6_testcases)
def test_question6(prices,budget,result):
    assert hashcode(num_toppings(prices,budget)) == result