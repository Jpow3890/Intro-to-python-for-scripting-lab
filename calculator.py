num1 = int(input("Enter the first number: "))
operator = input("Please enter an operator (=, -, *, /): ")
num2 = int(input("Enter the second number: "))

result = None

if operator == "+":
    result = num1 + num2

elif operator == "-": 
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 // num2

else:
    print("invalid operator")


print(result)



