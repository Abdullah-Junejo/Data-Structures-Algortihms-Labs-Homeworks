from Question1 import *

def finding_multiple(lst, item):
    index = binary_search_iterative(lst, item)
    if index == -1:
        return []
    else:
        index_lst = []
        index_lst.append(index)
        left = index - 1

        #Two Linear Searches to count insert dupplicatess.
        while left >= 0 and lst[left] == item:
            index_lst.insert(0,left)
            left -= 1
        right = index + 1
        while right <= len(lst)-1 and lst[right] == item:
            index_lst.append(right)
            right += 1

        return index_lst

if __name__ == "__main__":
    print(finding_multiple([0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42], 17)) # Output should be [5, 6, 7, 8]
    print(finding_multiple([0, 1, 2, 8, 13, 17 ,17 , 17 ,17, 19, 32, 42], 34)) # Output should be []