def Partition(lst, low, high):
    pivot = low  #Set the first element as the pivot
    i = low + 1  #Initializing the index forall elem > pivot
    for j in range(low+1, high+1): 
        if lst[j] <= lst[pivot]:  
            lst[i], lst[j] = lst[j], lst[i]  #Swap the current element at index i
            i += 1  #Increment the index forall elems > pivot
    lst[pivot], lst[i - 1] = lst[i - 1], lst[pivot]  #Swap the pivot element to put at its right position
    pivot = i - 1  #i-1 because i swap was yet to swap but it did not happen as loop terminated 
    return pivot 

def PartitionMid(lst, low, high):
    middle_index_of_lst = (low + high) // 2 
    pivot = middle_index_of_lst  
    lst[low], lst[pivot] = lst[pivot], lst[low]  #Swap the middle element with the first element
    return Partition(lst, low, high)  #Call the Partition function to partition the list and return the pivot index at its rightful position

def quick_sort(array, low, high):
    if low < high:  
        pi = PartitionMid(array, low, high)  #This call moves mid element to first element and then reccursively calculates
        print(array)
        #Divide and conquering the array into small parts so that we rightfully put the 
        #pivot in its place in all these sub arrays. Once all the sub arrays are sorted so is the main array as 
        #its an inplace sortingn algorithm
        quick_sort(array, low, pi - 1)  
        quick_sort(array, pi + 1, high) 
        return
    else:
        return 

# Testing
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)

# Should print:
# [5, 7, 1, 8, 10, 9]
# [1, 5, 7, 8, 10, 9]
# [1, 5, 7, 8, 10, 9]
# [1, 5, 7, 8, 9, 10]