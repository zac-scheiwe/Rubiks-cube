from package.face import Face, ColoredFace
from package.piece import Piece

def test_piece_with_one_face():
    my_piece = Piece(1, 4, -3, "re")
    assert my_piece.x == ColoredFace(1, "re")
    assert my_piece.y == Face(4)
    assert my_piece.z == Face(-3)
