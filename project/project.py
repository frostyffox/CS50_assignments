import random

def main():
    print("\n" + "="*40)
    print("Final project for CS50 by Giulia Di Rocco".center(40,"="))
    print("="*40)

    #running the app dashboard
    while True:
        try:
            choice = input("\n\nWelcome to your dashboard\n"
                           "Please coose an app:\n"
                           "1. Tetris\n2. Finance Manager\n3. Draw\n"
                           "Ctrl-D to terminate\n").strip().lower()
        except EOFError:
            print("\Goodbye!")
            break
            
        if choice == "1":
            playTetris()
        elif choice == "2":
            finance()
        elif choice == "3":
            draw()
        elif choice in ["q", "quit", "exit"]: #should not happen but for safety
            print("\Goodbye!")
            break
        else:
            print("Invalid choice.")


#1: MINI TETRIS-LIKE GAME



BLOCKS =[ #storing all my possible block shapes: composed by 1 to 3 blocks
    ["█"],            # 1x1

    ["██"],           # 2x1

    ["█","█"],        # 1x2

    ["███"],          # 3x1

    ["█","█","█"],    # 1x3

    ["██"," █"],      # L-shape

    ["██","█ "],       #j shape

    [" █","██"]       # mirrored L
]

FILLED = "█"
EMPTY = " "

#return the measurements of the shape
def shape_size(shape):
    h = len(shape)
    w = max(len(r) for r in shape)
    return h,w 


def new_block(width):
    shape = random.choice(BLOCKS)
    h,w = shape_size(shape)
    x = width // 2 - w //2
    y = 0
    return {"shape": shape, "x": x, "y": y}

def placement(board, shape, x, y):
    #makes shure every block can be placed with no collision
    height = len(board)
    width = len(board[0])
    for r, row in enumerate(shape):
        for c, col in enumerate(row):
            if col == EMPTY:
                continue
            bx, by = x + c , y + r
            if bx < 0 or bx >= width or by < 0  or by >= height:
                return False
            if board[by][bx] != EMPTY:
                return False
    return True

def lock_block(board, block):
    shape, x, y = block["shape"], block["x"], block["y"]
    for r, row in enumerate(shape):
        for c, col in enumerate(row):
            if col != EMPTY:
                board[y + r][x + c] = FILLED

def drop(board, block):
    x = block["x"]
    y = block["y"]
    shape = block["shape"]

    while placement(board, shape, x, y+1): #make sure y range is valid
        y +=1
    block["y"] = y


def print_board(board, block):
    width = len(board[0])
    height = len(board)

    print("\n" + "-" * (width+2))
    for y in range(height):
        row = list(board[y])

        #when block intersect another, overlay
        bl_top = block["y"]
        bl_bottom = block["y"] + len(block["shape"]) - 1
        if bl_top <= y <= bl_bottom:
            bl_idx = y - bl_top
            block_row = block["shape"][bl_idx]
            for dx, cl in enumerate(block_row):
                if cl != EMPTY:
                    blx = block["x"] + dx
                    if 0 <= blx < width:
                        row[blx] = cl #overlay for now
        print("|" + "".join(row)+ "|")
    print("-" * (width + 2))

def move(board, block, direction):
    x,y = block["x"], block["y"]
    shape = block["shape"]
    if direction == "l":
        nx, ny = x-1, y
    elif direction == "r":
        nx, ny = x+1, y
    elif direction == "d":
        nx, ny = x,y+1
    else:
        return block
    
    if placement(board, shape, nx,ny):
        block["x"], block["y"] = nx, ny
    return block

def playTetris():
    width, height = 10, 12 #init empty board
    board = [[EMPTY for _ in range(width)] for _ in range(height)]

    print("\n"+ "=" * 40)
    print("\nPlay Mini Tetris (Ctrl-D to exit)\n")
    print("Move to left(l), right(r) or down(d). \nPress 'q' to quit".center(40))

    current_block = new_block(width)
    if not placement(board, current_block["shape"], current_block["x"], current_block["y"]):
        print("Game over")
        return
    
    tot_moves = 0

    while True:
        print_board(board, current_block)
        try:
            command = input("Move (l, r, d), quit(q): ").strip().lower()
        except EOFError:
            print("\nExiting Tetris...")
            break

        if command == "q":
            break

        elif command in ["l", "r", "d"]:
            before = (current_block["x"], current_block["y"])
            current_block = move(board, current_block, command)
            after = (current_block["x"], current_block["y"])

            if after != before:
                tot_moves +=1
        else:
            print("Use a valid command")
            continue

        if command == "d" and not placement(board, current_block["shape"], 
                                            current_block["x"], current_block["y"] +1):
            lock_block(board, current_block)
            current_block = new_block(width)
            tot_moves = 0
            if not placement(board, current_block["shape"], current_block["x"], current_block["y"]):
                print_board(board, current_block)
                print("Game over!")
                break
            continue

        if tot_moves >=3: #change block
            drop(board, current_block)
            lock_block(board, current_block)

            current_block = new_block(width)
            tot_moves = 0
            if not placement(board, current_block["shape"], current_block["x"], current_block["y"]):
                print_board(board, current_block)
                print("Game over")
                break
            
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