
def amount_due():
    due = 50

    while due>0:
        print(f"Amount Due: {due}")
        cash = input("Insert Coin: ")
        coin = int(cash)
        if coin in [25,10,5]:
            due -= coin
        else:
            print("Amount not accepted")
            continue
    print(f"Change Owed: {-due}")

def main():
    amount_due()

main()