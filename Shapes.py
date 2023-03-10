import pygame


class Shape:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color


class Circle(Shape):
    def __init__(self, screen, color, radius):
        super().__init__(screen, color)
        self.radius = radius

    def draw(self, center):
        pygame.draw.circle(self.screen, self.color, (center.x, center.y), self.radius)


class Rect(Shape):
    def __init__(self, screen, color, size):
        super().__init__(screen, color)
        self.size = size

    def draw(self, center):
        half_x, half_y = self.size.x * 0.5, self.size.y * 0.5
        rect = (center.x - half_x, center.y - half_y, self.size.x, self.size.y)
        pygame.draw.rect(self.screen, self.color, rect)


class Text(Shape):
    def __init__(self, screen, color, font):
        super().__init__(screen, color)
        self.font = font

    def draw(self, center, text):
        text = self.font.render(text, True, self.color)
        text_rect = text.get_rect()
        text_rect.center = center.to_tuple()
        self.screen.blit(text, text_rect)

