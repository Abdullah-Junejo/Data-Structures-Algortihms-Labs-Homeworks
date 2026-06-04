def create_list(size):
    """
    Creates a deque-like data structure with a fixed-size list.

    Parameters:
    - size: The fixed size of the deque.

    Returns:
    A dictionary representing the deque:
    {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }
    """

    return {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }

def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """
    if listADT['n'] == 0:
        return True
    return False


def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """
    if  listADT['n'] == listADT['size']:
        return True
    return False


def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """
    if i < 0 or i >= listADT['n']:
        print("Incorrect Index! Please check again!")
        return
    return listADT['data'][(listADT['i'] + i) % listADT['size']]
    #The Index of data lst would be (listADT['i'] + i) % listADT['size']
    # This is because we need to take into acount the circular nature of fthe queue.
    # lst['i'] would increment decrement based on adding remove
    # We add another i to it to calculate the actual offset
    # we find the remainder of it from size so that we get actual index

def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """
    if i < 0 or i >= listADT['n']:
        print("Incorrect Index! Please check again!")
        return
    listADT['data'][(listADT['i'] + i) % listADT['size']] = e #Using same logic stated above

def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """
    return listADT['n'] #Simply using the dictionary key to get its value


def add(i, e, listADT):
    """
    Adds an element at the specified index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.
    """
    #Basic Error Checking
    if is_full(listADT):
        print("Deque is full")
        return
    if i < 0 or i > listADT['n']:
        print("Incorrect indexe!")
        return
    if i==0:
        insert_first(e,listADT)
        return
    #Main Logic
    for j in range(listADT['n'], i, -1):
        #Shifting elements one place to the right to make space for the new element e
        listADT['data'][(listADT['i'] + j) % listADT['size']] = listADT['data'][(listADT['i'] + j - 1) % listADT['size']]
    listADT['data'][(listADT['i'] + i) % listADT['size']] = e
    listADT['n'] += 1

def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """
    #Error Checking
    if is_empty(listADT):
        print("Empty Deque")
        return
    if i < 0 or i >= listADT['n']:
        print("Incorrect indexe!")
        return
    if i==0:
        remove_first(listADT)
        return
    #Main Logic
    for j in range(i, listADT['n'] - 1):
        #Shifting to left
        listADT['data'][(listADT['i'] + j) % listADT['size']] = listADT['data'][(listADT['i'] + j + 1) % listADT['size']]
    listADT['data'][(listADT['i'] + listADT['n'] - 1) % listADT['size']] = None
    listADT['n'] -= 1

def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    #Basic Error Checking
    if is_full(listADT):
        print("Deque is full")
        return
    last_index_plus_one = (listADT['i'] + listADT['n']) % listADT['size']
    listADT['data'][last_index_plus_one] = e
    listADT['n'] += 1


def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    #Error Checking
    if is_empty(listADT):
        print("Empty Deque")
        return
    last_index = (listADT['i'] + listADT['n'] - 1) % listADT['size']
    element = listADT['data'][last_index]
    listADT['data'][last_index] = None
    listADT['n'] -= 1
    return element


def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        print("Deque is full")
        return

    #Adjusting the starting index for the new element at the front
    listADT['i'] = (listADT['i'] - 1) % listADT['size'] #Moving backwards by one and then calculating actual index
    # If we think about the default case when 'i'=0 now this would become i=4 aka the last index if 'n' = 5
    listADT['data'][listADT['i']] = e
    #Incrementing number of elements
    listADT['n'] += 1


def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    #Basic Error Checking
    if is_empty(listADT):
        print("Empty Deque")
        return

    element_temp_var = listADT['data'][listADT['i']] #To return the pop value
    listADT['data'][listADT['i']] = None
    listADT['i'] = (listADT['i'] + 1) % listADT['size'] #Incrementing 'i' and calculating new index!
    listADT['n'] -= 1
    return element_temp_var


def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """
    if is_empty(listADT):
        print("Empty Deque")
        return
    return listADT['data'][listADT['i']]

def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
    if is_empty(listADT):
        print("Empty Deque")
        return
    return listADT['data'][(listADT['i'] + listADT['n'] - 1) % listADT['size']]


#Testing
listADT = create_list(5)

# Insert elements 1, 2, 3
insert_first(1, listADT)
insert_first(2, listADT)
insert_first(3, listADT)

# Test get_first() and get_last()
assert get_first(listADT) == 3

# Verify length
assert length(listADT) == 3

