import pytest
from termcolor import colored  # type: ignore
from package.face import Color, Face

def test_invalid_color():
    with pytest.raises(ValueError) as _:
        Color("lue")

def test_color_printout(capsys):
    my_face = Face("yell", 3)
    print(my_face)
    captured = capsys.readouterr()
    assert captured.out == colored("██", "yellow")+"\n"

def test_face_properties():
    my_face = Face("wh", 2)
    assert my_face.color == "W"
    assert my_face.coord == 2

def test_face_switch():
    my_face = Face("re", 1)
    my_face.switch()
    assert my_face.coord == -1
