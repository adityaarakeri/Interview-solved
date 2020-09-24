#!/usr/bir/#!/usr/bin/#!/usr/bin/env python
"""
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.
Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.
The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
 my code
 """
 
 def validateBattlefield(field):
    ships = {}
    for row in range(len(field[0])):
        for col in range(len(field)):
            if field[row][col] == 1:
                try:
                    result = getShipSize(row, col, field)
                    ships[result] = ships.get(result, 0) + 1
                except ValueError:
                    return False
    return ships.get(4, 0) == 1 and ships.get(3, 0) == 2 and ships.get(2, 0) == 3 and ships.get(1, 0) == 4


def isCornerValid(row, col, field):
    if row == len(field) - 1:
        return True
    if col == 0:
        return field[row + 1][col + 1] != 1
    if col == len(field[0]) - 1:
        return field[row + 1][col - 1] != 1
    return field[row + 1][col + 1] != 1 and field[row + 1][col - 1] != 1


def isSideValid(row, col, field):
    if row == len(field) - 1 or col == len(field[0]) - 1:
        return True
    return not (field[row + 1][col] != 0 and field[row][col + 1] != 0)


def isValidPoint(row, col, field):
    return isCornerValid(row, col, field) and isSideValid(row, col, field)


def getShipSize(row, col, field):
    if not isValidPoint(row, col, field):
        raise ValueError('Invalid disposition')
    field[row][col] = -1
    if row != len(field) and field[row + 1][col] == 1:
        return 1 + getShipSize(row + 1, col, field)
    if col != len(field[0]) and field[row][col + 1] == 1:
        return 1 + getShipSize(row, col + 1, field)
    return 1
