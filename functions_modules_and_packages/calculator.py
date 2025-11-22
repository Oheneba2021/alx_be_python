# calculator module 
def add(a ,b):
    return a + b

def subtract(a ,b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    if b == 0:
        return "Error! Cannot divide by zero."
    else:
        return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Cannot compute square root of negative number."
    else:
        return a ** 0.5

def modulus(a, b):
    return a % b    

def floor_divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    else:
        return a // b

def calculate_percentage(part, whole):
    if whole == 0:
        return "Error! Whole cannot be zero."
    else:
        return (part / whole) * 100

def factorial(n):
    if n < 0:
        return "Error! Factorial of negative number doesn't exist."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result   
