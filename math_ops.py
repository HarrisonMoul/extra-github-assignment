# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b != 0:
        return a / b  # Potential division by zero error
    else:
        raise ArithmeticError("Cannot divide by 0.")

if __name__ == "__main__":
    x = 10
    y = 0
    try:
        result = divide_numbers(x, y)
        print(f"The result of division is: {result}")
    except ArithmeticError as err:
        print(err)