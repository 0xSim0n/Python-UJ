from typing import List, Tuple

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def from_points(cls, points: Tuple[Point, Point]):
        return cls(points[0].x, points[0].y, points[1].x, points[1].y)

    def top(self):
        return self.pt2.y

    def left(self):
        return self.pt1.x

    def bottom(self):
        return self.pt1.y

    def right(self):
        return self.pt2.x

    def width(self):
        return self.pt2.x - self.pt1.x

    def height(self):
        return self.pt2.y - self.pt1.y

    def topleft(self):
        return Point(self.left, self.top)

    def bottomleft(self):
        return Point(self.left, self.bottom)

    def topright(self):
        return Point(self.right, self.top)

    def bottomright(self):
        return Point(self.right, self.bottom)

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
