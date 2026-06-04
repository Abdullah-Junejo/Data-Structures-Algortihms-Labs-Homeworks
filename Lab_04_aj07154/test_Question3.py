import pytest
import hashlib
from Question3 import *

question3_testcases = [
    ("()", "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18"),
    ("())", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("{()}", "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18"),
    ("{)({", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("{()}[]()", "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18"),
    ("{[}]", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("()()()([{])}({{[]}})", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("]", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("(){}}{", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("[])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("(])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("([}}])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("[](])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("[", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe"),
    ("[[[[[[(((([{{{{{{[[[[", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe")
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp,result", question3_testcases)
def test_question3(inp, result):
    assert hashcode(balanced_braces(inp)) == result
