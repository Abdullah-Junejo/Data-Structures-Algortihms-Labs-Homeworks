from Question1 import *

def Insert(list, index, value):
    """
    Insert the given value at the specified index in the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the value into.
    - index (int): The index at which to insert the value.
    - value: The value to insert into the list.

    Returns:
    str: A string indicating the result of the insertion.
        - "List is full" if the list is already full and no insertion is possible.
        - "Invalid Index" if the provided index is outside the valid range.
                * The valid index range is between 0 and NumberOfElements(list)
        - "Element inserted successfully" if the insertion is successful.

    ** Tip: Try using helper functions created in Q1 where applicable.
    """
    None_Start = NumberOfElements(list)
    if IsFull(list):
        return "List is full"
    if index not in range(0,None_Start+1):
        return "Invalid Index"
    for i in range(None_Start, index,-1):
        list[i]=list[i-1]
    list[index] = value
    return "Element inserted successfully"
    
if __name__ == "__main__":
    lst = Initialize(3)
    
    print(Insert(lst, 0, 'a'))           # Should print "Element inserted successfully"
    print(lst)                           # Should print "['a', None, None]"
    print()

    print(Insert(lst, 2, 'b'))           # Should print "Invalid Index"
    print(lst)                           # Should print "['a', None, None]"
    print()

    print(Insert(lst, 1, 'b'))           # Should print "Element inserted successfully"
    print(lst)                           # Should print "['a', 'b', None]"
    print()

    print(Insert(lst, 4, 'e'))           # Should print "Invalid Index"
    print(lst)                           # Should print "['a', 'b', None]"
    print()

    print(Insert(lst, 2, 'c'))           # Should print "Element inserted successfully"
    print(lst)                           # Should print "['a', 'b', 'c']"
    print()
    
    print(Insert(lst, 3, 'd'))           # Should print "List is full"
    print(lst)                           # Should print "['a', 'b', 'c']"
    print()

    #####################################################################
    
    lst = ['a', 'b', None]
    print(Insert(lst, 1, 'c'))           # Should print "Element inserted successfully"
    print(lst)                           # Should print "['a', 'c', 'b']"
    print()

    #####################################################################

    lst = ['a', 'b', None]
    print(Insert(lst, 0, 'c'))           # Should print "Element inserted successfully"
    print(lst)                           # Should print "['c', 'a', 'b']"
    print()

    #####################################################################

    lst = ['a', 'c', None, None]
    print(Insert(lst, 0, 'b'))           # Should print "Element inserted successfully"
    print(lst)                           # Should print "['b', 'a', 'c', None]"
    print()

    #####################################################################

    lst = ['a', None]
    print(Insert(lst, 0, 'b'))           # Should print "Element inserted successfully"
    print(lst)                           # Should print "['b', 'a']"