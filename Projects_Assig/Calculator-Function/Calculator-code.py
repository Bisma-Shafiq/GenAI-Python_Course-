def cal(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "Invalid operation"

# Calling the function
result = cal(
    x=int(input("Enter your 1st number: ")),
    y=int(input("Enter your 2nd number: ")),
    op=input("Enter your operation (+,-,*,/) : ")
)
print("Result of x and y :", result)
