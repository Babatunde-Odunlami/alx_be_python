#OOP concepts: creating a robust division calculator
def safe_divide(numerator, denominator):
    try:
        if numerator.isnumeric() and denominator.isnumeric():
            if denominator != 0:
                return float(numerator)/float(denominator)
            else:
                raise ZeroDivisionError("Cannot divide by zero")
        else:
            raise ValueError("both numerator and denominator must be numeric")
    except ValueError:
        print("both numerator and denominator must be numeric")
