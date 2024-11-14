# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    return a / b  # Potential division by zero error

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

    result = divide_numbers(x, y)
    tetration = tetrate_numers(base, tet, base)
    print(f"The result of division (10/0) is: {result}")
    print(f"The result of tetration (2^^4) is: {tetration}")