def binary_search_recursive(lst, item, low, high):
    if low > high:
        return -1
    mid = (high-low // 2)
    mid_index = low + mid // 2
    
    if lst[mid_index]==item:
        return mid_index
    elif lst[mid_index]<item:
        return binary_search_recursive(lst, item, mid_index + 1, high)
    elif lst[mid_index]>item:
        return binary_search_recursive(lst, item, low, mid_index - 1)
    return



if __name__ == "__main__":
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, 0, 8)) # Output should be -1
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 19, 0, 8)) # Output should be 6