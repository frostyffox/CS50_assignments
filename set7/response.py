from validators import email

def main():
    #
    s_email = input("Email address: ").strip()
    if validate(s_email):
        print("Valid")
    if not validate(s_email):
        print("Invalid")

def validate(s):
    return bool(email(s))
if __name__ == "__main__":
    main()
