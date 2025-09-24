def main():
    greet = input("Greet the customer: ").lower().strip()
    fee = value(greet)
    print(f"the bank ower the customer {fee} $")


def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
    


if __name__ == "__main__":
    main()
