import random

def main():
    print("Final project for CS50 by Giulia Di Rocco")
    while True:
        try:
            choice = input("\n\nWelcome to your dashboard. \nPlease coose an app:\n1. Tetris\n2. Finance Manager\n3. Draw\nCtrl-D to terminate\n")
        except EOFError:
            print("\Goodbye!")
            break
            
        if choice == "1":
            playTetris()
        elif choice == "2":
            finance()
        elif choice == "3":
            draw()
        else:
            print("Invalid choice.")


#1: MINI TETRIS-LIKE GAME
def playTetris():
    width, height = 10, 5
    board = [[" " for _ in range(width)] for _ in range(height)]
    print("\nStarting Mini Tetris (Ctrl-D to exit)\n")

    current_block = {"x": width // 2, "y": 0, "char": "█"}

    while True:
        print_board(board, current_block)
        try:
            move = input("Move block: left(l), right(r), down(d), quit(q): ").strip()
        except EOFError:
            print("\nExiting Tetris...")
            break

        if move == "q":
            break
        elif move in ["l", "r", "d"]:
            current_block = move_block(board, current_block, move)
            if current_block["y"] >= height - 1:
                # Lock block
                board[current_block["y"]][current_block["x"]] = current_block["char"]
                current_block = {"x": width // 2, "y": 0, "char": "█"}  # spawn new block
        else:
            print("Invalid input. Use l, r, d, or q.")


def print_board(board, block):
    for y in range(len(board)):
        row = ""
        for x in range(len(board[0])):
            if y == block["y"] and x == block["x"]:
                row += block["char"]
            else:
                row += board[y][x]
        print("|" + row + "|")
    print("-" * (len(board[0]) + 2))


def move_block(board, block, direction):
    width = len(board[0])
    height = len(board)
    x, y = block["x"], block["y"]

    if direction == "l" and x > 0 and board[y][x-1] == " ":
        x -= 1
    elif direction == "r" and x < width - 1 and board[y][x+1] == " ":
        x += 1
    elif direction == "d" and y < height - 1 and board[y+1][x] == " ":
        y += 1

    return {"x": x, "y": y, "char": block["char"]}

#2: FINANCIAL MANAGER
#input: amount ($) -> monthly income; condition("status"): student/worker/retired
#returns a suggested partition of the monthly income, both in % and $
#takes into account the amount and the condition
def finance():
    try:
        amount = float(input("Enter monthly income: "))
    except ValueError:
        print("Invalid Amount")
        return
    
    while True:
        status = input("Select your current MAIN status: \nstudent= s, worker= w, retired= r\n").strip().lower()
        if status in ["s","w","r"]:
            break
        else: 
            print("Invalid choice. Please enter s, w or r")

    budget = budgeting(amount, status)
    print_budget(budget)

#evaluates and computes partition
def budgeting(a, status):
    if status == "s":
        parts = {"rent/home": 0.3, "food": 0.25, "free time": 0.15, "savings": 0.2, "investment": 0.1}
    elif status == "w":
        parts = {"rent/home": 0.35, "food": 0.2, "hobbies": 0.15, "savings": 0.2, "investment": 0.1}
    elif status == "r":
        parts = {"rent/home": 0.25, "food": 0.3, "hobbies": 0.1, "savings": 0.2, "investment": 0.15}
    else:
        print("Unknown condition. Using default percentages.")
        parts = {"rent": 0.3, "food": 0.25, "hobbies": 0.15, "savings": 0.2, "investment": 0.1}

    # Adjust percentages if amount is very low
    if a < 1000:
        parts["savings"] *= 0.5
        parts["food"] += 0.1

    budget = {}
    #categories and percentages
    for cat, perc in parts.items():
        money = round(a * perc, 2)
        perctg = int(perc * 100)
        budget[cat] = (money, perctg)
    return budget



def print_budget(budget):
    print("__RECOMMENDED BUDGET ALLOCATION__\n")
    for k, (val, perc) in budget.items():
        print(f"** {k.capitalize()}: ${val} ({perc}%)")
        #print("\n")



#3: DRAWING A PATTERN GIVEN A SYMBOL AND A NUMBER, USING RECURSION
def draw():
    symbol = input("Choose a symbol: . or _ or *\n").strip()
    if symbol not in [".", "_", "*"]:
        print("Invalid symbol")
        return
    try:
        n = int(input("Enter pattern size: (between 1 and 10):\n"))
    except ValueError:
        print("Invalid height")
        return
    if n < 1 or n> 10:
        print("Pick a nub=mber between 1 and 10")
        return
    print("\Pattern: \n")
    rec_draw(symbol, n)

#DRAWS A PATTERN GIVEN A SIMBOL AND A SIZE(int between 1 and 10 incl.)
def rec_draw(symbol, n):
    if n == 0:
        return
    print(symbol*n)
    rec_draw(symbol, n-1)


#MAIN CTRL
if __name__ == "__main__":
    main()