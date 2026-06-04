def insertion_sort(lst):
    ##  Step 1 − If it is the first element, it is already sorted.
    ##  Step 2 − Pick next element
    i=1
    while i < len(lst):
        X = lst[i]
        j = i - 1
        ##  Step 3 − Compare with all elements in the sorted sub-list
        while j >= 0 and lst[j] > X:
            ##  Step 4 − Shift all the elements in the sorted sub-list that is greater than the value to be sorted
            lst[j + 1] = lst[j] #Right shift
            j -= 1
        ##  Step 5 − Insert the value
        lst[j + 1] = X
        print(lst)
    ##  Step 6 − Repeat until list is sorted
        i+=1


# Function call
insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])


# #Function call
# insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
# #Printed on terminal
# [26, 54, 93, 17, 77, 31, 44, 55, 20]
# [26, 54, 93, 17, 77, 31, 44, 55, 20]
# [17, 26, 54, 93, 77, 31, 44, 55, 20]
# [17, 26, 54, 77, 93, 31, 44, 55, 20]
# [17, 26, 31, 54, 77, 93, 44, 55, 20]
# [17, 26, 31, 44, 54, 77, 93, 55, 20]
# [17, 26, 31, 44, 54, 55, 77, 93, 20]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
    