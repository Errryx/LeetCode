#!/bin/python
import copy
import time

puzzle = [
            [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0]
        ]
PUZZLE_SIZE = len(puzzle[0])

def printPuzzle(puzzleParam):
    i = 0
    j = 0
    print '\n|---|---|---|---|---|---|---|---|---|'
    while i < PUZZLE_SIZE:
        print('|'),
        while j < PUZZLE_SIZE:
            k = puzzleParam[i][j]
            if k == 0:
                print(' '),
            else:
                print(k),
            print('|'),
            j += 1
        i += 1
        j = 0
        print '\n|---|---|---|---|---|---|---|---|---|'

def getRow(i, puzzleParam):
    row = []
    j = 0
    while j < PUZZLE_SIZE:
        row.append(puzzleParam[i][j])
        j += 1
    return row

def getColumn(j, puzzleParam):
    column = []
    i = 0
    while i < PUZZLE_SIZE:
        column.append(puzzleParam[i][j])
        i += 1
    return column

def getCell(i, j, puzzleParam):
    cell = []
    startX = i / 3 * 3
    startY = j / 3 * 3
    count = 0

    while count < PUZZLE_SIZE:
        cell.append(puzzleParam[startX + count / 3][startY + count % 3])
        count += 1
    return cell

def isValid(puzzleParam):
    count = 0
    while count < PUZZLE_SIZE:
        row = getRow(count, puzzleParam)
        if isListValid(row) == False:
            return False
        column = getColumn(count, puzzleParam)
        if isListValid(column) == False:
            return False
        cell = getCell(count / 3 * 3, count % 3 * 3, puzzleParam)
        if isListValid(cell) == False:
            return False
        count += 1
    return True

def isListValid(listParam):
    for x in listParam:
        if x is 0:
            continue
        if listParam.count(x) > 1:
            return False
    return True

def getEmpty(i, j, puzzleParam):
    if puzzleParam[i][j] == 0:
        return [i, j]
    return getNextEmpty(i, j, puzzleParam)

def getNextEmpty(i, j, puzzleParam):
    count = j + 1
    while count < PUZZLE_SIZE:
        if puzzleParam[i][count] == 0:
            return [i, count]
        count += 1

    count = 0
    i += 1
    while i < PUZZLE_SIZE:
        while count < PUZZLE_SIZE:
            if puzzleParam[i][count] == 0:
                return [i, count]
            count += 1
        i += 1
    return None

def feelingLucky(i, j):
    firstEmpty = getEmpty(i, j, puzzle)
    suggestPuzzle = [row[:] for row in puzzle]
    while True:
        suggest = guessEmpty(firstEmpty, suggestPuzzle)
        if suggest > 9:
            return False
        suggestPuzzle[firstEmpty[0]][firstEmpty[1]] = suggest
        if isValid(suggestPuzzle):
            if feelingLuckyRecusive(firstEmpty[0], firstEmpty[1], suggestPuzzle):
                return True
            else:
               continue

def feelingLuckyRecusive(i, j, puzzleParam):
    empty = getNextEmpty(i, j, puzzleParam)
    if empty is None:
        printPuzzle(puzzleParam)
        return True
    suggestPuzzle = [row[:] for row in puzzleParam]
    while True:
        suggest = guessEmpty(empty, suggestPuzzle)
        if suggest > 9:
            return False
        suggestPuzzle[empty[0]][empty[1]] = suggest
        if isValid(suggestPuzzle):
            if feelingLuckyRecusive(empty[0], empty[1], suggestPuzzle):
                return True
            else:
               continue
        else:
           continue

def guessEmpty(empty, puzzleParam):
    return puzzleParam[empty[0]][empty[1]] + 1

startTime = time.time()
printPuzzle(puzzle)
feelingLucky(0, 0)
print (time.time() - startTime)
