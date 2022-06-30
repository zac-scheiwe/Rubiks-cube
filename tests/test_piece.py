from package.face import Face
from package.piece import Piece

def test_position():
    my_piece = Piece((1, "re"), 4, -3)
    assert my_piece.x == Face(1, "re")
    assert my_piece.y == 4
    assert my_piece.z == -3
    assert my_piece.position == (1, 4, -3)

def test_equality():
    my_piece = Piece((1, "ma"), (-1, "Y"), 2)
    assert my_piece == Piece(Face(1, "M"), Face(-1, "yellow"), Face(2))
    assert my_piece == (Face(1, "M"), Face(-1, "yellow"), Face(2))
    assert my_piece == ((1, "M"), (-1, "Y"), 2)
    assert my_piece != Piece(1, -1, 2)
    assert my_piece != Piece((1, "ma"), (-1, "yel"), (2, "bl"))

