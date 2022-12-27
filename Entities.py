import pygame as pg

from DataTypes import *


class GameObject:

    def __init__(self, screen, name, position, size, color):
        self.screen = screen
        self.name = name
        self.position = position
        self.size = size
        self.velocity = Vector2.zero()
        self.color = color

    def __str__(self):
        f"""{self.name} : {self.position}"""

    def move(self, delta_time):
        self.position += self.velocity * delta_time


class Paddle(GameObject):

    def __init__(self, screen, name, position, size, color, direction, speed):
        super().__init__(screen, name, position, size, color)
        self.direction = direction
        self.speed = speed

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
    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.position.x, self.position.y), self.size)
