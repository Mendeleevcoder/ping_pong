from pygame import *
from random import randint
from typing import Any

font.init()

WIDTH = 600
HEIGHT = 500
FPS = 60

BACKGROUND = (randint(0, 255), randint(0, 255), randint(0, 255))
WHITE = (255, 255, 255)
RED = (150, 0, 0)
GREEN = (0, 150, 0)

font_text = font.Font(None, 36)
font_score = font.Font(None, 50)

lose1 = font_text.render("PLAYER1 LOSE", True, RED)
lose2 = font_text.render("PLAYER2 LOSE", True, RED)
win1 = font_text.render("PLAYER1 WIN", True, RED)
win2 = font_text.render("PLAYER2 WIN", True, RED)

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("PING-PONG")
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img: str, x: int, y: int, w: int, h: int):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, up: str, down: str, img: str, x: int,  y: int, w: int, h: int, speed: int):
        super().__init__(img, x, y, w, h)
        self.speed = speed
        self.up = up
        self.down = down

    def update(self):
        keys = key.get_pressed()
        if keys[self.up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[self.down] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, img: str, x: int, y: int, w: int, h: int, dx: int, dy: int):
        super().__init__(img, x, y, w, h)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

racket1 = Player(K_w, K_s, "racket.png", 30, 200, 50, 150 , 4)
racket2 = Player(K_UP, K_DOWN, "racket.png", 520, 200, 50, 150, 4)
ball = Ball("tenis_ball.png", 200, 200, 50, 50, 3, 3)

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(BACKGROUND)
        ball.reset()
        racket1.reset()
        racket2.reset()

        racket1.update()
        racket2.update()
        ball.update()

    display.update()
    clock.tick(FPS)

