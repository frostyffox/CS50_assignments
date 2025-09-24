#_______OK______
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0

    while True: #continues until ctrl-d
        try:
            #ask for item to add and remove case sensitivity issues
            item = input("Add to order: ").title()

            if item in menu:

                #compute new total
                total += menu[item]

                #display new total
                print(f"Total: $ {total:.2f}")
            


        except EOFError: #user has pressed control-d
            #new line
            print("\n")
            break
if __name__ == "__main__":
    main()
