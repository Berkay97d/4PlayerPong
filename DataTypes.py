from dataclasses import dataclass


@dataclass
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def up():
        return Vector2(0, 1)

    @staticmethod
    def down():
        return Vector2(0, -1)

    @staticmethod
    def left():
        return Vector2(-1, 0)

    @staticmethod
    def right():
        return Vector2(1, 0)

    @staticmethod
    def one():
        return Vector2(1, 1)

    @staticmethod
    def zero():
        return Vector2(0, 0)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __iadd__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __imul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __idiv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def to_tuple(self):
        return self.x, self.y
