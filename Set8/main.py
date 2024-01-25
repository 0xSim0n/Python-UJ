import pytest
from rectanglesv2 import Rectangle, Point

def test_point_initialization():
    p = Point(1, 2)
    assert p.x == 1 and p.y == 2

def test_point_get_coordinates():
    p = Point(3, 4)
    assert p.get_coordinates() == (3, 4)

def test_rectangle_initialization():
    r = Rectangle(0, 0, 2, 2)
    assert r.pt1.get_coordinates() == (0, 0) and r.pt2.get_coordinates() == (2, 2)

def test_rectangle_initialization_invalid():
    with pytest.raises(ValueError):
        Rectangle(2, 2, 1, 1)

def test_rectangle_area():
    r = Rectangle(0, 0, 2, 2)
    assert r.area() == 4

def test_rectangle_move():
    r = Rectangle(0, 0, 2, 2)
    r_moved = r.move(1, 1)
    assert r_moved.pt1.get_coordinates() == (1, 1) and r_moved.pt2.get_coordinates() == (3, 3)

def test_rectangle_intersection():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(1, 1, 3, 3)
    r_intersect = r1.intersection(r2)
    assert r_intersect is not None
    assert r_intersect.pt1.get_coordinates() == (1, 1) and r_intersect.pt2.get_coordinates() == (2, 2)

def test_rectangle_no_intersection():
    r1 = Rectangle(0, 0, 1, 1)
    r2 = Rectangle(2, 2, 3, 3)
    assert r1.intersection(r2) is None

def test_rectangle_cover():
    r1 = Rectangle(0, 0, 2, 2)
    r2 = Rectangle(1, 1, 3, 3)
    r_cover = r1.cover(r2)
    assert r_cover.pt1.get_coordinates() == (0, 0) and r_cover.pt2.get_coordinates() == (3, 3)

def test_rectangle_make4():
    r = Rectangle(0, 0, 2, 2)
    rects = r.make4()
    assert len(rects) == 4
    assert all(isinstance(rect, Rectangle) for rect in rects)