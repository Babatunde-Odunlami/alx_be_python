#A calculator based on used input
num1 = float(input("Enter the first number:")
num2 = float(input("Enter the second number:")
    operand = input("Choose the operation (+, -, *, /):")
match operand:
    case "*":
        result = num1 * num2
        break;
    case "+":
        result = num1 + num2
        break;
    case "-":
        result = num1 - num2
        break;
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero")
        break;
    case _:
        print("Please entera valid number")

print("The result is ", result)
