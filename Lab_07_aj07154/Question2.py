def partition_column(lst, low, high, column):
    pivot = low
    i = low + 1
    for j in range(low + 1, high + 1):
        if lst[j][column] <= lst[pivot][column]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[pivot], lst[i - 1] = lst[i - 1], lst[pivot]
    return i - 1

def partition_mid_column(lst, low, high, column):
    pivot = high
    lst[low], lst[pivot] = lst[pivot], lst[low]
    return partition_column(lst, low, high, column)

def quick_sort_by_column_number(array, low, high, column):
    if low < high:
        pi = partition_mid_column(array, low, high, column)
        print(array)  # Print the array after partitioning
        quick_sort_by_column_number(array, low, pi - 1, column)
        quick_sort_by_column_number(array, pi + 1, high, column)


# Testing
matrix = [['square', 'rectangle', 'triangle'],['chair', 'table', 'house'],['motor cycle', 'car', 'truck']]
quick_sort_by_column_number(matrix, 0, 2, 1)

# Should print:
# [['motor cycle', 'car', 'truck'], ['chair', 'table', 'house'], ['square', 'rectangle', 'triangle']]
# [['motor cycle', 'car', 'truck'], ['square', 'rectangle', 'triangle'], ['chair', 'table', 'house']]

matrix = [[75, 28, 12], [63, 37, 23], [84, 15, 49]]
quick_sort_by_column_number(matrix,0, 2, 1)

# Should print:
# [[84, 15, 49], [63, 37, 23], [75, 28, 12]]
# [[84, 15, 49], [75, 28, 12], [63, 37, 23]]