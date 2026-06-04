def score(grid, n):
    # Write your code here
    sum =0
    i,j=0,0
    while i <n and j < n:
        elem = grid[i][j]
        # print("elem:",elem)
        if j<n-1 and elem == grid[i][j+1]:
            sum+=elem*2
        # print(sum)
        if j<n:
            j+=1
        if j==n:
            i+=1
            if i<n:
                j=0
        if i==n:
            break

    ## Vertical Check
    i,j=0,0
    while i <n and j < n:
        elem= grid[i][j]
        # print("elem:",elem)
        if i < n-1 and elem == grid[i+1][j]:
            sum+=elem*2
        # print(sum)
        if j<n:
            j+=1
        if j==n:
            i+=1
            if i<n:
                j=0
        if i==n:
            break

    #Diagonal
    i,j=0,0
    while i <n and j < n:
        elem= grid[i][j]
        # print("elem:",elem)
        if i < n-1 and j < n-1 and elem == grid[i+1][j+1]:
            sum+=elem*2
        # print(sum)
        if j<n:
            j+=1
        if j==n:
            i+=1
            if i<n:
                j=0
        if i==n:
            break
    #Diagonal check 2
    i,j=0,0
    while i <n and j < n:
        elem= grid[i][j]
        # print("elem:",elem)
        if i > 0 and j<n-1 and elem == grid[i-1][j+1]:
            sum+=elem*2
        # print(sum)
        if j<n:
            j+=1
        if j==n:
            i+=1
            if i<n:
                j=0
        if i==n:
            break
    return sum
# DO NOT EDIT
n = 5
grid = [[12, 21, 36, 36, 11], [12, 32, 19, 36, 12], [71, 11, 17, 17, 34], [62, 17, 49, 53, 16], [62, 39, 18, 49, 16]]
assert score(grid,n) == 562
