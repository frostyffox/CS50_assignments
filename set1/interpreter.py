def main():
#prompt for expression in format x y z. and remove white spaces
    exp = input("Expression: ").strip()

    x , sign, y = exp.split()

    if len(exp.split()) != 3:
        print("something's wrong with yoir expression format")

        return

    x_f = float(x)
    y_f = float(y)

    #calculate and return
    if sign == '+':
        print(y_f+x_f)
    elif  sign == '-':
        print(x_f-y_f)
    elif sign == '*':
        print(y_f*x_f)
    elif sign == '/':
        print(x_f/y_f)
    else:
        print("something's wrong with yoir expression format")
main()
