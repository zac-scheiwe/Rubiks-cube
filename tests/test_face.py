import pytest
from termcolor import colored  # type: ignore
from package.face import Face, ColoredFace

def test_face_coord():
    my_face = Face(2)
    assert my_face.coord == 2
    my_face.switch()
    assert my_face.coord == -2

def test_face_equality():
    my_face = Face(2)
    assert my_face == Face(2)
    assert my_face != Face(3)
    assert my_face == 2

def test_colored_face_coord():
    my_face = ColoredFace(5, "re")
    assert my_face.coord == 5
    assert my_face.color == "R"
    my_face.switch()
    assert my_face.coord == -5

def test_colored_face_equality():
    my_face = ColoredFace(-1, "ora")
    assert my_face == ColoredFace(-1, "O")
    assert my_face != ColoredFace(-1, "b")
    assert my_face != ColoredFace(1, "ora")
    assert my_face == (-1, "O")

def test_invalid_color():
    with pytest.raises(ValueError) as _:
        ColoredFace(2, "lue")

def test_color_printout(capsys):
    my_face = ColoredFace(3, "ye")
    print(my_face)
    captured = capsys.readouterr()
    assert captured.out == colored("██", "yellow")+"\n"
