# Python Calculator

operator = input("Enter an operator: ")
num_one = float(input("Enter the first number: "))
num_two = float(input("Enter the second number: "))

if operator == "+":
    result = num_one + num_two
    print(round(result, 2))
elif operator == "-":
    result = num_one - num_two
    print(round(result, 2))
elif operator == "*":
    result = num_one * num_two
    print(round(result, 2))
elif operator == "/":
    result = num_one / num_two
    print(round(result, 2))
else:
    print(f"{operator} is not valid")