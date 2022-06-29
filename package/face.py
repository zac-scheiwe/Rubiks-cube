from termcolor import colored  # type: ignore
import os

class Color:
    """A color of a face on a Rubik's cube."""

    VALID_COLORS: list[str] = ["blue", "red", "yellow", "white", "orange", "green"]
    
    @staticmethod
    def get_valid_color(color: str) -> str:
        color_len: int = len(color)
        for valid_color in Color.VALID_COLORS:
            if color.lower() == valid_color[0:color_len].lower():
                return valid_color
        
        # Else not a valid color:
        raise ValueError("Not a valid color (B,R,Y,W,O,G)")

    def __init__(self, color: str):
        self._color = Color.get_valid_color(color)
    
    @property
    def color_name(self):
        return self._color
    
    @property
    def color(self):
        return self.color_name[0].upper()

    def __str__(self):
        return colored("██", self.color_name)


class Face(Color):
    """A face of one piece on a Rubik's cube."""

    os.system('color')

    def __init__(self, color: str, coord: int):
        Color.__init__(self, color)
        self._coord: int = coord

    @property
    def coord(self):
        return self._coord

    def __repr__(self):
        return colored(f"({self.coord})", self.color_name)

    def switch(self):
        self._coord = -self._coord