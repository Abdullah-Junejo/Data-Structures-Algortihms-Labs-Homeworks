# StudentDatabase.py

import csv
from HashTable import *

def main(filename):
    student_records = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            student_records.append(row)
    return student_records

def create_studentDatabase(studentRecords):
    size = 7
    hash_table = create_hashtable(size)
    for record in studentRecords:
        hash_table, size = put(hash_table, record['ID'], record, size)
    return hash_table


def perform_Operations(hashtable, operationFile):
    collision_path = {}  # Dictionary to track collision paths
    opNumber = 1  # Operation number for tracking
    
    with open(operationFile, 'r') as file:
        for line in file:
            parts = line.strip().split()
            command = parts[0]
            key = parts[1]
            
            if command == 'Find':
                if len(parts) == 2:
                    columnName = None
                else:
                    columnName = parts[2]
                get(hashtable, key, len(hashtable[0]), collision_path, opNumber)
                
            elif command == 'Update':
                columnName = parts[2]
                data = parts[3]  
                
                Update(hashtable, key, columnName, data, len(hashtable[0]), collision_path, opNumber)
                
            elif command == 'Delete':
                delete(hashtable, key, len(hashtable[0]), collision_path, opNumber)
                
            opNumber += 1  # Increment operation number after each operation

    return collision_path


