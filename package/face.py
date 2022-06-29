from termcolor import colored  # type: ignore
import os

class Face:

    os.system('color')
    color_names = {"B": "blue", "R": "red", "Y": "yellow",
                    "W": "white", "O": "orange", "G": "green"}

    def __init__(self, color: str, coord: int):
        if color not in Face.color_names.keys():
            raise ValueError("Not a valid color (B,R,Y,W,O,G)")
        
        self._color: str = color
        self._coord: int = coord

    @property
    def color(self):
        return self._color

    @property
    def coord(self):
        return self._coord

    def __str__(self):
        return colored(self._color, Face.color_names[self._color])

    def switch(self):
        self._coord = -self._coord