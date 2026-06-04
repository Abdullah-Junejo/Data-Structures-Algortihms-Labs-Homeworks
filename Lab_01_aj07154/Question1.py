def dot(lst1, lst2):
    # Write your code here
    #Constraint Checking
    if isinstance(lst1, list) and isinstance(lst2,list) and (len(lst1)==len(lst2)):
        if len(lst1)>0:
            a= lst1.pop()
            if not isinstance(a,int):
                 return None
            b= lst2.pop()
            if not isinstance(b,int):
                 return None
            dot_product= a*b
            return dot_product + dot(lst1,lst2)
        else:
              dot_product=0
              return dot_product
    else:
         return None
# DO NOT EDIT
assert  dot([1], [3]) == 3
assert  dot([0, -3, 6], [4, 9, 1]) == -21