# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b != 0:
        return a / b  # Potential division by zero error
    else:
        raise ArithmeticError("Cannot divide by 0.")

def tetrate_numers(a, b, orig):
    """Finds the tetration (repeated exponentiation)
    a^^b and returns the result. Please use small numbers :)"""
    if b == 0 or a == 1:
        return 1
    elif b == 1:
        return a
    else:
        return tetrate_numers(orig**a, b-1, orig)
    

if __name__ == "__main__":
    x = 10
    y = 0

    base = 2
    tet = 4

    try:
        result = divide_numbers(x, y)
        print(f"The result of division is: {result}")
    except ArithmeticError as err:
        print(err)

    tetration = tetrate_numers(base, tet, base)
    print(f"The result of tetration (2^^4) is: {tetration}")

