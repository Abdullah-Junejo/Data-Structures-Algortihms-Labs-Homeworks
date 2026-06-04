def Initialize(n):
    """
    Create and return a new list of size n,
    with all elements initialized to None.

    Parameters:
    - n (int): The size of the list.

    Returns:
    list: A new list with n elements, all set to None.
    """
    arr = [None for i in range (n) ]
    return arr

def Get(list, index):
    """
    Retrieve the element at the specified index in the list.

    Parameters:
    - list (list): The list to retrieve the element from.
    - index (int): The index of the element to retrieve.

    Returns:
    The element at the specified index in the list.
    """
    return list[index]

def Set(list, index, value):
    """
    Set the element at the specified index in the list to the given value.

    Parameters:
    - list (list): The list to modify.
    - index (int): The index at which to set the value.
    - value: The value to set at the specified index.

    Returns:
    None
    """
    list[index]  = value
    

def Size(list):
    """
    Get the size of the list.

    Parameters:
    - list (list): The list to determine the size of.

    Returns:
    int: The size of the list.
    """
    for i in range(len(list)):
        continue
    return i+1


def NumberOfElements(list):
    """
    Get the number of elements in the list.

    Parameters:
    - list (list): The list to count elements in.

    Returns:
    int: The number of elements in the list.

    ** Tip : Break the loop when you find the first None value.
    """
    count=0
    for i in range(len(list)):
        if list[i]!=None:
            count+=1
    return count

def IsEmpty(list):
    """
    Check if the list is empty.

    Parameters:
    - list (list): The list to check.

    Returns:
    bool: True if the list is empty, False otherwise.
    """
    for i in range(len(list)):
        if list[i]!=None:
            return False
    return True
    

def IsFull(list):
    """
    Check if the list is full.

    Parameters:
    - list (list): The list to check.

    Returns:
    bool: True if the list is full, False otherwise.
    """
    for i in range(len(list)):
        if list[i]==None:
            return False
    return True


if __name__ == "__main__":
    lst = Initialize(5)
    print(lst)
    # Should print "[None, None, None, None, None]"

    Set(lst, 0, 10)
    print(lst)
    # Should print "[10, None, None, None, None]"

    print(Get([10, None, None, None, None], 0))
    # Should print "10"

    print(Size([10, None, None, None, None]))
    # Should print "5"

    print(NumberOfElements([10, None, None, None, None]))
    # Should print "1"

    print(IsEmpty([10, None, None, None, None]))
    # Should print "False"
    
    print(IsFull([10, None, None, None, None]))
    # Should print "False"