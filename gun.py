import math
import time
from random import choice
import random as ra
import pygame

FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
GAME_COLORS = [RED, BLUE, GREEN, YELLOW, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

gt = -1  # speed growth per frame
score = 0  # score in the beginning
time_game = 20  # time of one game round
start_time = time.time()

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """
        Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.r = 10
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        if (800 - self.r) > self.x > self.r:
            self.x += self.vx
            self.vx = self.vx * 0.99
        else:
            self.vx = - self.vx
            self.x = self.x + 2 * self.vx

        if (600 - self.r) > self.y > self.r:
            self.y += self.vy
            self.vy = self.vy - gt
            self.vy = self.vy * 0.95
        else:
            self.vy = - 0.9 * self.vy
            self.y = self.y + 0.9 * self.vy

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 20
        self.width = 15
        self.f2_on = 0
        self.an = 0.5
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = -math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = -math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """Рисуем пушку. Зависит от положения мыши."""
        pygame.draw.polygon(self.screen, self.color, ([40, 450],
                                                      [40 + self.f2_power * math.cos(self.an),
                                                       450 - self.f2_power * math.sin(self.an)],
                                                      [40 + self.f2_power * math.cos(self.an) + self.width * math.sin(
                                                          self.an),
                                                       450 - self.f2_power * math.sin(self.an) + self.width * math.cos(
                                                           self.an)],
                                                      [40 + self.width * math.sin(self.an),
                                                       450 + self.width * math.cos(self.an)]))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.x = ra.randint(600, 780)
        self.y = ra.randint(300, 550)
        self.r = 20
        self.points = 0
        self.live = 1
        self.color = choice(GAME_COLORS)
        self.v = 2

    def new_target(self):
        """ Инициализация новой цели."""
        self.x = ra.randint(600, 780)
        self.y = ra.randint(300, 550)
        self.r = ra.randint(2, 50)
        self.v = 2
        self.color = choice(GAME_COLORS)
        self.live = 1

    def move(self):
        self.y = self.y - self.v
        if self.y + self.r >= HEIGHT-80 or self.y - self.r <= 0:
            self.v = -self.v

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []
clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False

while not finished:
    if time.time() - start_time > time_game:
        finished = True
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    target.move()
    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            score = score + 1
            target.new_target()

    gun.power_up()
print('Your score is ', score)
pygame.quit()
