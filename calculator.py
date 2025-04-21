# Basic Calculator Program with Validation

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

# Get inputs with validation
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = get_operation()

# Perform calculation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
