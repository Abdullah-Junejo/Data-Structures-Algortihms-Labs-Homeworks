import pytest
import hashlib
from Question5 import RemoveFromStart

remove_from_start_testcases = [
    ([None, None], 'ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a', '48c6c9950ec6c619699a7f00c994bb102585194e43397676eb89b213f00be989'), 
    ([None], 'ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a', '778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2'), 
    (['a', 'b'], 'd8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10', 'a697777b4f89ccfda42a45ebf52795cd8127254bb00727f63eeaf307f17b17dd'), 
    (['a'], 'd8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10', '778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2'),
    ([10, 20, 40, 50, None], 'd8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10', 'b79fab235453230e8ea3fc56ca8afa677cc88c35d916392312ae3998487d5208'),
    ([None, None, None, None], 'ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a', '2023f50b8ba151cd10fdb2a83bd4cf75f645443e9303a516b1a78c90f269a310'),


]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,output,final",remove_from_start_testcases)
def test_RemoveFromStart(list,output,final):
    assert hashcode(RemoveFromStart(list)) == output
    assert hashcode(list) == final