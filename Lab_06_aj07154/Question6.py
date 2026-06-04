from Question1 import *

def binary_search_nested_list(student_records, ID):
    left = 0 
    right = len(student_records) - 1
    while left <= right:
        mid = (left + right) // 2
        if student_records[mid][0] == ID:
            return mid
        elif student_records[mid][0] < ID:
            left = mid + 1
        elif student_records[mid][0] > ID:
            right = mid - 1
    return -1

def update_record(student_records, ID, record_title, data):
    index = binary_search_nested_list(student_records, ID)
    if record_title == "ID":
        return "ID cannot be updated"
    if index == -1:
        return "Record not found"
    else:
        student_record = student_records[index]
        student_record = list(student_record)  #Because tuple is immutable
        if record_title == "ID":
            return "ID cannot be updated"
        elif record_title == "Email":
            student_record[1] = data
        elif record_title == "Mid1":
            student_record[2] = data
        elif record_title == "Mid2":
            student_record[3] = data
        else:
            return "Invalid record title"
        student_records[index] = tuple(student_record) #Converting back into tuple
        return "Record updated"


if __name__ == "__main__":
    # Output should be [('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)]
    print(update_record([('aa02822', 'ea02822', 80, 65), ('ea02822', 'ea02822@st.habib.edu.pk', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)],'ea02822','Email','updated@gmail.com'))