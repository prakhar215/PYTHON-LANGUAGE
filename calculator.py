def calculator(a,b,operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation =='*':
        return a*b
    elif operation == '/':
        if b!=0:
            return a/b
        else:
            return "Error Division by zero"
    else:
        return "INVALID OPERATION"
num1=float(input("Enter First number:"))
num2=float(input("Enter Second number:"))
oper=input("Enter opertation (+ - * /)")

result=calculator(num1,num2,oper)
print("The result is :",result)