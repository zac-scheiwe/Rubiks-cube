import pytest
from package.face import *

def test_invalid_color():
    with pytest.raises(ValueError) as e_info:
        my_face = Face("A", 1)

def test_face_properties():
    my_face = Face("W", 2)
    assert my_face.color == "W"
    assert my_face.coord == 2

def test_face_printout(capsys):
    my_face = Face("Y", 3)
    print(my_face)
    captured = capsys.readouterr()
    assert captured.out == colored("Y", "yellow")+"\n"