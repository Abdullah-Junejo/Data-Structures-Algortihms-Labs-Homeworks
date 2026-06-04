from listADT import *

# ** Tip: Try using ListADT helper functions  where applicable.

def push(lst, item):
    Insert(lst,NumberOfElements(lst),item)

def pop(lst):
    topp = top(lst)
    if Remove(lst, NumberOfElements(lst) - 1) == "Element removed successfully":
        return topp

def top(lst):
    return Get(lst,NumberOfElements(lst)-1)

def is_empty(lst):
    return IsEmpty(lst)

if __name__ == "__main__":
    stack = Initialize(5)
    # Initialize a stack of size 5

    print(is_empty(stack))
    # Should print "True"

    push(stack, 1)
    print(stack)
    # Should print "[1, None, None, None, None]"

    push(stack, 2)
    print(stack)
    # Stack should print "[1, 2, None, None, None]"

    print(pop(stack))
    # Should remove the intger 2 from stack and print "2"

    print(top(stack))
    # Should ONLY print "1" which is at the top of the stack

    print(stack)
    # Should print the entire stack which is "[1, None, None, None, None]"