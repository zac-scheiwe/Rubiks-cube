import os
from termcolor import colored  # type: ignore
from typing import Optional

class Face:
    """A colored faced of one piece of a Rubik's cube. Magenta used instead of orange."""

    os.system('color')

    VALID_COLORS: list[str] = ["blue", "red", "yellow", "white", "magenta", "green"]
    
    @staticmethod
    def get_valid_color(color: Optional[str]) -> Optional[str]:
        if color is None:
            return None
        color_len = len(color)
        for valid_color in Face.VALID_COLORS:
            if color.lower() == valid_color[0:color_len].lower():
                return valid_color
        
        # Else:
        raise ValueError("Not a valid color (B,R,Y,W,M,G)")

    def __init__(self, coord: int, color: Optional[str]=None):
        self._coord = coord
        self._color_name = Face.get_valid_color(color)

    @property
    def coord(self):
        return self._coord

    def switch(self):
        self._coord = -self._coord

    @property
    def is_colored(self):
        return self._color_name is not None

    @property
    def color_name(self):
        return self._color_name
    
    @property
    def color(self):
        if self.is_colored:
            return self.color_name[0].upper()
        # Else:
        return None

    def __eq__(self, other) -> bool:
        if isinstance(other, Face):
            return (self.coord == other.coord) and (self.color == other.color)
        if isinstance(other, tuple) and list(map(type, other)) == [int, str]:
            return (self.coord == other[0]) and (self.color == other[1])
        # Else:
        return False
 
    def __repr__(self):
        return f"({self.coord}, '{self.color}')"

    def __str__(self):
        if self.color:
            return colored("██", self.color_name)
        # Else:
        return "  "
   