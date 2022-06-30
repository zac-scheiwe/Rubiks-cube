from .face import Face
from typing import Union

class Piece:
    """One piece of a Rubik's cube with three faces."""

    FaceType = Union[Face, int, tuple]

    @staticmethod
    def get_valid_face(f: FaceType) -> Face:
        if isinstance(f, Face):
            return f
        if isinstance(f, int):
            return Face(f)
        if Face.is_valid_tuple(f):
            return Face(*f)
        # Else:
        raise ValueError("Not a valid face (int, color_str)")

    def __init__(self, x: FaceType, y: FaceType, z: FaceType):
        self._faces = tuple(map(Piece.get_valid_face, (x,y,z)))

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

    def __eq__(self, other):
        if isinstance(other, Piece):
            return self.faces == other.faces
        if isinstance(other, tuple) and len(other) == 3:
            return all([s == o for (s, o) in zip(self.faces, other)])
        # Else:
        return False

    def __repr__(self):
        return "("+ ", ".join(map(repr, self.faces)) + ")"

    def __str__(self):
        return " ".join([f.__str__() for f in self.faces])

