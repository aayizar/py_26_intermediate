from src.domain.Point import Point

class Snake:
    def __init__(self) -> None:
        self.body: list[Point] = []
        self.dx = 1
        self.dy = 0