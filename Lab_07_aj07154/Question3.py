# Function to perform quicksort

def partition(rectangle_records, low, high, record_title):
    pivot = rectangle_records[low][record_title]  # Select the first element as the pivot
    left,right = low + 1, high  #Selecting first element index followed by the pivot, high remains the same

    while left <= right:  #Loop until the left and right pointers cross
        if rectangle_records[left][record_title] <= pivot:
            left += 1 #Move only if left elements are less than pivot
            continue
        elif rectangle_records[right][record_title] >= pivot:  #Move right pointer to the left if greater than or equal to pivot
            right -= 1
            continue
        else:
            rectangle_records[left], rectangle_records[right] = rectangle_records[right], rectangle_records[left]  #Swap elements at left and right pointers
    rectangle_records[low], rectangle_records[right] = rectangle_records[right], rectangle_records[low]  #Swap the pivot element with the element at the right pointer
    return right 

def quick_sort_rectangles(array, low, high, column):
    if low < high:  
        pi = partition(array, low, high, column)  #Partition the array and get the pivot index in its rightful position
        print(array) 
        quick_sort_rectangles(array, low, pi - 1, column)  
        quick_sort_rectangles(array, pi + 1, high, column) 


# Testing
rectangle_records  = [{"ID":"Rect1","Length": 40 ,"Breadth": 25 ,"Color":"red"} , {"ID":"Rect2","Length":30 ,"Breadth": 20 ,"Color":"blue"} , {"ID":"Rect3","Length": 70 ,"Breadth": 45 ,"Color":"green"} , {"ID":"Rect4","Length": 20 ,"Breadth": 10 ,"Color":"purple"}]
quick_sort_rectangles(rectangle_records, 0, len(rectangle_records)-1, "Length")

# Should print:
# [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]
# [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]