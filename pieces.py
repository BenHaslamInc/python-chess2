from __future__ import annotations
import numpy as np

class Piece:
    def __init__(self: Piece) -> None:
        self.coordinates: tuple[int, int] = (0, 0)
        self.symbol = '| P  '
        self.colour = bool(0)


# The Whites

class Pawn (Piece):
    def __init__(self: Pawn) -> None:
        # General pawn rules
        self.symbol = '| ♙  '
        self.colour = 0


class Castle (Piece):
    def __init__(self: Castle) -> None:
        # General Castle rules
        self.symbol = '| ♖  '
        self.colour = 0


class Knight (Piece):
    def __init__(self: Knight) -> None:
        # General Knight rules
        self.symbol = '| ♘  '
        self.colour = 0


class Bishop (Piece):
    def __init__(self: Bishop) -> None:
        # General Bishop rules
        self.symbol = '| ♗  '
        self.colour = 0

class King (Piece):
    def __init__(self: King) -> None:
        # General King rules
        self.symbol = '| ♔  '
        self.colour = 0

class Queen (Piece):
    def __init__(self: Queen) -> None:
        # General Queen rules
        self.symbol = '| ♕  '
        self.colour = 0
    

# The Blacks

class PawnBlack (Pawn):
    def __init__(self: PawnBlack) -> None:
        # Reverse direction
        self.symbol = '| ♟  '
        self.colour = 1

class CastleBlack (Castle):
    def __init__(self: CastleBlack) -> None:
        self.symbol = '| ♜  '
        self.colour = 1

class KnightBlack (Knight):
    def __init__(self: KnightBlack) -> None:
        self.symbol = '| ♞  '
        self.colour = 1

class BishopBlack (Bishop):
    def __init__(self: BishopBlack) -> None:
        self.symbol = '| ♝  '
        self.colour = 1

class KingBlack (King):
    def __init__(self: KingBlack) -> None:
        self.symbol = '| ♚  '
        self.colour = 1

class QueenBlack (Queen):
    def __init__(self: QueenBlack) -> None:
        self.symbol = '| ♛  '
        self.colour = 1