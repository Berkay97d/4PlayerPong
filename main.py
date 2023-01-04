import random

import pygame

from Shapes import *
from Entities import *
from DataTypes import *

# COLOR
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (64, 64, 64)

# SCREEN
SCREEN_SIZE = Vector2(1080, 1080) * .9
SCREEN_HALF_SIZE = SCREEN_SIZE * 0.5

SCREEN_COLOR = GREY

SCREEN_BOTTOM_LEFT = Vector2(0, SCREEN_SIZE.y)
SCREEN_BOTTOM_RIGHT = SCREEN_SIZE
SCREEN_UP_RIGHT = Vector2(SCREEN_SIZE.x, 0)
SCREEN_UP_LEFT = Vector2(0, 0)

SCOREBOARD_OFFSET = 25

# GAME SETTINGS
GAME_TITLE = '4 PLAYER PONG'
FPS = 300
SCORE_MULTIPLIER = 1

# BALL
BALL_RADIUS = 10
BALL_COLOR = BLACK
BALL_SPEED = 350

# PADDLE
PADDLE_SPEED = 500

P1_COLOR = WHITE
P2_COLOR = RED
P3_COLOR = GREEN
P4_COLOR = BLUE

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

PADDLE_HALF_WIDTH = PADDLE_WIDTH * 0.5
PADDLE_HALF_HEIGHT = PADDLE_HEIGHT * 0.5

# ENVIRONMENT
BORDER_THICKNESS = 5

# FIELDS
isRunning = True
gameObjects = []
paddles = []
balls = []
borders = []
scoreboards = []

# INIT
pg.init()
screen = pg.display.set_mode((SCREEN_SIZE.x, SCREEN_SIZE.y))
pg.display.set_caption(GAME_TITLE)
font = pygame.font.SysFont('Comic Sans MS', 30)


# FUNCTIONS
def main():
    init_gameobjects()
    clock = pg.time.Clock()
    while isRunning:
        clock.tick(FPS)
        handle_events()
        update()
        draw()

    pg.quit()


def update():
    move_gameobjects(1.0 / FPS)
    handle_collision()
    handle_points()
    move_paddles()
    keep_paddles_in_area()


def draw():
    screen.fill(SCREEN_COLOR)
    draw_gameobjects()
    pg.display.update()


def init_gameobjects():
    paddle_shape1 = Rect(screen, P1_COLOR, Vector2(PADDLE_WIDTH, PADDLE_HEIGHT))
    paddle_shape3 = Rect(screen, P3_COLOR, Vector2(PADDLE_WIDTH, PADDLE_HEIGHT))
    paddle_shape2 = Rect(screen, P2_COLOR, Vector2(PADDLE_HEIGHT, PADDLE_WIDTH))
    paddle_shape4 = Rect(screen, P4_COLOR, Vector2(PADDLE_HEIGHT, PADDLE_WIDTH))

    border_shape1 = Rect(screen, P1_COLOR, Vector2(SCREEN_SIZE.x, BORDER_THICKNESS))
    border_shape2 = Rect(screen, P2_COLOR, Vector2(BORDER_THICKNESS, SCREEN_SIZE.y))
    border_shape3 = Rect(screen, P3_COLOR, Vector2(SCREEN_SIZE.x, BORDER_THICKNESS))
    border_shape4 = Rect(screen, P4_COLOR, Vector2(BORDER_THICKNESS, SCREEN_SIZE.y))

    paddle1 = Paddle('P1', Vector2(SCREEN_HALF_SIZE.x, SCREEN_SIZE.y - PADDLE_HALF_HEIGHT), paddle_shape1,
                     Vector2.right(), PADDLE_SPEED)
    paddle2 = Paddle('P2', Vector2(SCREEN_SIZE.x - PADDLE_HALF_HEIGHT, SCREEN_HALF_SIZE.y), paddle_shape2,
                     Vector2.up(), PADDLE_SPEED)
    paddle3 = Paddle('P3', Vector2(SCREEN_HALF_SIZE.x, PADDLE_HALF_HEIGHT), paddle_shape3, Vector2.right(),
                     PADDLE_SPEED)
    paddle4 = Paddle('P4', Vector2(PADDLE_HALF_HEIGHT, SCREEN_HALF_SIZE.y), paddle_shape4, Vector2.up(), PADDLE_SPEED)

    p1_border = Border('p1', Vector2(SCREEN_HALF_SIZE.x, SCREEN_SIZE.y - BORDER_THICKNESS / 2), border_shape1)
    p2_border = Border('p2', Vector2(SCREEN_SIZE.x - BORDER_THICKNESS / 2, SCREEN_HALF_SIZE.y), border_shape2)
    p3_border = Border('p3', Vector2(SCREEN_HALF_SIZE.x, BORDER_THICKNESS / 2), border_shape3)
    p4_border = Border('p4', Vector2(BORDER_THICKNESS / 2, SCREEN_HALF_SIZE.y), border_shape4)

    p1_score_shape = Text(screen, P1_COLOR, font)
    p2_score_shape = Text(screen, P2_COLOR, font)
    p3_score_shape = Text(screen, P3_COLOR, font)
    p4_score_shape = Text(screen, P4_COLOR, font)

    p1_scoreboard = ScoreBoard('ScoreP1', paddle1.position + Vector2.up() * SCOREBOARD_OFFSET, p1_score_shape)
    p2_scoreboard = ScoreBoard('ScoreP2', paddle2.position + Vector2.left() * SCOREBOARD_OFFSET, p2_score_shape)
    p3_scoreboard = ScoreBoard('ScoreP3', paddle3.position + Vector2.down() * SCOREBOARD_OFFSET, p3_score_shape)
    p4_scoreboard = ScoreBoard('ScoreP4', paddle4.position + Vector2.right() * SCOREBOARD_OFFSET, p4_score_shape)

    global gameObjects
    gameObjects = [paddle1, paddle2, paddle3, paddle4, p1_border, p2_border, p3_border, p4_border, p1_scoreboard,
                   p2_scoreboard, p3_scoreboard, p4_scoreboard]
    global paddles
    paddles = [paddle1, paddle2, paddle3, paddle4]
    global borders
    borders = [p1_border, p2_border, p3_border, p4_border]
    global scoreboards
    scoreboards = [p1_scoreboard, p2_scoreboard, p3_scoreboard, p4_scoreboard]
    init_ball()


def init_ball():
    ball_shape = Circle(screen, BALL_COLOR, BALL_RADIUS)
    ball = Ball('ball', SCREEN_HALF_SIZE, ball_shape)
    balls.append(ball)
    gameObjects.append(ball)
    ball.velocity = Vector2.random() * BALL_SPEED


def handle_collision():
    for paddle in paddles:
        for ball in balls:
            if Physics.box_collider2d_circle_collider_intersects(paddle.collider, ball.collider):
                ball.on_hit_paddle(paddle)


def update_scores():
    for i in range(len(paddles)):
        scoreboards[i].score = paddles[i].score


def handle_points():
    for border in borders:
        for ball in balls:
            if Physics.box_collider2d_circle_collider_intersects(border.collider, ball.collider):
                ball.on_hit_border(SCORE_MULTIPLIER)
                balls.remove(ball)
                gameObjects.remove(ball)
                update_scores()
                init_ball()


def move_gameobjects(delta_time):
    for gameobject in gameObjects:
        gameobject.move(delta_time)
    balls[0].velocity += balls[0].velocity/(FPS*10)


def handle_events():
    global isRunning
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
            break


def draw_gameobjects():
    for gameObject in gameObjects:
        gameObject.draw()


def keep_paddles_in_area():
    paddles[0].stay_area(PADDLE_WIDTH/2, SCREEN_SIZE.x - PADDLE_WIDTH / 2, 0, SCREEN_SIZE.y)
    paddles[2].stay_area(PADDLE_WIDTH/2, SCREEN_SIZE.x - PADDLE_WIDTH / 2, 0, SCREEN_SIZE.y)
    paddles[1].stay_area(0, SCREEN_SIZE.x, PADDLE_WIDTH/2, SCREEN_SIZE.y - PADDLE_WIDTH / 2)
    paddles[3].stay_area(0, SCREEN_SIZE.x, PADDLE_WIDTH/2, SCREEN_SIZE.y - PADDLE_WIDTH / 2)


def move_paddles():
    rand = random.uniform(2, 3)
    rand2 = random.uniform(0, 1)

    if rand2 > 0.5:
        if balls[0].position.x > paddles[0].position.x + PADDLE_WIDTH / rand:
            paddles[0].move_right()
        elif balls[0].position.x < paddles[0].position.x - PADDLE_WIDTH / rand:
            paddles[0].move_left()
        else:
            paddles[0].stop()

        if balls[0].position.x > paddles[2].position.x - PADDLE_WIDTH / rand:
            paddles[2].move_right()
        elif balls[0].position.x < paddles[2].position.x:
            paddles[2].move_left()
        else:
            paddles[2].stop()

        if balls[0].position.y > paddles[1].position.y - PADDLE_WIDTH / rand:
            paddles[1].move_left()
        elif balls[0].position.y < paddles[1].position.y + PADDLE_WIDTH / rand:
            paddles[1].move_right()
        else:
            paddles[1].stop()

        if balls[0].position.y > paddles[3].position.y - PADDLE_WIDTH / rand:
            paddles[3].move_left()
        elif balls[0].position.y < paddles[3].position.y + PADDLE_WIDTH / rand:
            paddles[3].move_right()
        else:
            paddles[3].stop()
    else:
        if balls[0].position.x > paddles[0].position.x - PADDLE_WIDTH / rand:
            paddles[0].move_right()
        elif balls[0].position.x < paddles[0].position.x + PADDLE_WIDTH / rand:
            paddles[0].move_left()
        else:
            paddles[0].stop()

        if balls[0].position.x > paddles[2].position.x + PADDLE_WIDTH / rand:
            paddles[2].move_right()
        elif  balls[0].position.x < paddles[2].position.x:
            paddles[2].move_left()
        else:
            paddles[2].stop()

        if balls[0].position.y > paddles[1].position.y - PADDLE_WIDTH / rand:
            paddles[1].move_left()
        elif balls[0].position.y < paddles[1].position.y + PADDLE_WIDTH / rand:
            paddles[1].move_right()
        else:
            paddles[1].stop()

        if balls[0].position.y > paddles[3].position.y + PADDLE_WIDTH / rand:
            paddles[3].move_left()
        elif balls[0].position.y < paddles[3].position.y - PADDLE_WIDTH / rand:
            paddles[3].move_right()
        else:
            paddles[3].stop()

def handle_inputs():
    if get_key(pygame.K_d):
        gameObjects[0].move_right()
    elif get_key(pygame.K_a):
        gameObjects[0].move_left()
    else:
        gameObjects[0].stop()

    if get_key(pygame.K_w):
        gameObjects[1].move_right()
    elif get_key(pygame.K_s):
        gameObjects[1].move_left()
    else:
        gameObjects[1].stop()

    if get_key(pygame.K_RIGHT):
        gameObjects[2].move_right()
    elif get_key(pygame.K_LEFT):
        gameObjects[2].move_left()
    else:
        gameObjects[2].stop()

    if get_key(pygame.K_UP):
        gameObjects[3].move_right()
    elif get_key(pygame.K_DOWN):
        gameObjects[3].move_left()
    else:
        gameObjects[3].stop()


def get_key(key):
    keys = pg.key.get_pressed()
    return keys[key]


if __name__ == '__main__':
    main()
