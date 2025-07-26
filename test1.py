def function_apply(operation_function,operand1,operand2):
    result=operation_function(operand1,operand2)
    return result

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

result1=function_apply(add,100,400)
result2=function_apply(sub,1000,500)