from listADT import *

# ** Tip: Try using ListADT helper functions  where applicable.

def enQueue(lst, item):
    Insert(lst,NumberOfElements(lst),item)

def deQueue(lst):
    frontt=front(lst)
    if RemoveFromStart(lst) == "Element removed successfully":
        return frontt

def front(lst):
    return Get(lst,0)

def is_empty(lst):
    return IsEmpty(lst)

if __name__ == "__main__":
    Queue = Initialize(5)
    # Initialize a queue of size 5

    print(is_empty(Queue))
    # Should print "True" as Queue is empty

    enQueue(Queue, 5)
    print(Queue)
    # Should print "[5, None, None, None, None]"

    print(is_empty(Queue))
    # Should print "False" as Queue is non-empty

    enQueue(Queue, 7)
    print(Queue)
    # Should print "[5, 7, None, None, None]"

    print(front(Queue))
    # Should print "5"

    print(deQueue(Queue))
    # Should print "5"

    print(Queue)
    # Should print "[7, None, None, None, None]"

    print(front(Queue))
    # Should print "7"

    deQueue(Queue)
    print(Queue)
    # Should print "[None, None, None, None, None]"
