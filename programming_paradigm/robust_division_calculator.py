#OOP concepts: creating a robust division calculator
def safe_divide(numerator, denominator):
    try:
        if numerator.isnumeric() and float(numerator) and denominator.isnumeric() and float(denominator):
            if denominator != 0:
                answer =int(numerator)/int(denominator)
                return f"The result of the division is {answer:.1f}"
            else:
                raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            raise ValueError("Error: Please enter numeric values only.")
    except ValueError:
        return f"Error: Please enter numeric values only."
