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


    
    