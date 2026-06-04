def initialize_matrix(rows, cols):
    return [[0 for i in range(cols)] for j in range(rows)]

def matrix_transpose(X):
    row = len(X)
    col = len(X[0])
    Z = initialize_matrix(col, row) 
    i=0
    while i< row:
        j=0
        while j < col:
            Z[j][i] = X[i][j] 
            j+=1
        i+=1
    return Z

print(matrix_transpose([[12,7],[4 ,5],[3 ,8]]))
# solution=[[12, 4, 3],[7, 5, 8]]

# print(matrix_transpose([[12, 4, 3],[7, 5, 8]]))
# solution=[[12,7],[4 ,5],[3 ,8]]

