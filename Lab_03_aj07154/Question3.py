from Question1 import *

def Remove(list, index):
    """
    Remove the element at the specified index in the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.
    - index (int): The index of the element to be removed.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Invalid Index" if the provided index is outside the valid range.
                * The valid index range is between 0 and NumberOfElements(list)-1
         - "Element removed successfully" if the removal is successful.

    ** Tip: Try using helper functions created in Q1 where applicable.
    """
    None_Start = NumberOfElements(list) - 1
    if IsEmpty(list):
        return "List is empty"
    if index not in range(0,None_Start+1):
        return "Invalid Index"
    list[index] = None
    #print(None_Start)
    #print(index)
    for i in range(index, None_Start):
        list[i] = list[i + 1]
        continue
    list[None_Start] = None
    return "Element removed successfully"

if __name__ == "__main__":
    lst = [10, 20, 30, 40, 50]
    print(Remove(lst, 2))           # Should print "Element removed successfully"
    print(lst)                      # Should print "[10, 20, 40, 50, None]"
    print()

    print(Remove(lst, 0))           # Should print "Element removed successfully"
    print(lst)                      # Should print "[20, 40, 50, None, None]"
    print()

    print(Remove(lst, 5))           # Should print "Invalid Index"
    print(lst)                      # Should print "[20, 40, 50, None, None]"
    print()

    print(Remove(lst, 3))           # Should print "Invalid Index"
    print(lst)                      # Should print "[20, 40, 50, None, None]"
    print()

    print(Remove(lst, 4))           # Should print "Invalid Index"
    print(lst)                      # Should print "[20, 40, 50, None, None]"
    print()

    ###########################################################################

    lst = Initialize(4)
    print(Remove(lst, 0))           # Should print "List is empty"
    print(lst)                      # Should print "[None, None, None, None]"
    print()
    
    ###########################################################################

    lst = ['a', 'b']
    print(Remove(lst, 0))           # Should print "Element removed successfully"
    print(lst)                      # Should print "['b', None]"
    print()

    ###########################################################################
    
    lst = ['a']
    print(Remove(lst, 0))           # Should print "Element removed successfully"
    print(lst)                      # Should print "[None]"