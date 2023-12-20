import pytest
from rectangles import Rectangle, Point
import math


def test_invalid_rectangle_coordinates():
    with pytest.raises(ValueError):
        invalid_rectangle = Rectangle(3, 4, 1, 2)


def test_move():
    rectangle = Rectangle(1, 2, 3, 4)
    moved_rectangle = rectangle.move(2, 3)
    assert moved_rectangle == Rectangle(3, 5, 5, 7)


def test_center():
    rectangle = Rectangle(1, 2, 5, 6)
    center_point = rectangle.center()
    expected_center = Point(3.0, 4.0)
    assert math.isclose(center_point.x, expected_center.x, abs_tol=1e-10)
    assert math.isclose(center_point.y, expected_center.y, abs_tol=1e-10)


def test_area():
    rectangle = Rectangle(0, 0, 3, 4)
    assert rectangle.area() == 12


def test_intersection():
    rectangle1 = Rectangle(1, 1, 4, 4)
    rectangle2 = Rectangle(3, 3, 6, 6)
    intersection = rectangle1.intersection(rectangle2)
    assert intersection == Rectangle(3, 3, 4, 4)


def test_cover():
    rectangle1 = Rectangle(1, 2, 3, 4)
    rectangle2 = Rectangle(0, 1, 4, 5)
    covering_rect = rectangle1.cover(rectangle2)
    assert covering_rect == Rectangle(0, 1, 4, 5)


def test_make4():
    rectangle = Rectangle(0, 0, 4, 4)
    smaller_rectangles = rectangle.make4()
    expected_result = (
        Rectangle(0, 0, 2.0, 2.0),
        Rectangle(2.0, 0, 4.0, 2.0),
        Rectangle(0, 2.0, 2.0, 4.0),
        Rectangle(2.0, 2.0, 4.0, 4.0)
    )
    assert smaller_rectangles == expected_result
