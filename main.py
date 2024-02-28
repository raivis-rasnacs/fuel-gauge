"""
CS50 | Fuel gauge
"""

def input_fraction():
    fraction = input("Fraction: ")
    if "/" in fraction:
        x, y = fraction.split("/")
    else:
        raise ValueError("It must be a fraction!")
    return x, y
    
def check_int_validity(fraction):
    x, y = fraction
    try:
        x = int(x)
        y = int(y)
        
        return x, y
    except:
        raise ValueError("Values must be digits")
    
def calculate_percentage(fraction):
    x, y = fraction
    if y == 0:
        raise ZeroDivisionError("Y can not be 0")
    elif x > y:
        raise ValueError("X can not be larger than Y")
    else:
        return round(x/y*100, 0)

def main():
    try:
        fraction = input_fraction()
        valid_fraction = check_int_validity(fraction)
        percentage = calculate_percentage(valid_fraction)
        print(f"{int(percentage)}%")
    except Exception as e:
        print(e)
        main()
    
main()