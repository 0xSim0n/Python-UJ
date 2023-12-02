import unittest
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1.get_coordinates() == other.pt1.get_coordinates() and \
               self.pt2.get_coordinates() == other.pt2.get_coordinates()

    def __ne__(self, other):
        return not self == other

    def center(self):
        x = (self.pt2.x + self.pt1.x) / 2
        y = (self.pt2.y + self.pt1.y) / 2
        return Point(x, y)

    def area(self):
        x = self.pt2.x - self.pt1.x
        y = self.pt2.y - self.pt1.y
        return x * y

    def move(self, x, y):
        new_pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        new_pt2 = Point(self.pt2.x + x, self.pt2.y + y)
        return Rectangle(new_pt1.x, new_pt1.y, new_pt2.x, new_pt2.y)

    def intersection(self, other):
        x_overlap = max(0, min(self.pt2.x, other.pt2.x) - max(self.pt1.x, other.pt1.x))
        y_overlap = max(0, min(self.pt2.y, other.pt2.y) - max(self.pt1.y, other.pt1.y))

        if x_overlap > 0 and y_overlap > 0:
            intersection_rect = Rectangle(
                max(self.pt1.x, other.pt1.x),
                max(self.pt1.y, other.pt1.y),
                max(self.pt1.x, other.pt1.x) + x_overlap,
                max(self.pt1.y, other.pt1.y) + y_overlap
            )
            return intersection_rect
        else:
            return None

    def cover(self, other):
        cover_rect = Rectangle(
            min(self.pt1.x, other.pt1.x),
            min(self.pt1.y, other.pt1.y),
            max(self.pt2.x, other.pt2.x),
            max(self.pt2.y, other.pt2.y)
        )
        return cover_rect

    def make4(self):
        mid_x = (self.pt1.x + self.pt2.x) / 2
        mid_y = (self.pt1.y + self.pt2.y) / 2
        smaller_rect1 = Rectangle(self.pt1.x, self.pt1.y, mid_x, mid_y)
        smaller_rect2 = Rectangle(mid_x, self.pt1.y, self.pt2.x, mid_y)
        smaller_rect3 = Rectangle(self.pt1.x, mid_y, mid_x, self.pt2.y)
        smaller_rect4 = Rectangle(mid_x, mid_y, self.pt2.x, self.pt2.y)
        return smaller_rect1, smaller_rect2, smaller_rect3, smaller_rect4


class TestRectangles(unittest.TestCase):
    def test_invalid_rectangle_coordinates(self):
        with self.assertRaises(ValueError):
            invalid_rectangle = Rectangle(3, 4, 1, 2)

    def test_move(self):
        rectangle = Rectangle(1, 2, 3, 4)
        moved_rectangle = rectangle.move(2, 3)
        self.assertEqual(moved_rectangle, Rectangle(3, 5, 5, 7))

    def test_center(self):
        rectangle = Rectangle(1, 2, 5, 6)
        center_point = rectangle.center()
        expected_center = Point(3.0, 4.0)
        self.assertTrue(math.isclose(center_point.x, expected_center.x, abs_tol=1e-10))
        self.assertTrue(math.isclose(center_point.y, expected_center.y, abs_tol=1e-10))

    def test_area(self):
        rectangle = Rectangle(0, 0, 3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_intersection(self):
        rectangle1 = Rectangle(1, 1, 4, 4)
        rectangle2 = Rectangle(3, 3, 6, 6)
        intersection = rectangle1.intersection(rectangle2)
        self.assertEqual(intersection, Rectangle(3, 3, 4, 4))

    def test_cover(self):
        rectangle1 = Rectangle(1, 2, 3, 4)
        rectangle2 = Rectangle(0, 1, 4, 5)
        covering_rect = rectangle1.cover(rectangle2)
        self.assertEqual(covering_rect, Rectangle(0, 1, 4, 5))

    def test_make4(self):
        rectangle = Rectangle(0, 0, 4, 4)
        smaller_rectangles = rectangle.make4()
        expected_result = (
            Rectangle(0, 0, 2.0, 2.0),
            Rectangle(2.0, 0, 4.0, 2.0),
            Rectangle(0, 2.0, 2.0, 4.0),
            Rectangle(2.0, 2.0, 4.0, 4.0)
        )
        self.assertEqual(smaller_rectangles, expected_result)


if __name__ == '__main__':
    unittest.main()
