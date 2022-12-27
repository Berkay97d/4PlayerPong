import pygame

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

GAME_TITLE = '4 PLAYER PONG'

FPS = 120

# BALL
BALL_RADIUS = 10
BALL_COLOR = BLACK


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
gameObjects = {}


# INIT
pg.init()
screen = pg.display.set_mode((SCREEN_SIZE.x, SCREEN_SIZE.y))
pg.display.set_caption(GAME_TITLE)


# FUNCTIONS
def main():
    init_gameobjects()
    clock = pg.time.Clock()

    while isRunning:
        clock.tick(FPS)
        draw()
        update()

    pg.quit()


def update():
    handle_events()
    handle_inputs()
    move_gameobjects(1.0/FPS)


def init_gameobjects():
    paddle1 = Paddle(screen, 'P1', Vector2(SCREEN_HALF_SIZE.x, SCREEN_SIZE.y - PADDLE_HALF_HEIGHT), Vector2(PADDLE_WIDTH, PADDLE_HEIGHT), P1_COLOR, Vector2.right(), PADDLE_SPEED)
    paddle2 = Paddle(screen, 'P2', Vector2(SCREEN_SIZE.x - PADDLE_HALF_HEIGHT, SCREEN_HALF_SIZE.y), Vector2(PADDLE_HEIGHT, PADDLE_WIDTH), P2_COLOR, Vector2.down(), PADDLE_SPEED)
    paddle3 = Paddle(screen, 'P3', Vector2(SCREEN_HALF_SIZE.x, PADDLE_HALF_HEIGHT), Vector2(PADDLE_WIDTH, PADDLE_HEIGHT), P3_COLOR, Vector2.right(), PADDLE_SPEED)
    paddle4 = Paddle(screen, 'P4', Vector2(PADDLE_HALF_HEIGHT, SCREEN_HALF_SIZE.y), Vector2(PADDLE_HEIGHT, PADDLE_WIDTH), P4_COLOR, Vector2.down(), PADDLE_SPEED)
    ball = Ball(screen, 'ball', SCREEN_HALF_SIZE, BALL_RADIUS, BALL_COLOR)
    global gameObjects
    gameObjects = [paddle1, paddle2, paddle3, paddle4, ball]


def move_gameobjects(delta_time):
    for gameobject in gameObjects:
        gameobject.move(delta_time)


def handle_events():
    global isRunning
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
            break


def draw_borders():
    pg.draw.rect(screen, P2_COLOR, (SCREEN_SIZE.x - BORDER_THICKNESS, 0, BORDER_THICKNESS, SCREEN_SIZE.y))
    pg.draw.rect(screen, P4_COLOR, (0, 0, BORDER_THICKNESS, SCREEN_SIZE.y))
    pg.draw.rect(screen, P1_COLOR, (0, SCREEN_SIZE.y - BORDER_THICKNESS, SCREEN_SIZE.x, BORDER_THICKNESS))
    pg.draw.rect(screen, P3_COLOR, (0, 0, SCREEN_SIZE.x, BORDER_THICKNESS))


def draw_gameobjects():
    for gameObject in gameObjects:
        gameObject.draw()


def draw():
    screen.fill(SCREEN_COLOR)
    draw_borders()
    draw_gameobjects()
    pg.display.update()


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
