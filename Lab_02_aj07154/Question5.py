def initialize_matrix(rows, cols):
    return [[0 for i in range(cols)] for j in range(rows)]

def reduce_image(lst):
    row=len(lst)
    col=len(lst[0])
    new_lst=initialize_matrix(row,col)
    for i in range(row):
        for j in range(col):
            new_lst[i][j] = round((lst[i][j] * Sum_helper(lst,i,j,row,col))**(1/3), 3)
            print(Sum_helper(lst,i,j,row,col))
    return new_lst

def Sum_helper(lst,i,j,row,col):
    n1,n2,n3,n4,n5,n6,n7,n8 = 0,0,0,0,0,0,0,0
    if i>0:
        n1=lst[i-1][j]
        if j>0:
            n2=lst[i-1][j-1]
        if j<col-1:
            n3=lst[i-1][j+1]
    if i<row-1:
        n4=lst[i+1][j]
        if j>0:
            n5=lst[i+1][j-1]
        if j<col-1:
            n6=lst[i+1][j+1]
    if j>0:
        n7=lst[i][j-1]
    if j<col-1:
        n8=lst[i][j+1]
    return n1+n2+n3+n4+n5+n6+n7+n8

#print(reduce_image([[10, 20, 30], [30, 10, 20], [20, 0, 30]]))
#print(reduce_image([[12, 29, 32], [15, 1, 46], [79, 11, 44]]))

# solution=[[7.368, 10.627, 9.283], [8.879, 10.627, 9.283], [8.434, 8.879, 8.434]]

# print(reduce_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# solution=[[2.224, 3.362, 3.391], [4.514, 5.848, 5.451], [4.919, 6.283, 5.55]]
