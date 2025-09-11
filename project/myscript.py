import random


#______MAIN______
# runs the main dashboard

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

filled = "█"
empty = " "

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
            if col == empty:
                continue


            bx, by = x + c , y + r
            if bx < 0 or bx >= width or by < 0  or by >= height:
                return False
            if board[by][bx] != empty:
                return False
    return True

def lock_block(board, block):
    shape, x, y = block["shape"], block["x"], block["y"]
    for r, row in enumerate(shape):
        for c, col in enumerate(row):
            if col != empty:
                board[y + r][x + c] = filled

def drop(board, block):
    x = block["x"]
    y = block["y"]
    shape = block["shape"]

    while placement(board, shape, x, y+1): #make sure y range is valid
        y +=1
    block["y"] = y


#visualisation of the board with "updated moves"
#board is a list of rows
#each row is a list of characters
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
                if cl != empty:
                    blx = block["x"] + dx
                    if 0 <= blx < width:
                        row[blx] = cl #overlay for now
        print("|" + "".join(row)+ "|")
    print("-" * (width + 2))

# the user moves the block
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

#runs the whole game
def playTetris():
    width, height = 5, 4 #init empty board
    board = [[empty for _ in range(width)] for _ in range(height)]

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

#if the symbol or the pattern size aentered are not valid > re-prompt
#after the pattern has been correctly drawn: go back to main menu
def draw():
    while True:
        symbol = input("Choose a symbol: . or _ or *\n").strip()
        if symbol not in [".", "_", "*"]:
            print("Invalid symbol")
            continue
        break

    while True:
        try:
            #i choose a range of n so that the drawing looks good enough
            n = int(input("Enter pattern size (between 7 and 16 -included-):\n"))
        except ValueError:
            print("Invalid height")
            continue
        if n < 7 or n> 16:
            print("Pick a nubmber between 7 and 16")
            continue
        break
    print("\Pattern: \n")
    if n%2 == 1:
        rec_odd(symbol,n)
    else:
        rec_square(symbol,n)

    

#DRAWS A PATTERN GIVEN A SIMBOL AND A SIZE

#for odd numbers, i draw a pyramid of n lines
#ex: 7
#half = 4
#if l> 7: return
#if l>4 -> second part of the pyramid
#if l<= 4: -> first part of the pyramid
def rec_odd(symbol, n, l=1):
    if l > n:
        return
    half = (n + 1) // 2  # middle line
    if l <= half:
        count = l
    else:
        count = n - l + 1
    print(symbol * count)
    rec_odd(symbol, n, l + 1) #implement the recursion here, modifying l value to go on in the lines


#for even numbers, i draw a square
def rec_square(symbol, n):
    
    for _ in range(n):
        print((symbol+" ")*n)
    



#MAIN CTRL
if __name__ == "__main__":
    main()