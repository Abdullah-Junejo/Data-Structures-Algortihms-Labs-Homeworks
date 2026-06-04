from Question3 import *

def RemoveFromStart(list):
    """
    Remove the element at the beginning of the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Element removed successfully" if the removal is successful.
    
    ** Tip: You can call Remove function created in Q3.
    """
    return Remove(list,0)


if __name__ == "__main__":
    lst = Initialize(2)
    print(RemoveFromStart(lst))           # Should print "List is empty"
    print(lst)                            # Should print "[None, None]"
    print()
    
    ######################################################

    lst = ['a', 'b']
    print(RemoveFromStart(lst))           # Should print "Element removed successfully"
    print(lst)                            # Should print "["b", None]"