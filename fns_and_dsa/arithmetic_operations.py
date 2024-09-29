# creation of arithmetic operations with 2 variables.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = (
    input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
)

#define a function to for the various arithmetic operations
def perform_operation(num1, num2, operation):
    """function to perform arithmetic operation stated"""
    result = None  #Initialize the reult variable
    if operation == "add":
        result = num1+num2
    elif operation == "subtract":
        result = num1-num2
    elif operation == "multiply":
        result = num1*num2
    elif operation == "divide":
        if num2 == 0:
            return "enter valid numbers as arguments"
        else:
            result = num1 / num2
    else:
        return "please enter a valid operation"
    return f"Result: {result}"

result = perform_operation(num1, num2, operation)
print(result)
