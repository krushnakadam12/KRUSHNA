def apply_function(operation_function,operand1,operand2):
    result=operation_function(operand1,operand2)
    return result

def add(x,y):
    return x + y

def sub (a,b):
    return a + b

result1=apply_function(add,100,200)
result2=apply_function(sub,500,50)