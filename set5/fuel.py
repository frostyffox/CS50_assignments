def main():
    while True:
        try:
            fract = input("Fraction: ")
            perc = convert(fract)
            print(gauge(perc))

            break
        except ValueError:
            print("Invalid input.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

def convert(f):
    if "/" not in f:
        raise ValueError("Fraction must contain /")

    x_str, y_str = f.split("/")

    try:
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError("X and Y must be integers")


    if y==0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x < 0 or y < 0:
        raise ValueError("X and Y must be positive")  # explicitly catch negatives
    if x > y:
        raise ValueError("X must be <= Y")
    perc = round((x/y)*100)

    return max(0, min(perc,100))

def gauge(p):
    if p <=1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return f"{p}%"

if __name__ == "__main__":
    main()
