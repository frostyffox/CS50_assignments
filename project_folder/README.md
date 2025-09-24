APPS
    #### Video Demo:  <URL HERE>
    #### Description:
    This program simulates a dashboard (such as the Desktop of a pc or the "home screen" of a mobile).
    It prompts the user to choose between 3 apps available to use.
    App 1: a mini-simplified version of Tetris
    App 2: budget manager
    App 3: recursive pattern drawing

    The program terminates if the user uses Ctrl-D
    If the choice is not 1, 2 or 3, the user is re-promoted.

    *****TETRIS:
    Each block can be moved left, right, down
    the user can quite the game with "q"
    mechanism to win/loose:

    ****BUDGET MANAGER:
    Asks for a monthly amount(monthly income) and a current status (student/worker/retired)
    the aim is to provide a recommended partition of the monthky budget, considering the current status (ex: a student will probably save more than a retired person).
    if the amount is quite low or high, there are further adjustments to make sure basic needs are met and to avoid excessive amounts allocated in a category.

    *******RECURSIVE DRAW
    the user is prompted to choose a symbol between ".", "*", "_" and a number between 7 and 16.
    for odd numbers, the program draws a pattern using recursion, where the number is the height and the symbol the basic unit of the pattern. the pattern is a pyramid where the middle line is the longest
    ex: n = 7
    out:
    1: *
    2: **
    3: ***
    4: ****
    5: ***
    6: **
    7: *

    if the chosen number is even, the program will output a square size n x n