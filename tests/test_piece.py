from package.face import Face
from package.piece import Piece
from pytest import fixture

@fixture
def my_piece():
    yield Piece((2, "whit"), 1, (-3, "bl"))

class TestPiece:

    def test_attributes(self):
        my_piece = Piece((1, "re"), 4, -3)
        assert my_piece.x == Face(1, "re")
        assert my_piece.y == 4
        assert my_piece.z == -3
        assert my_piece.position == (1, 4, -3)
        assert my_piece.colors == ("R", None, None)

    def test_equality(self):
        my_piece = Piece((1, "ma"), (-1, "Y"), 2)
        assert my_piece == Piece(Face(1, "M"), Face(-1, "yellow"), Face(2))
        assert my_piece == (Face(1, "M"), Face(-1, "yellow"), Face(2))
        assert my_piece == ((1, "M"), (-1, "Y"), 2)
        assert my_piece != Piece(1, -1, 2)
        assert my_piece != Piece((1, "ma"), (-1, "yel"), (2, "bl"))

    def test_no_rotation(self, my_piece):
        my_piece.rotate(-4, "x")
        assert my_piece.position == (2, 1, -3)
        assert my_piece.colors == ("W", None, "B")

    def test_rotation_clockwise(self, my_piece):
        my_piece.rotate(5, "x")
        assert my_piece.position == (2, -3, -1)
        assert my_piece.colors == ("W", "B", None)

    def test_rotation_180_degrees(self, my_piece):
        my_piece.rotate(10, "y")
        assert my_piece.position == (-2, 1, 3)
        assert my_piece.colors == ("W", None, "B")

    def test_rotation_anticlockwise(self, my_piece):
        my_piece.rotate(-1, "y")
        assert my_piece.position == (-3, 1, -2)
        assert my_piece.colors == ("B", None, "W")