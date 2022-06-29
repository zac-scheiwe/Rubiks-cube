from termcolor import colored  # type: ignore
import os

class Face:
    """A face of one piece on a Rubik's cube."""

    def __init__(self, coord: int):
        self._coord: int = coord

    @property
    def coord(self):
        return self._coord

    def switch(self):
        self._coord = -self._coord

    def __eq__(self, other) -> bool:
        if isinstance(other, Face):
            return self.coord == other.coord
        # Else:
        return False

    def __repr__(self):
        return self.coord

class ColoredFace(Face):
    """A colored face of one piece of a Rubik's cube."""

    os.system('color')

    VALID_COLORS: list[str] = ["blue", "red", "yellow", "white", "orange", "green"]
    
    @staticmethod
    def get_valid_color(color: str) -> str:
        color_len = len(color)
        for valid_color in ColoredFace.VALID_COLORS:
            if color.lower() == valid_color[0:color_len].lower():
                return valid_color
        
        # Else:
        raise ValueError("Not a valid color (B,R,Y,W,O,G)")

    def __init__(self, coord: int, color: str):
        Face.__init__(self, coord)
        self._color_name = ColoredFace.get_valid_color(color)
    
    @property
    def color_name(self):
        return self._color_name
    
    @property
    def color(self):
        return self.color_name[0].upper()

    def __eq__(self, other) -> bool:
        if Face.__eq__(self, other):
            if isinstance(other, ColoredFace):
                return (self.color == other.color)
        # Else:
        return False

    def __str__(self):
        return colored("██", self.color_name)
    
    def __repr__(self):
        return (self.coord, self.color)
