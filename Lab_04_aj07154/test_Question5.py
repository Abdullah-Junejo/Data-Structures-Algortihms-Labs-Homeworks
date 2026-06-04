import pytest
import hashlib
from Question5 import *

question5_testcases = [
    (

        "( ( ( A + B ) * C ) - ( ( D - E ) * ( F + G ) ) )",
        "c896a19d3f6d6b4685372fe984f989ed59ca54f56e4b92d24a24902efc1fa4af",
    ),
    (
        "( P + Q ) * ( M - N )",
        "0fcf8bf894e8f6454029656c54ece5f62570cabdfa5dc81edb5dc28cf64df32e",
    ),
    (
        "( P + Q ) / ( M - N ) - ( A * B )",
        "0cdff534743663022c3111b18fe502df368851808be917be2c710c4db6a96e21",
    ),
    ("X + Y", "1d3f8bc14474b9b14400fe078381a09c6a9978c83f20e6a30dfd9bdd03b2866c"),
    ("X + Y * Z", "5ef92da34864a8c395b2073619ab25978137fb42d8b4033faf4cac3d6c42a87a"),
    (
        "( X + Y ) * Z",
        "84f9c680888f4bc1b1df04d24e19ce90062b6c0fbe9c72b8ad2ff8ff9f972802",
    ),
    ("A + B * C + D", "4205141e00310a4ecb039bc1fcaf35ea43731e764cf6f8c3de988dba5c8c0527"),
    ("( A + B ) * ( C + D )", "f64def2f01c5aa4d0cd5d8e8b10fa7eac2639365e3c6021aa32f42079c48e771"),
    ("A * B + C * D", "d6cb5342cbde15bb44f7fe42412a8b58f0cb9a4dd602ff1d9ea456a07b12b64a"),
    ("A + B + C + D", "80642afdc7b874b689d126a573654f978b2c46ba7af895467f2d71532fe95bea"),
    ("( A + B ) * C - ( D - E ) * ( F + G )", "c896a19d3f6d6b4685372fe984f989ed59ca54f56e4b92d24a24902efc1fa4af"),
    ("A * B + C", "7ccb5869bfb596fbcb4748a8812f88a3b09e91b6ab4c9642db78ac6b4b178955"),
    ("A * ( B + C )", "db8cb9676b94e3fa855391ba0dff20fd986005861b69c6915621ed44136701fc"),
    ("( A + B ) * C", "f8b44969acd1947d2f085d059d2b610f0d191b712b70f398b17e120bd8c3e2e6"),
    ("a + b * c - ( d / e + f * g * h )", "5e739bb70342522ae258f1b86fcd7b5bbc635d41d08fc19abe69341fdb2956bf")
    ]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp,result", question5_testcases)
def test_question5(inp, result):
    assert hashcode(Infix_to_Postfix(inp)) == result
