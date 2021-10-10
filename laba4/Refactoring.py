import pygame
import pygame.draw as pgd
from math import sin, cos, pi
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)
GRASS = (50, 255, 50)
BLUE = (50, 50, 255)
LIGHTBLUE = (150, 150, 255)
PEACH = (255, 100, 100)
BROWN = (190, 100, 34)
LIGHTBROWN = (204, 119, 34)
pygame.init()

FPS = 30
screen = pygame.display.set_mode((910, 600))


def sun(x, y, n, r1, r2):
    """
        Функция рисует солнце.
        x, y - координаты центра солнца
        n- число вершин многоугольника, изображающего солнце
        r1, r2-  радиусы описанной и вписанной в многоугольник окружности соответственно
    """
    spt = []
    for i in range(n):
        a = 2 * pi * i / n
        if i % 2 == 0:
            xt = int(r1 * cos(a))
            yt = int(r1 * sin(a))
        else:
            xt = int(r2 * cos(a))
            yt = int(r2 * sin(a))
        xt += x
        yt += y
        spt.append((xt, yt))
    pgd.polygon(screen, PEACH, spt, 0)
    pgd.polygon(screen, BLACK, spt, 1)


def cloud(x, y, r):
    """
        Функция рисует облако.
        x, y - координаты центра левого нижнего круга
        r - радиус кругов, из которых составлено облако
    """
    pgd.circle(screen, WHITE, (x + r, y + 2 * r), r, 0)
    pgd.circle(screen, BLACK, (x + r, y + 2 * r), r, 1)
    pgd.circle(screen, WHITE, (x + 2 * r, y + 2 * r), r, 0)
    pgd.circle(screen, BLACK, (x + 2 * r, y + 2 * r), r, 1)
    pgd.circle(screen, WHITE, (x + 3 * r, y + 2 * r), r, 0)
    pgd.circle(screen, BLACK, (x + 3 * r, y + 2 * r), r, 1)
    pgd.circle(screen, WHITE, (x + 4 * r, y + 2 * r), r, 0)
    pgd.circle(screen, BLACK, (x + 4 * r, y + 2 * r), r, 1)
    pgd.circle(screen, WHITE, (x + 3 * r, y + r), r, 0)
    pgd.circle(screen, BLACK, (x + 3 * r, y + r), r, 1)
    pgd.circle(screen, WHITE, (x + 2 * r, y + r), r, 0)
    pgd.circle(screen, BLACK, (x + 2 * r, y + r), r, 1)


def tree(x, y, s):
    """
            Функция рисует дерево.
            x, y - координаты центра изображения
            s- параметр, отвечающий за размер дерева
    """
    k = 0.8
    pgd.rect(screen, BLACK, (x + s * 3 // 7, int(y + s * k), s // 7, s))
    pgd.circle(screen, GREEN, (x + s // 2, int(y + s * k // 4)), s // 4,
               0)
    pgd.circle(screen, BLACK, (x + s // 2, int(y + s * k // 4)), s // 4, 1)
    pgd.circle(screen, GREEN, (x + s // 4, int(y + s * k // 2)), s // 4,
               0)
    pgd.circle(screen, BLACK, (x + s // 4, int(y + s * k // 2)), s // 4, 1)
    pgd.circle(screen, GREEN, (x + s * 3 // 4, int(y + s * k // 2)),
               s // 4, 0)
    pgd.circle(screen, BLACK, (x + s * 3 // 4, int(y + s * k // 2)),
               s // 4, 1)
    pgd.circle(screen, GREEN, (x + s // 2, int(y + s * k * 3 // 4)),
               s // 4, 0)
    pgd.circle(screen, BLACK, (x + s // 2, int(y + s * k * 3 // 4)),
               s // 4, 1)
    pgd.circle(screen, GREEN, (x + s // 4, int(y + s * k)), s // 4, 0)
    pgd.circle(screen, BLACK, (x + s // 4, int(y + s * k)), s // 4, 1)
    pgd.circle(screen, GREEN, (x + s * 3 // 4, int(y + s * k)), s // 4,
               0)
    pgd.circle(screen, BLACK, (x + s * 3 // 4, int(y + s * k)), s // 4, 1)


def house(x, y, s):
    """
              Функция рисует дом.
              x, y - левого нижнего угла изображения
              s- параметр, отвечающий за размер дома
      """
    pgd.rect(screen, LIGHTBROWN, (x, y + s, 2 * s, int(1.5 * s)))
    pgd.rect(screen, BLACK, (x, y + s, 2 * s, int(1.5 * s)), 1)
    pgd.rect(screen, LIGHTBLUE, (x + s * 3 // 4, y + int(1.5 * s),
                                       s // 2, s // 2))
    pgd.rect(screen, BROWN, (x + s * 3 // 4, y + int(1.5 * s),
                                      s // 2, s // 2), 5)
    pgd.polygon(screen, PEACH, [(x, y + s), (x + s, y), (x + 2 * s,
                                                                   y + s)], 0)
    pgd.polygon(screen, BLACK, [(x, y + s), (x + s, y), (x + 2 * s,
                                                             y + s)], 1)
    kt = 13
    for i in range(kt + 1):
        pgd.polygon(screen, GREY, [(x + s - i * int(s // kt),
                                               y + i * int(s // kt)),
                                              (x + s - (i + 1) * int(s // kt),
                                               y + (i + 1) * int(s // kt)),
                                              (x + s - i * int(s // kt),
                                               y + (i + 1) * int(s // kt))], 0)
    for i in range(kt + 1):
        pgd.polygon(screen, GREY, [(x + s + i * int(s // kt),
                                               y + i * int(s // kt)),
                                              (x + s + (i + 1) * int(s // kt),
                                               y + (i + 1) * int(s // kt)),
                                              (x + s + i * int(s // kt),
                                               y + (i + 1) * int(s // kt))], 0)


pgd.rect(screen, BLUE, (0, 0, 910, 300))
pgd.rect(screen, (50, 255, 50), (0, 300, 910, 300))
sun(50, 50, 40, 40, 38)
cloud(150, 40, 35)
tree(320, 210, 140)
house(100, 230, 100)
house(500, 230, 80)
tree(700, 200, 110)
cloud(430, 100, 25)
cloud(700, 60, 37)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


