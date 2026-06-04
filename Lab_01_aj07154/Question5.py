def minmax(lst):
    if len(lst) == 1: #Base Case
        return tuple((lst[0], lst[0]))
    else: #Main Logic
        minn, maxx = lst[0], lst[0] 
        tup = minmax(lst[1:])
        possible_min = tup[0]
        possible_max = tup[1]
        if minn > possible_min:
            minn = possible_min
        if maxx < possible_max:
            maxx = possible_max
        return tuple((minn, maxx))
# DO NOT EDIT
assert minmax([1]) == (1,1)
assert minmax([0, -3, 6, 4, 9, 1])==(-3,9)