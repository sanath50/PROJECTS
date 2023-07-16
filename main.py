#Sudoku solver using python autogui integrated

#import numpy as np
sudokuPuzzleUnsolved =[
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
def checkIfInsertionPossible(x, y, n):
    for i in range(0,9):#To check repeated number in a row
        if sudokuPuzzleUnsolved[i][x]==n and i!=y:
            return False
    for i in range(0,9):#To check repeated number in a column
        if sudokuPuzzleUnsolved[y][i]==n and i!=x:
            return False
    i = (x // 3) * 3
    j = (y // 3) * 3
    for x in range(i,i + 3):#To check repeated numnber in a 3X3 grid
        for y in range(j, j + 3):
            if sudokuPuzzleUnsolved[y][x] == n:
                return False
    return True

def sudokuPuzzleSolved(listOfList):
    for i in range(9):
        print(listOfList[i])
def solveSudokuPuzzle():
    global sudokuPuzzleUnsolved
    for y in range(9):
        for x in range(9):
            if sudokuPuzzleUnsolved[y][x] == 0:
                for n in range(1,10):
                    if checkIfInsertionPossible(x, y, n):
                        sudokuPuzzleUnsolved[y][x]=n
                        solveSudokuPuzzle()
                        sudokuPuzzleUnsolved[y][x]=0
                return
    sudokuPuzzleSolved(sudokuPuzzleUnsolved)
    input('More?')

solveSudokuPuzzle()