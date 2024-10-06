#OOP concepts: creating a robust division calculator
def safe_divide(numerator, denominator):
    try:
        if float(numerator).isnumeric() and float(denominator).isnumeric():
            if denominator != 0:
                answer = numerator/denominator
                return f"The result of the division is {answer:.1f}"
            else:
                raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            raise ValueError("Error: Please enter numeric values only.")
    except ValueError:
        return f"Error: Please enter numeric values only."
