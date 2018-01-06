from stacks import my_stack

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def dijkstras(expression):
    operands = my_stack([])
    operators = my_stack([])
    ops = '+-*/'
    exp = expression.split()
    for i in exp:
        if (i in ops):
            operators.push(i)
        elif (is_integer(i)):
            operands.push(i)
        elif (i == ')' and not operators.is_empty()):
            oper = operators.pop()
            a = operands.pop()
            b = operands.pop()
            if (oper=='+'):
                operands.push(float(a)+float(b))
                # print(operands)
            elif(oper=='-'):
                operands.push(float(b)-floata)
            elif(oper=='*'):
                operands.push(float(a)*float(b))
            elif(oper=='/'):
                operands.push(float(b)/float(a))
    return operands.top()

expression = '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'
print(dijkstras(expression))
