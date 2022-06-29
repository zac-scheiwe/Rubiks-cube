from .face import Face, ColoredFace
from typing import Optional

class Piece:
    """One piece of a Rubik's cube with three faces."""

    @staticmethod
    def get_face(coord: int, color: Optional[str]=None) -> Face:
        if color is None:
            return Face(coord)
        # Else:
        return ColoredFace(coord, color)

    def __init__(self, x_coord: int, y_coord: int, z_coord: int, x_color: Optional[str]=None, y_color: Optional[str]=None, z_color: Optional[str]=None):
        self._x = Piece.get_face(x_coord, x_color)
        self._y = Piece.get_face(y_coord, y_color)
        self._z = Piece.get_face(z_coord, z_color)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def faces(self):
        """Tuple of faces in [x, y, z] order."""
        return (self.x, self.y, self.z)
    
    def __str__(self):
        return sum([face.__str__ for face in self.faces])


