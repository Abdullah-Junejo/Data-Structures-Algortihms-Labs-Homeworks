import pytest
import hashlib
from Question4 import *

# Note the Graphs used in the test cases is not
# the same as the graphs in the previous questions
question4_testcases = [
    ("{'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}", 1, "3a316d6d3226f84c1e46e4447fa8d5fd800bff4a1bc6498152523cd4a602b69b"),
    ("{'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}", 2, "3c818f8f77fcc64ac49eedf48fcdfd63fc8243dd77988461309bb9a35e92ce2f"),
    ("{'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}", 3, "589ffd3acf522ae81192579f297589e93b0c41f748b224d1b4bb5c857a2f70cb"),
    ("{'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)], 'Austin': [('Houston', 160), ('Chicago', 900)], 'Washington': [('Atlanta', 600)], 'Denver': [], 'Atlanta': [], 'Chicago': [], 'Houston': []}", 1, "c77fa14ab16aa0567db77adc833c3d1597b05da993b6c00a272d20bb12ec9ce6"),
    ("{'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)], 'Austin': [('Houston', 160), ('Chicago', 900)], 'Washington': [('Atlanta', 600)], 'Denver': [], 'Atlanta': [], 'Chicago': [], 'Houston': []}", 2, "1110d76afaf0f25d9ffcdcbe6a185e7766739da63926c891bf360e3e7ee5662c"),
    ("{'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)], 'Austin': [('Houston', 160), ('Chicago', 900)], 'Washington': [('Atlanta', 600)], 'Denver': [], 'Atlanta': [], 'Chicago': [], 'Houston': []}", 3, "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"), 
    ("{'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'JFK': [('DFW', 1)], 'MIA': [('LAX', 1), ('ORD', 1)], 'SFO': [], 'ORD': [], 'DFW': [], 'LAX': [('MAX', 1), ('HAX', 1)], 'HAX': [], 'MAX': []}", 1, "8d7c73da8d28a59bcba24359cfaf5aa3302edc857ba0ba727edd9c893b4ca16b"),
    ("{'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'JFK': [('DFW', 1)], 'MIA': [('LAX', 1), ('ORD', 1)], 'SFO': [], 'ORD': [], 'DFW': [], 'LAX': [('MAX', 1), ('HAX', 1)], 'HAX': [], 'MAX': []}", 2, "2451fb44c2c4dcd6e76d61f5efa45cebb1cb945db8e6a48995f0b593621bc4f1"),
    ("{'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'JFK': [('DFW', 1)], 'MIA': [('LAX', 1), ('ORD', 1)], 'SFO': [], 'ORD': [], 'DFW': [], 'LAX': [('MAX', 1), ('HAX', 1)], 'HAX': [], 'MAX': []}", 3, "33c3278b0b171033998c129d3d3b4cfc04ec0a177497144b02108d90e38d6602"), 
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp,start,result", question4_testcases)
def test_question4(inp, start, result):
    assert hashcode(nodes_of_level(eval(inp), start)) == result