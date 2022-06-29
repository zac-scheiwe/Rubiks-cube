import pytest
from termcolor import colored  # type: ignore
from package.face import Face, ColoredFace

def test_invalid_color():
    with pytest.raises(ValueError) as _:
        ColoredFace(2, "lue")

def test_color_printout(capsys):
    my_face = ColoredFace(3, "ye")
    print(my_face)
    captured = capsys.readouterr()
    assert captured.out == colored("██", "yellow")+"\n"

def test_face_properties():
    my_face = ColoredFace(-1, "wh")
    assert my_face.color == "W"
    assert my_face.coord == -1

def test_face_switch():
    my_face = ColoredFace(5, "re")
    my_face.switch()
    assert my_face.coord == -5
