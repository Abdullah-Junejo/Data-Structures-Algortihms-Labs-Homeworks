def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    return [[None]*n for i in range(n)]  #initializing a matrix with None values*n
    


def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    count=0                              #counting number of non-None values and returns them 
    for item in arr:
        if item is not None:
            count+=1
    return count


def get_maximum(arr: list[int]) -> int:
    """
    A function that takes an array as an argument, and WITHOUT using the built-in functions, returns the maximum value of the array.
    """
    max_val=arr[0]     #returns the maximum value in the list
    for item in arr:
        if item is not None and item>max_val:
            max_val=item
    return max_val


def insertion_sort(arr: list[int]) -> None:
    """
    A void function that takes a single-dimensional array arr as an argument and applies insertion sort on the valid data items in the array, i.e., the non-None values. This is an in-place function, meaning the original array that was passed as a reference will be updated with the sorted values.
     
    The function should not return anything.
    """
    for i in range(1, length(arr)):   #does not return anything however it sorts the list ignoring the None values
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition_and_prevail(arr: list[int]) -> None:
    """
    A void function that takes the array to be sorted as an argument
    and applies the “Partition and Prevail” algorithm to sort the valid
    data items in the array, as explained in the assignment.

    The function should not return anything.
    """
    if not arr:     #checking if array is empty
        return
    
    n=length(arr)  #count the number of not-None elements and if not any then just return
    if n==0:
        return 
    
    max_val=get_maximum(arr)     #get the max value and if max val is None then just return
    if max_val is None:
        return
    
    group=(max_val+1)//n+((max_val+1)%n != 0)   #using the ceiling value logic we calc group size
    matrix=initialize_matrix(n)    

    for item in arr:
        if item is not None:    #if the item is not None
            row=item//group     #calc which row this element will be placed in
            if matrix[row][0] is None:  #if the row has a None then replace it with the item
                matrix[row][0]=item
            else: 
                col=1   #start with the second position in the row
                while matrix[row][col] is not None: #find the next available position and then place the item there
                    col+=1
                matrix[row][col]=item

    for i in range(n):
        insertion_sort(matrix[i])   #applying insertion sort to sort the matrix

    index = 0            # Initialize index for placing elements back into the original array
    for i in range(n):          # Iterate over each row in the matrix
        for j in range(n):       # Iterate over each column in the row
            if matrix[i][j] is not None:  
                arr[index] = matrix[i][j]       # Place the element in the original array
                index += 1                     # Move to the next position in the original array




def main(filename) -> list[int]:
    """
    - Take input from the given filename one line at a time
    - Apply partition_and_prevail sorting algorithm to get the sorted arrays and returns the output as a one dimensional array.
    """
    myFile = open(filename, "r")
    line = myFile.readline()   # Read the first line from the file
    
    line = line[1:-1].split(", ")

    n = length(line)
    
    # Convert the elements from string to int or None as appropriate
    for i in range(n):
        if line[i] == "None":
            line[i] = None  # If the element is the string "None", convert it to the Python None
        else:
            line[i] = int(line[i])  # Otherwise, convert the element to an integer
    
    # Apply the partition_and_prevail sorting algorithm to the array
    partition_and_prevail(line)
    
    # Return the sorted array
    return line
