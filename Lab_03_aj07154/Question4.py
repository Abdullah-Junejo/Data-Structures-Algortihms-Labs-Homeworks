from Question2 import *

def InsertAtStart(list, element):
    """
    Insert the given element at the beginning of the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the element into.
    - element: The element to insert at the start of the list.

    Returns:
    str: A string indicating the result of the insertion.
         - "List is full" if the list is already full and no insertion is possible.
         - "Element inserted successfully" if the insertion is successful.

    ** Tip: You can call Insert function created in Q2.
    """
    return Insert(list, 0, element)


if __name__ == "__main__":
    lst = Initialize(2)
    print(InsertAtStart(lst, 'a'))           # Should print "Element inserted successfully"
    print(lst)                               # Should print "['a', None]"
    print()

    ######################################################

    lst = ['a', 'b']
    print(InsertAtStart(lst, 'c'))           # Should print "List is full"
    print(lst)                               # Should print "['a', 'b']"