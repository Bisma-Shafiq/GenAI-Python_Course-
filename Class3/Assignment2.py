## Calculator
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
operation = input("Enter the operations(+,-,*,/): ")

if operation=='+':
    print("Output: ",num1+num2)
elif operation=='-':
    print("Output: ",num1-num2)
elif operation=='*':
    print("Output: ",num1*num2)
elif operation=='/':
    print("Output: ",num1/num2)
else:
    print("Operation is Invalid")
