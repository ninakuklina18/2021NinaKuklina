
import pygame
import math
from pygame.draw import *
from pygame.event import *
from random import *
import time
import os

pygame.init()

# start condition
score = 0
hight_screen = 700
width_screen = 1300
start_time = time.time()
time_game = 30
# balls
count_ball = 8
max_speed_ball = 15
min_speed_ball = 2
max_radius = 60
min_radius = 15
max_alpha_ball = 2 * math.pi
balls = []
# square
count_triangle = 3
max_speed_triangle = 15
min_speed_triangle = 2
max_side = 200
min_side = 20
triangles = []

FPS = 30
screen = pygame.display.set_mode((width_screen, hight_screen))

colors = [(0, 0, 0),  # black
          (51, 51, 255),  # blue
          (51, 153, 255),  # sky
          (102, 255, 255),  # light_blue
          (0, 0, 204),  # dark_blue
          (153, 153, 255),  # light_violet
          (0, 204, 102),  # green-turquoise
          (0, 255, 0),  # lime
          (255, 255, 102),  # banana
          ]


def new_ball():
    '''
    Draw a new ball
    Return the parameters of the ball:
    ball[0] is radius
    ball[1] is x coordinate of the center
    ball[2] is y coordinate of the center
    ball[3] is direction angle
    ball[4] is speed
    ball[5] is color
    '''

    radius = randint(min_radius, max_radius)
    x_start_ball = randint(radius, width_screen - radius)
    y_start_ball = randint(radius, hight_screen - radius)
    angle_ball = randint(0, int(max_alpha_ball))
    speed_ball = randint(min_speed_ball, max_speed_ball)
    color = colors[randint(2, 8)]
    circle(screen, color, (x_start_ball, y_start_ball), radius)
    return [radius, x_start_ball, y_start_ball, angle_ball, speed_ball, color]


def new_triangle():
    '''
    Draw new triangle
    Return the parameters of the triangle:
      triangle[0] is side
      triangle[1] is x coordinate of center
      triangle[2] is y coordinate of center
     triangle[3] is speed
      triangle[4] is color
    '''

    side = randint(min_side, max_side)
    x_start_triangle = randint(side // 2, width_screen - side // 2)
    y_start_triangle = randint(3 ** 0.5 * side // 2, hight_screen - (3 ** 0.5 * side // 2))
    speed_triangle = randint(min_speed_triangle, max_speed_triangle)
    color = colors[randint(1, 8)]
    polygon(screen, color, ((x_start_triangle - side // 2, y_start_triangle + (3 ** 0.5 * side // 6)),
                            (x_start_triangle, y_start_triangle - side // 3 ** 0.5),
                            (x_start_triangle + side // 2, y_start_triangle + (3 ** 0.5 * side // 6))
                            ))
    return [side, x_start_triangle, y_start_triangle, speed_triangle, color]


def move_ball(ball: list):
    '''
    Moves the ball according to its paraveters
    Change the angle when reflected from the wall
    Gets parameters of one ball
    Returns new ball parameters
    '''

    color = ball[5]
    radius = ball[0]
    x = ball[1]
    y = ball[2]
    if x >= width_screen - radius:
        ball[3] = math.pi / 2 + random() * math.pi
    if y >= hight_screen - radius:
        ball[3] = random() * math.pi
    if radius >= x:
        ball[3] = random() * math.pi - math.pi / 2
    if radius >= y:
        ball[3] = random() * math.pi + math.pi
    speed = ball[4]
    alpha_ball = ball[3]
    x += int(speed * math.cos(alpha_ball))
    y -= int(speed * math.sin(alpha_ball))
    ball[1] = x
    ball[2] = y
    circle(screen, color, (x, y), radius)
    return ball


def move_triangle(triangle: list, triangles: list):
    '''
    Reduces the size of the triangle to according to its parameters
    Goes to function delete_triangle at zero side of the triangle
    Gets parameters of one triangle and the whole list of triangle
    Returns the modified square parameters and the whole list of squares
    '''

    color = triangle[4]
    side = triangle[0]
    x = triangle[1]
    y = triangle[2]
    speed = triangle[3]
    side -= 1 * int(speed * 0.2)
    if side <= 1:
        delete_triangle(triangle, triangles)
    polygon(screen, color, ((x - side // 2, y + (3 ** 0.5 * side // 6)),
                            (x, y - side // 3 ** 0.5),
                            (x + side // 2, y + (3 ** 0.5 * side // 6))
                            ))

    triangle[0] = side
    return triangle, triangles


def delete_ball(ball: list, balls: list):
    '''
    Replaces the "ball" in the "balls" list with a new one
    To do this, calls the function new_ball
    Gets parameters of one ball, which need to delete and the whole list of balls
    Returns the modified nested list "ball" in list "balls"
    '''

    balls[balls.index(ball)] = list(new_ball())
    return balls


def delete_triangle(triangle: list, triangles: list):
    '''
    Replaces the "triangle" in the "triangles" list with a new one
    To do this, calls the function new_triangle
    Gets parameters of one triangle, which need to delete and the whole list of triangles
    Returns the modified nested list "triangle" in list "triangles"
    '''

    triangles[triangles.index(triangle)] = list(new_triangle())
    return triangles


def click_ball(ball: list, event, score: int, balls: list):
    '''
    Checks if the player hits the ball
    Calls function delete_ball when hitting the ball
    Gets the following parameters:
      ball is parameters of one ball
      score is current hit count
      balls is list of all balls
    Returns the modified nested list "ball" in list "balls" and "score"
    '''

    radius = ball[0]
    x_ball = ball[1]
    y_ball = ball[2]
    distance = math.sqrt((event.pos[0] - x_ball) ** 2 + (event.pos[1] - y_ball) ** 2)
    if distance <= radius:
        delete_ball(ball, balls)
        score = score + 1
    return balls, score


def click_triangle(triangle: list, event, score: int, triangles: list):
    '''
    Checks if the player hits the triangle
    Calls function delete_triangle when hitting the triangle
    Gets the following parameters:
      square is parameters of one triangle
      score is current hit count
      squares is list of all triangles
    Returns the modified nested list "triangle" in list "triangles" and "score"
    '''

    side = triangle[0]
    x_triangle = triangle[1]
    y_triangle = triangle[2]
    if (event.pos[0] <= x_triangle + side // 2) and (event.pos[0] >= x_triangle - side // 2) and (
            event.pos[1] <= y_triangle + side // 2) and (event.pos[1] >= y_triangle - side // 2):
        delete_triangle(triangle, triangles)
        score = score + 5
    return triangles, score


# player's name
print("Enter your name here: ")
name = input()

# generation of the first balls
for ball in range(count_ball):
    balls.append(list(new_ball()))

# generation of the first triangles
for triangle in range(count_triangle):
    triangles.append(list(new_triangle()))

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    if time.time() - start_time > time_game:
        finished = True
    pygame.display.update()
    screen.fill(colors[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                balls, score = click_ball(ball, event, score, balls)
            for triangle in triangles:
                triangles, score = click_triangle(triangle, event, score, triangles)
    for ball in balls:
        move_ball(ball)
    for triangle in triangles:
        move_triangle(triangle, triangles)
pygame.quit()
count = 0
file = open('Score_table', 'r')
if os.stat("Score_table").st_size != 0:
    for line in file:
        player_score = line.split()[-1] # the result of one other player
        if int(player_score) >= count:
            count = int(player_score)
    if score >= count:
        line_person = name + ' : ' + str(score)
        file = open('Score_table', 'a')
        file.write(line_person + "\n")
else:
    line_person = name + ' : ' + str(score)
    file = open('Score_table', 'a')
    file.write(line_person + "\n")
file.close()

print("Your score is ", score)
