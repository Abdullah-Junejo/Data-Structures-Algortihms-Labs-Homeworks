from Question2 import *

# Note:
# 1. You are allowed to make a new queue to store up the results.
# 2. You are not allowed to use stack or list.
# 3. Only Queue ADT Operations are to be used in your implementation ( Initialize() , enqueue() , dequeue() , front() and is_empty() ).

def stutter(A, n):
    Qew=Initialize(Size(A)*n)
    while not is_empty(A):
        frontt=deQueue(A)
        count=0
        while count!=n:
            enQueue(Qew,frontt)
            count+=1
    return Qew

if __name__ == "__main__":
    print(stutter([1, 2, 3], 2))
    # Should print "[1, 1, 2, 2, 3, 3]"

    print(stutter(['a', 'b', 'c'], 3))
    # Should print "['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']"