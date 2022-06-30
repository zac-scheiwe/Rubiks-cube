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
        self._faces = list(map(Piece.get_valid_face, (x,y,z)))

    @property
    def faces(self):
        return tuple(self._faces)

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

    def _flip_axis(self, axis_num: int) -> None:
        self._faces[axis_num].flip()

    def _switch_axes(self, axis_num_1: int, axis_num_2: int) -> None:
        self._faces[axis_num_1], self._faces[axis_num_2] = self._faces[axis_num_2], self._faces[axis_num_1]

    def rotate(self, num_rotations: int, axis: str) -> None:
        """Rotates piece n times around x/y/z axis.

        Args:
            axis (str): Axis of rotation.
            num_rotations (int): Number of clockwise rotations (negative -> anticlockwise).
        """
        axes = ['x', 'y', 'z']
        idx_ignore = axes.index(axis)
        axis_num_1 = (idx_ignore+1) % 3
        axis_num_2 = (idx_ignore+2) % 3
        num_rotations = num_rotations % 4
        match num_rotations:
            case 0:
                pass
            case 1:  # clockwise 90 degrees
                self._switch_axes(axis_num_1, axis_num_2)
                self._flip_axis(axis_num_2)
            case 2:  # 180 degrees
                self._flip_axis(axis_num_1)
                self._flip_axis(axis_num_2)
            case 3:  # anticlockwise 90 degrees
                self._switch_axes(axis_num_1, axis_num_2)
                self._flip_axis(axis_num_1)

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

