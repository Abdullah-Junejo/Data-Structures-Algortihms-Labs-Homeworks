from Question1 import *

# Note:
# 1. Only Stack ADT Operations are to be used in your implementation ( Initialize() , push() , pop() , top() and is_empty() ).
# 2. Use Stack ADT operations on the Stack only.
#
# Infix to Postfix Conversion Simulator: https://raj457036.github.io/Simple-Tools/prefixAndPostfixConvertor.html

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def is_operand(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z'

def Infix_to_Postfix(expression):
    operator = Initialize(len(expression))  #Operator stack
    output = Initialize(len(expression))    #Output stack
    for char in expression:
        #print("Operator Stack:", operator)
        #print("Output Stack:", output)
        if char == ' ': #Empty Space check
            continue
        if is_operand(char):
            push(output, char) #Operand push
        elif char == '(':
            push(operator, char) #Paranthesis Push
        elif char == ')':   #Pushing Operator Stack into output stack for the range of entire paranthesis
            while not is_empty(operator) and top(operator) != '(':
                push(output, pop(operator))
            pop(operator)  #pop the opening '(' from stack
        else: #Dealing with Operators
            while not is_empty(operator) and precedence(top(operator)) >= precedence(char):
                push(output, pop(operator))
            push(operator, char)
    #Expression Loop Ends, so we have to emmpty the operator stack now
    while not is_empty(operator): #Emptyingg Operator stack
        push(output, pop(operator))

    #Converting result into string
    result = ''
    while not is_empty(output):
        result=str(pop(output)) + ' ' + result
    return result[:-1]

if __name__ == "__main__":
    print(Infix_to_Postfix("( A + B ) * ( C + D )"))
    # Should print "A B + C D + *"

    print(Infix_to_Postfix("A * B + C * D"))
    # Should print "A B * C D * +"

    print(Infix_to_Postfix("A * B + C"))
    # Should print "A B * C +"

    print(Infix_to_Postfix("A * ( B + C )"))
    # Should print "A B C + *"

    print(Infix_to_Postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # Should print "A B + C * D E - F G + * -"