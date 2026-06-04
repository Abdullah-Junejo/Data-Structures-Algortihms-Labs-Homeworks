import hashlib
import pytest
from Question3 import update_record

question3_testcases = [
    ([("E001", "Manager", 80000, 5), ("E002", "Developer", 60000, 2), ("E003", "Analyst", 50000, 1),
        ("E004", "Designer", 70000, 3)], "E001", "ID", "E005",
        '8c0f5197a938f5b322033e2cc3ca340cd84836c05e6bac81f0cee118f01f6403',
        '504cb64ef6cc46b6f83fd0fd7f75e2888941efe72f691f42ef998c130fdc1e99'),
    ([("E001", "Manager", 80000, 5), ("E002", "Developer", 60000, 2), ("E003", "Analyst", 50000, 1),
        ("E004", "Designer", 70000, 3)], "E001", "Position", "Senior Manager",
        'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1',
        '3d0dec314f9ef335c5a40adb0d7d316c9d4b855e431105c283a30403a61c3ceb'),
    ([("E001", "Manager", 80000, 5), ("E002", "Developer", 60000, 2), ("E003", "Analyst", 50000, 1),
        ("E004", "Designer", 70000, 3)], "E005", "Salary", 55000,
        '60de363f36743d355c615af8528d592aa944790b679331bd6fa8c066b8f9ba6e',
        '504cb64ef6cc46b6f83fd0fd7f75e2888941efe72f691f42ef998c130fdc1e99'),
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1),
        ('E004', 'Designer', 70000, 3)], "E002", "Position", "Senior Developer",
        'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1',
        'a9c62581871405dedc65f53b1bb491e2ed5ab23c60ae764fda4fbc13b1c22844'),
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1),
        ('E004', 'Designer', 70000, 3)], "E003", "Salary", 55000,
        'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1',
        '03ebd9d2420df9865ff9381a1227f7b945ee943377adb00d6b7c85c8db76eb3e'),
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1),
        ('E004', 'Designer', 70000, 3)], "E004", "Experience", 4,
        'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1',
        '99efa1fb0f8011c6db98c5f68903857fd11b0b8e4373d27d62b59aba9624abfe'),
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1),
        ('E004', 'Designer', 70000, 3)], "E003", "ID", "E005",
        '8c0f5197a938f5b322033e2cc3ca340cd84836c05e6bac81f0cee118f01f6403',
        '504cb64ef6cc46b6f83fd0fd7f75e2888941efe72f691f42ef998c130fdc1e99'),
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1),
        ('E004', 'Designer', 70000, 3)], "E005", "Position", "Senior Developer",
        '60de363f36743d355c615af8528d592aa944790b679331bd6fa8c066b8f9ba6e',
        '504cb64ef6cc46b6f83fd0fd7f75e2888941efe72f691f42ef998c130fdc1e99')
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()


@pytest.mark.parametrize("employee_records, ID, record_title, data,result1, result2", question3_testcases)
def test_question3(employee_records, ID, record_title, data, result1, result2):
    assert hashcode(update_record(employee_records,
                                  ID, record_title, data)) == result1
    assert hashcode(employee_records) == result2
