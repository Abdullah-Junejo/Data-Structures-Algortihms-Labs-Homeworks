import pytest
import hashlib
from Question2 import Insert

insert_testcases = [
    ([None, None, None], 0, 'a', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '9bf4b5c1d663646e15eac5a644ee42b0b90740ebbf4afd76cfe061e66fe6c9a9'), 
    (['a', None, None], 1, 'b', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '26da2835afd041f34ebfc5a8e7a0582421933402fe77cd3fba8a23aedbbb6833'), 
    (['a', 'b', None], 2, 'c', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '8b7bff6e4f868e026388803fa14914c21d7e63da6197cdec8e88d75e7b3218bb'), 
    (['a', 'b', None], 4, 'e', 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', '26da2835afd041f34ebfc5a8e7a0582421933402fe77cd3fba8a23aedbbb6833'), 
    (['a', 'b', None], -1, 'e', 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', '26da2835afd041f34ebfc5a8e7a0582421933402fe77cd3fba8a23aedbbb6833'), 
    (['a', 'b', 'c'], 3, 'd', '71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5', '8b7bff6e4f868e026388803fa14914c21d7e63da6197cdec8e88d75e7b3218bb'),
    (['a'], 0, 'b', '71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5', 'a326618a43c0b61aff497f4d8a82f4857fe952c5fae156ab94facf4adbf7dcb4'),
    (['a', 'b', None], 1, 'c', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '5bc0f06b18e2e7604a5465c2b334c99aec1f98d8bc579a85e4d6de61e6c33572'),
    (['a', 'b', None], 0, 'c', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', 'e98d25fa1ba65a6e1efcfdab966486e42daff252bc6d7564bddf2942b4a56ace'),
    (['a', 'c', None, None], 0, 'b', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', '3ac714c130c93025dd2e80be5544952c351e30b51c88e5bf3d3d2c6e7892f783'),
    (['a', None], 0, 'b', '134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5', 'f9c31f7e1418d5930e9d8fc48189670976826b4cea4b7aa6a3c2db491e1533c7'),
    (['a', None, None], 2, 'e', 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', '9bf4b5c1d663646e15eac5a644ee42b0b90740ebbf4afd76cfe061e66fe6c9a9'),
    (['a', None, None, None], 3, 'e', 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', '3b9fdb455eb6b4d933856a76287a3559fad3fd7fac58afae2c11c716ad864382'),
    (['a', None, None, None], 2, 'e', 'a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128', '3b9fdb455eb6b4d933856a76287a3559fad3fd7fac58afae2c11c716ad864382')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,index,element,output,result",insert_testcases)
def test_Insert(list,index,element,output,result):
    assert hashcode(Insert(list,index,element)) == output
    assert hashcode(list) == result