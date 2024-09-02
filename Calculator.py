a=float(input("Enter the first number: "))
b=float(input("Enter the second integer: "))
print("+ -> Addition","- -> Subtraction","* -> Multiplication","/ -> Division",sep="\n")
operator=input("Enter the operator:")
try:
    if operator == '+':
        print(f'{a} + {b} = {a+b}')
    elif operator == '-':
        print(f'{a} - {b} = {a-b}')
    elif operator == '*':
        print(f'{a} * {b} = {a*b}')
    elif operator == '/':
        print(f'{a} / {b} = {a/b}')
    else:
        print("Invalisd operator!!")
except ZeroDivisionError:
    print("Cannot divide with zero , set the value of b to non zero integer")