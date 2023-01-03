import pygame as pg

import Physics
from Physics import *
from DataTypes import *


class GameObject:

    def __init__(self, screen, name, position, size, color):
        self.collider = None
        self.screen = screen
        self.name = name
        self.position = position
        self.size = size
        self.velocity = Vector2.zero()
        self.color = color

    def __str__(self):
        return f"""{self.name} : {self.position}"""

    def move(self, delta_time):
        self.position += self.velocity * delta_time
        self.collider.center = self.position

    def stay_in_area(self, area_size):
        if self.position.x > area_size.x:
            self.position.x = area_size.x
        if self.position.y > area_size.y:
            self.position.y = area_size.y
        if self.position.x < 0:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = 0


class Paddle(GameObject):

    def __init__(self, screen, name, position, size, color, direction, speed):
        super().__init__(screen, name, position, size, color)
        self.direction = direction
        self.speed = speed
        self.collider = BoxCollider2D(position, size)

    def draw(self):
        half_x, half_y = self.size.x * 0.5, self.size.y * 0.5
        rect = (self.position.x - half_x, self.position.y - half_y, self.size.x, self.size.y)
        pg.draw.rect(self.screen, self.color, rect)

    def move_right(self):
        self.velocity = self.direction * self.speed

    def move_left(self):
        self.velocity = self.direction * -self.speed

    def stop(self):
        self.velocity = Vector2.zero()


class Ball(GameObject):

    def __init__(self, screen, name, position, size, color):
        super().__init__(screen, name, position, size, color)
        self.collider = CircleCollider(position, size)

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.position.x, self.position.y), self.size)

    def on_collision(self, other):
        direction = (self.position - other.position).normalized()
        self.velocity = direction * self.velocity.magnitude()
