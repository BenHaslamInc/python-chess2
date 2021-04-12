import numpy as np


def ValidateNInput(N: str) -> int:
    if not N in ['1', '2', '3', '4', '5', '6', '7', '8']:
        raise ValueError('Must input a number between 1 and 8')

    return int(N) - 1


def ValidateLInput(L: str) -> int:
    L = L.upper()
    allowedLValues = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    if not L in allowedLValues:
        raise ValueError('Must input a letter between A and H')

    return allowedLValues.index(L)


def MoveLetter():

    while True:
        try:
            return ValidateLInput(input('Select a square A-H: '))

        except ValueError as e:
            print(e)


def MoveNumber():
    while True:
        try:
            return ValidateNInput(input('Select a square 1-8: '))

        except ValueError as e:
            print(e)


def taken(output, turn, game):
    for piece in game.board:
        (X, Y) = piece.coordinates
        if (X, Y) == output:
            if piece.colour == turn:
                print('You already have a piece there, try again!')
                return 0
            else:
                if turn == 0:
                    game.taken_blacks.append(piece)
                    game.board.remove(piece)
                else:
                    game.taken_whites.append(piece)
                    game.board.remove(piece)

                return 1
