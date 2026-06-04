def sort_matrix_by_columnNumber(matrix, col):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[j][col] < matrix[i][col]:
                matrix[i], matrix[j] = matrix[j], matrix[i]
    return matrix


# #Function call
print(sort_matrix_by_columnNumber([['square', 'rectangle', 'triangle'],['chair','table', 'house'],['motor cycle', 'car', 'truck']], 2))

# #Expected output
# [['chair', 'table', 'house'], ['square', 'rectangle', 'triangle'], ['motor cycle', 'car', 'truck']]