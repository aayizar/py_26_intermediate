from __future__ import annotations

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def is_equal(self, p: Point):
        return self.x == p.x and self.y == p.y