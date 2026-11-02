# question 1
fruits = ["apple" , "banana", "orange","strawberry"]

# for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)

# question 2 while loop creating a countdown from 10 to 1
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1

#question 3 using a for loop with range to print first 10 square numbers
    for i in range(1, 11):
        print(i ** 2)

# question 4  using the random module
import random
colors = ["Black", "Blue", "Red", "Yellow"]

print(random.choice(colors))

# question 5 
import math_operations
print(math_operations.add(5, 3))
print(math_operations.subtract(10, 4))
print(math_operations.multiply(6, 7))
print(math_operations.divide(20, 4))
print(math_operations.divide(10, 0))  # Testing division by zero
print(math_operations.divide(15, 3))
#prints the result of the math operations performed using the functions defined in the math operations module.while it also tests the division by zero to ensure that the error handling is working correctly.

# import custom module and use its functions
import importlib

# It loads custom module import and handle the case where it may not be available
try:
    custom_module = importlib.import_module("custom_module")
except ModuleNotFoundError:
    custom_module = None

if custom_module is not None:
    print(custom_module.custom_function())
else:
    print("custom_module is not available.")

# Simple calculator using a while loop
while True:
    operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")
    if operation.lower() == "q":
        break
    if operation not in ("+", "-", "*", "/"):
        print("Invalid operation.")
        continue
#  Asks the user to input two numbers and performs the selected operation using the  functions defined in the math operations module. it also handles invalid inputs and division by zero errors.
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue
#checks operation and performs the similar operation using the funtions defined in the math operations modules.
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif second_number == 0:
        print("Cannot divide by zero.")
        continue
    else:
        result = first_number / second_number
# Prints the result of the operation to display the text or number result of the operation to the user.
    print("Result:", result)
