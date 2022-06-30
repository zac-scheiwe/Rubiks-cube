import pytest
from termcolor import colored  # type: ignore
from package.face import Face

def test_coord():
    my_face = Face(5, "mag")
    assert my_face.coord == 5
    assert my_face.color == "M"
    my_face.switch()
    assert my_face.coord == -5

def test_equality():
    my_face = Face(-1, "yel")
    assert my_face == Face(-1, "Y")
    assert my_face != Face(-1, "b")
    assert my_face != Face(1, "wh")
    assert my_face != Face(-1)
    assert my_face == (-1, "Y")

def test_invalid_color():
    with pytest.raises(ValueError):
        Face(2, "lue")
    with pytest.raises(ValueError):
        Face(-1, "O")

def test_color_printout(capsys):
    my_face = Face(3, "ye")
    print(my_face)
    captured = capsys.readouterr()
    assert captured.out == colored("██", "yellow")+"\n"

def test_no_color_printout(capsys):
    my_face = Face(1)
    print(my_face)
    captured = capsys.readouterr()
    assert captured.out == "  "+"\n"

def test_repr():
    my_face = Face(-2, "bl")
    assert repr(my_face) == "(-2, 'B')"