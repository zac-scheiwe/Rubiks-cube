from .face import Face
from typing import Union

class Piece:
    """One piece of a Rubik's cube with three faces."""

    def __init__(self, x: Union[tuple, Face], y: Union[tuple, Face], z: Union[tuple, Face]):
        self._faces = tuple([f if isinstance(f, Face) else Face(*f) for f in [x,y,z]])

    @property
    def faces(self):
        return self._faces

    @property
    def x(self):
        return self.faces[0]

    @property
    def y(self):
        return self.faces[1]

    @property
    def z(self):
        return self.faces[2]

    @property
    def position(self):
        return tuple([f.coord for f in self.faces])

    @property
    def colors(self):
        """Tuple of colours in [x, y, z] order."""
        return tuple([f.color for f in self.faces])

    def __repr__(self):
        return self.faces.__repr__

    def __str__(self):
        return " ".join([f.__str__() for f in self.faces])


