import pytest
import hashlib
from sys import stderr
from Question5 import *

question1_testcases = [
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"ID",'17645408fa5443bca139f64cd28b7982a42404b7b997c90aee51ae601e68ad85'),
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Length",'2e6ab76b9ca1b869b519f37e536fad66ce841da2c4f133bc693a79fbbd5c851b'),
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Breadth",'2e6ab76b9ca1b869b519f37e536fad66ce841da2c4f133bc693a79fbbd5c851b'),
([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Color",'4ea76e4f6d055254266c92f05e87a71e156e0cebd3e4d17c735c7b9788af4e28')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,dimension,result",question1_testcases)
def test_question1(capsys,dimension,lst1,result):
    assert hashcode(sort_rectangles(lst1,dimension)) == result