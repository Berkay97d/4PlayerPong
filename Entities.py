import pygame as pg
from Physics import *
from DataTypes import *


class GameObject:

    def __init__(self, name, position, shape):
        self.collider = None
        self.name = name
        self.position = position
        self.shape = shape
        self.velocity = Vector2.zero()

    def __str__(self):
        return f"""{self.name} : {self.position}"""

    def move(self, delta_time):
        self.position += self.velocity * delta_time
        if self.collider is not None:
            self.collider.center = self.position


class Paddle(GameObject):

    def __init__(self, name, position, shape, direction, speed):
        super().__init__(name, position, shape)
        self.direction = direction
        self.speed = speed
        self.collider = BoxCollider2D(position, shape.size)
        self.score = 0

    def size(self):
        return self.shape.size

    def draw(self):
        self.shape.draw(self.position)

    def move_right(self):
        self.velocity = self.direction * self.speed

    def move_left(self):
        self.velocity = self.direction * -self.speed

    def stop(self):
        self.velocity = Vector2.zero()

    def earn_score(self, score):
        self.score += score


class Ball(GameObject):

    def __init__(self, name, position, shape):
        super().__init__(name, position, shape)
        self.collider = CircleCollider(position, shape.radius)
        self.owner = None

    def draw(self):
        self.shape.draw(self.position)

    def on_hit_paddle(self, paddle):
        direction = (self.position - paddle.position).normalized()
        self.velocity = direction * self.velocity.magnitude()
        self.owner = paddle
        self.shape.color = self.owner.shape.color

    def on_hit_border(self, score):
        if self.owner is None:
            return
        self.owner.earn_score(score)


class Border(GameObject):
    def __init__(self, name, position, shape):
        super().__init__(name, position, shape)
        self.collider = BoxCollider2D(position, shape.size)

    def draw(self):
        self.shape.draw(self.position)


class ScoreBoard(GameObject):
    def __init__(self, name, position, shape):
        super().__init__(name, position, shape)
        self.score = 0

    def draw(self):
        self.shape.draw(self.position, self.score.__str__())
