from HelperFunctions import *

def Question1():
    bst = {}

    # Question 1.1
    keys = [68, 88, 61, 89, 94, 50, 4, 76, 66, 82]
    for key in keys:
        insert(bst, key)
    print(bst)

    # Question 1.2
    print(exist(bst, 50))

    # Question 1.3
    print(exist(bst, 49))

    # Question 1.4
    min_node_68 = minimum(bst, 68)
    print(min_node_68)

    # Question 1.5
    min_node_88 = minimum(bst, 88)
    print(min_node_88)

    # Question 1.6
    max_node_68 = maximum(bst, 68)
    print(max_node_68)

    # Question 1.7
    max_node_61 = maximum(bst, 61)
    print(max_node_61)

    # Question 1.8
    inorder_result = []
    inorder_traversal(bst, inorder_result)
    print(inorder_result)

    # Question 1.9
    preorder_result = []
    preorder_traversal(bst, preorder_result)
    print(preorder_result)

    # Question 1.10
    postorder_result = []
    postorder_traversal(bst, postorder_result)
    print(postorder_result)

    # Question 1.11
    successor_76 = successor(bst, 76)
    print(successor_76)


  

## Testing
Question1()

## Expected Outputs
## 1a
#{'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}

## 1b
# True 

## 1c
# False 

## 1d
# {'value': 4, 'left': {}, 'right': {}}

## 1e
# {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}

## 1f
# {'value': 94, 'left': {}, 'right': {}}

## 1g
# {'value': 66, 'left': {}, 'right': {}}

## 1h
# [4, 50, 61, 66, 68, 76, 82, 88, 89, 94]

## 1i
# [68, 61, 50, 4, 66, 88, 76, 82, 89, 94]

## 1j
# [4, 50, 66, 61, 82, 76, 94, 89, 88, 68]

## 1k
# 82