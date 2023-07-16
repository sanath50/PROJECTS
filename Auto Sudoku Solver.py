import pyautogui as pag
import numpy as np
import time

sudokuPuzzleUnsolved = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    sudokuPuzzleUnsolved.append(ints)

    if len(sudokuPuzzleUnsolved) == 9:
        break
    print('Row ' + str(len(sudokuPuzzleUnsolved)) + ' Complete')

time.sleep(1)

def checkIfInsertionPossible(x, y, n):
    for i in range(0, 9):
        if sudokuPuzzleUnsolved[i][x] == n and i != y: # Checks for number (n) in X columns
            return False

    for i in range(0, 9):
        if sudokuPuzzleUnsolved[y][i] == n and i != x: # Checks for number (n) in X columns
            return False

    i = (x // 3) * 3
    j = (y // 3) * 3
    for X in range(i, i + 3):
        for Y in range(j, j + 3):  # Checks for numbers in box(no matter the position, it finds the corner)
            if sudokuPuzzleUnsolved[Y][X] == n:
                return False
    return True

def sudokuPuzzleSolved(solvedPuzzle):
    solvedIntPuzzle = []
    solvedStrPuzzle = []
    for i in range(9):
        solvedIntPuzzle.append(solvedPuzzle[i])

    for lists in solvedIntPuzzle:
        for num in lists:
            solvedStrPuzzle.append(str(num))

    counter = []

    for num in solvedStrPuzzle:
        pag.press(num)
        pag.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pag.hotkey('down')
            for i in range(8):
                pag.hotkey('left')



def solveSudokuPuzzle():
    global sudokuPuzzleUnsolved
    for y in range(9):
        for x in range(9):
            if sudokuPuzzleUnsolved[y][x] == 0:
                for n in range(1, 10):
                    if checkIfInsertionPossible(x, y, n):
                        sudokuPuzzleUnsolved[y][x] = n
                        solveSudokuPuzzle()
                        sudokuPuzzleUnsolved[y][x] = 0
                return
    sudokuPuzzleSolved(sudokuPuzzleUnsolved)

solveSudokuPuzzle()