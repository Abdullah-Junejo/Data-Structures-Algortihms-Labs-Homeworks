from Question1 import *

# Note:
# 1. Only Stack ADT Operations are to be used in your implementation ( Initialize() , push() , pop() , top() and is_empty() ).
# 2. You have to use a SINGLE Stack only.
# 3. You are NOT allowed to use any sort of counter to count number of brackets.
# 4. You are NOT allowed to use any sort of counter to count number of opening and closing brackets.
# 5. Don't use Stack ADT operations on the given string.

def balanced_braces(s):
    stk = Initialize(len(s))
    for char in s:
        if char == '(' or char == '{' or char == '[':
            push(stk,char)
        elif char == ')' or char == '}' or char == ']':
            if is_empty(stk):
                return False
            topp = pop(stk)
            if not match(topp,char):
                return False
    return is_empty(stk)

#Helper

def match(topp,char):
    if topp == '(':
        topp = ')'
    elif topp == '{':
        topp = '}'
    elif topp == '[':
        topp = ']'
    if topp==char:
        return True
    else:
        return False
        

if __name__ == "__main__":
    print(balanced_braces("()"))
    # Should print "True"

    print(balanced_braces("())"))
    # Should print "False"

    print(balanced_braces("{()}"))
    # Should print "True"

    print(balanced_braces("{)({"))
    # Should print "False"

    print(balanced_braces("{()}[]()"))
    # Should print "True"

    print(balanced_braces("{[}]"))
    # Should print "False"