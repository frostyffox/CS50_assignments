# TEST PROGRAM
# the aim of this script is to test the key functions of my project
# i will use pytest for the testing and sys to raise errors

import sys
import pytest
import myscript as ms

def test_shape_size():
    shape = ["██", "█ "]
    height, width = ms.shape_size(shape)
    assert height == 2
    assert width == 2

def test_place_lock():
    board = [[ms.empty for _ in range(4)] for _ in range(4)]
    shape = ["██"]
    x,y=1,1
    assert ms.placement(board, shape, x,y)
    block = {"shape": shape, "x": x, "y": y}
    ms.lock_block(board, block)
    assert board[1][1] == ms.filled
    assert board[1][2] == ms.filled

def test_finance_student():
    student_budget = ms.budgeting(1000, "s")
    assert "rent/home" in student_budget
    assert sum(m[1] for m in student_budget.values())== 100 #check that the sum of all percentages is 1

def test_low_budget():
    low_budget = ms.budgeting(500, 'w')

    assert low_budget["savings"][0] < 500*0.2
    #since the income is lower than the threshold, 
    # saving % should be < 20%

# testing the function to draw recursively for n even
def test_rec_square(capsys):
    #print("Test for n = 4")
    ms.rec_square("*",4)
    cap = capsys.readouterr()
    output = cap.out.splitlines()
    #assert len(output) == 4
    assert output == ["* * * * "]*4
    #print("\nTest for n = 10")
    ms.rec_square(".",10)
    cap = capsys.readouterr()
    output = cap.out.splitlines()
    #assert len(output) == 10
    assert output == [". . . . . . . . . . "]*10


# testing the function to draw recursively for n odd
def test_rec_odd(capsys):
    ms.rec_odd('_', 5)
    cap = capsys.readouterr()
    output = cap.out.strip().split("\n")
    result = ["_","__","___","__","_"]
    assert output == result

