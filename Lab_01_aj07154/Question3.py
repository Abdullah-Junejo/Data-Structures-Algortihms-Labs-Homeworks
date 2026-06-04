def update_record(employee_records, ID, record_title, data):
    # Write your code here
    if record_title == "ID":
        return "ID cannot be updated"
    elif record_title == "Position":
        record_index = 1
    elif record_title == "Salary":
        record_index = 2
    elif record_title == "Experience":
        record_index = 3
    else:
        return "Record not found"

    for i, tup in enumerate(employee_records):
        if tup[0] == ID:
            lst = list(tup)
            lst[record_index] = data
            employee_records[i] = tuple(lst)
            return "Record updated"
    return "Record not found"

# DO NOT EDIT  
employee_records = [
    ("E001", "Manager", 80000, 5),
    ("E002", "Developer", 60000, 2),
    ("E003", "Analyst", 50000, 1),
    ("E004", "Designer", 70000, 3)
]
assert update_record(employee_records, "E001", "ID", "E005") == "ID cannot be updated"
assert update_record(employee_records, "E001", "Position", "Senior Manager") == "Record updated"
assert update_record(employee_records, 'E005', "Salary", 55000) == "Record not found"


