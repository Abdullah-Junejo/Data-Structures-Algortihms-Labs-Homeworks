def selection_sort(lst):
    i=0
    ##    Step 5 − Repeat until list is sorted 
    while i<len(lst):
        minn =i
    ##    Step 2 − Search the minimum element in the list
        for j in range(minn,len(lst)):
            if lst[j]<lst[minn]:
                minn=j
    ##    Step 3 − Swap with value at location MIN
        if minn!=i:
            lst[i],lst[minn]=lst[minn],lst[i]
        print(lst)
    ##    Step 4 − Increment MIN to point to next element
        i+=1

# #function call
# selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
# #Printed on terminal
# [17, 26, 93, 54, 77, 31, 44, 55, 20]
# [17, 20, 93, 54, 77, 31, 44, 55, 26]
# [17, 20, 26, 54, 77, 31, 44, 55, 93]
# [17, 20, 26, 31, 77, 54, 44, 55, 93]
# [17, 20, 26, 31, 44, 54, 77, 55, 93]
# [17, 20, 26, 31, 44, 54, 77, 55, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
    