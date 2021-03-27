
from __future__ import annotations

class Game:
    def __init__(self: Game) -> None:
        self.board = get_starting_pieces()

    def over(self: Game) -> bool:
        return False

class Piece:
    def __init__(self: Piece) -> None:
        self.coordinates = (0, 0)
        self.symbol = 'P'

def get_starting_pieces() -> list[Piece]:
    list_of_pieces: list[Piece] = []

    for i in range(8):
        list_of_pieces.append(Piece())

    return list_of_pieces

def print_board(board: list[Piece]) -> None:
    for piece in board:
        print(piece.symbol, end=' ')

game = Game()

while not game.over():
    print_board(game.board)
    break