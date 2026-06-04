import pytest
import hashlib
from Question2 import remove_user

question2_testcases = [
    ({'Alice': ('123-456-7890', ['Bob', 'Charlie']), 'Bob': ('987-654-3210', ['Alice', 'David']), 'Charlie': ('111-222-3333', [
     'Alice']), 'David': ('555-666-7777', ['Bob'])}, 'Alice', '64237bf82a14f2ed8f42ab5233ddf7885e518ba6fbb41e48d0e4ed57193464fc'),
    ({'Alice': ('123-456-7890', []), 'Bob': ('987-654-3210', ['Alice']), 'Charlie': ('111-222-3333', ['Alice']),
      'David': ('555-666-7777', ['Bob'])}, 'Alice', '671c5efd61511be7585e3ba1307c6c459d8850648e296e4d78df26ea6031f97a'),
    ({'Alice': ('123-456-7890', ['Bob']), 'Bob': ('987-654-3210', ['Alice']), 'Charlie': ('111-222-3333', ['Alice']),
      'David': ('555-666-7777', ['Bob'])}, 'Eve', '9893cc4d4ae7166e1f75ccf2e72ef46c91140ccd8b6911a68a7b572bcc6fe666'),
    ({'Alice': ('123-456-7890', ['Bob'])}, 'Alice',
     '44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a'),
    ({'Alice': ('123-456-7890', ['Bob', 'Charlie']), 'Bob': ('987-654-3210', ['Alice', 'David']), 'Charlie': ('111-222-3333', ['Alice',
                                                                                                                               'Bob']), 'David': ('555-666-7777', ['Bob', 'Charlie'])}, 'Alice', '83d5ff55960ba4966581b1eea80380cd6886c80be4899724034ac6592134757e')
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()


@pytest.mark.parametrize("users_data,user_name,result", question2_testcases)
def test_question1(users_data, user_name, result):
    remove_user(users_data, user_name)
    assert hashcode(users_data) == result
