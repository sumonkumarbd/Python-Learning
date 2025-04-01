
print("\n $$$Functions$$$ \n")

### Function ###
## Characteristics of Function
# - Code Reusability
# - Modular Approach
# - Can Have Parameters
# - Can Return Values
# - Increases Readability

def greet(name):
    # Function to greet a person
    print(f"Hello, {name}!")

def add(a, b):
    # Function to add two numbers
    return a + b

def is_even(number):
    # Function to check if a number is even
    return number % 2 == 0

print(add(5, 3))  # Output: 8
print(is_even(10))  # Output: True

## Some useful function concepts
# - Default Parameters
# - *args (Variable-Length Arguments)
# - **kwargs (Keyword Arguments)
# - Lambda Functions
# - Recursion

# Function with default parameter
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()  # Output: Welcome, Guest!
welcome("Sumon")  # Output: Welcome, Sumon

# Function with *args (multiple arguments)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Function with **kwargs (keyword arguments)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Bristi", age=23, city="Dhaka")

# Lambda function
square = lambda x: x * x
print(square(6))  # Output: 36

mylamFunc = lambda num,num2: num * num2
print(mylamFunc(2,3)) # Output: 6

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120