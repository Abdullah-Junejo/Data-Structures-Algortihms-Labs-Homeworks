def binary_search_iterative(lst,item):
    left= 0
    right = len(lst) - 1
    mid = 0
    while left <= right:
        mid = (right-left//2)
        mid_index = (left + mid)
        if lst[mid_index] == item:
            return mid_index
        elif lst[mid_index] < item:
            left = mid_index + 1
        else:
            right = mid_index - 1
    return -1

if __name__ == "__main__":
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42],3)) #Output should be -1
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42],17)) #Output should be 5
    