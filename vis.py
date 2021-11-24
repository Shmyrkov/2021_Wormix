import sys
import pyglet
import pygame
from pyglet.gl import *
from noise import pnoise1


RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

span = 5
points = 256
base = 0
octaves = 1

r = range(256)
a = -1000
b = 300

for i in r:
    x = (float(i) * span / points - 0.5 * span)*400
    y = pnoise1(x + base, octaves)*100+400
    pygame.draw.line(screen, WHITE, [a, b], [x, y], 3)
    pygame.draw.rect(screen, WHITE, (x, y, 5, 600))
    a = x
    b = y

pygame.display.update()
clock = pygame.time.Clock()
finished = False
FPS = 30

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
