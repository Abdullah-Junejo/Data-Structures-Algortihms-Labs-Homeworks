def initialize_matrix(rows,cols):
    return [[0]*cols]*rows

def matrix_subtraction(X, Y):
    Z=Y
    row=len(Y)
    col=len(Y[0])
    if row != len(X) or col!= len(X[0]):
        return "Matrices A and B don't have the same dimension required for matrix subtraction."
    i = 0
    while i < row:
        j=0
        while j<col:
            Z[i][j] = X[i][j] - Y[i][j]
            j+=1
        i+=1
    return Z
    
#print(matrix_subtraction([[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]))
# solution=[[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]

# print(matrix_subtraction([[12,7,3],[4,5,6],[7,8,9]],[[5,8,1],[6,7,3],[4,5,9]]) )
# solution=[[7,-1,2],[-2,-2,3],[3,3,0]]

# print(matrix_subtraction([[1],[1],[1]],[[2],[2],[4]]))
# solution=[[-1],[-1],[-3]]

# print(matrix_subtraction([[1],[2]],[[3,5],[4,6]]))
# solution="Matrices A and B don't have the same dimension required for matrix subtraction."
