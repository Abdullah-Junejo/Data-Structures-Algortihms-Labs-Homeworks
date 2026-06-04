from HelperFunctions import *

def Question2():
    bst = {}
    str_lst = ["begin", "do", "else", "end", "if", "then", "while"]
    for str in str_lst:
        insert(bst, str)
    print(bst)

## Testing
Question2()

## Expected Output
# {'value': 'begin', 'left': {}, 'right': {'value': 'do', 'left': {}, 'right': {'value': 'else', 'left': {}, 'right': {'value': 'end', 'left': {}, 'right': {'value': 'if', 'left': {}, 'right': {'value': 'then', 'left': {}, 'right': {'value': 'while', 'left': {}, 'right': {}}}}}}}}