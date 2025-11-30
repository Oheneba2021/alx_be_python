def perform_operation(num1,num2,operation):
    '''Performs basic arithmetic operations'''
    if operation == "add":
        return num1 + num2
    if operation == 'subtract':
        return num1 - num2
    if operation == 'multiply':
        return num1 * num2
    if operation == 'divide' and num2 == 0:
        return "Error! Cannot divide by zero"
    if operation == 'divide' and num2 != 0:
        return num1 / num2
    else:
        return "This is not a valid operation"


    
    def perform_operation(num1, num2, operation):
        '''Performs basic arithmetic operations'''

    # Convert input numbers to float
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid input! Please enter numeric values."

    # Perform the operation
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error! Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "This is not a valid operation"


# Main program
if __name__ == "__main__":
    # Prompt user for input
    num1, num2, operation = input("Enter two numbers and an operation (e.g., 5 3 add): ").split()
    
    # Perform calculation and print result
    result = perform_operation(num1, num2, operation)
    print("Result:", result)