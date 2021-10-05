import pygame


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LSALMON = (255, 160, 122)
PEACH = (255, 218, 185)
LEMONE = (255, 250, 205)
SKYBLUE = (100, 149, 237)
TOMATO = (255, 99, 71)
CADET = (176, 196, 222)
SLATE = (106, 90, 205)
DARK = (72, 61, 109)
BROWN = (139, 69, 19)


pygame.init()
x, y = 640, 480 #The size of the screen
screen = pygame.display.set_mode([x, y]) # Объект содерж экран.
pygame.display.set_caption('My first pygame app window caption')
done = False
clock = pygame.time.Clock() # Тут есть задержка.

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # The colours of background
    screen.fill(LSALMON)
    pygame.draw.rect(screen, PEACH, (0, y/5, x, y/5))
    pygame.draw.rect(screen, LEMONE, (0, 2*y/5, x, y/5))
    pygame.draw.rect(screen, SKYBLUE, (0, 3*y/5, x, 2*y/5))

    # A sun
    pygame.draw.circle(screen, TOMATO, [int(x/2),int(y/5)],40)
        
    # Mountains on the background
    pygame.draw.polygon(screen, CADET, [(640, 144), (586, 120), (510, 160)])
    pygame.draw.polygon(screen, CADET, [(580, 150), (510, 110), (453, 166)])
    pygame.draw.ellipse(screen, CADET, (503, 107, 30, 30))
    pygame.draw.ellipse(screen, CADET, (525, 124, 30, 30))
    pygame.draw.polygon(screen, CADET, [(527, 111), (551, 130), (510, 160)])
    pygame.draw.polygon(screen, CADET, [(400, 171), (480, 86), (510, 160)])
    pygame.draw.polygon(screen, CADET, [(400, 171), (300, 182), (346, 153)])
    pygame.draw.polygon(screen, CADET, [(510, 160), (330, 176), (386, 143)])
    pygame.draw.rect(screen, CADET, (386, 130, 60, 20))
    pygame.draw.ellipse(screen, PEACH, (370, 110, 60, 40))
    pygame.draw.ellipse(screen, CADET, (462, 85, 29, 50))
    pygame.draw.polygon(screen, CADET, [(430, 135), (465, 94), (480, 110)])
    pygame.draw.polygon(screen, PEACH, [(428, 137), (465, 94), (410, 135)])
    pygame.draw.polygon(screen, CADET, [(133, 92), (160, 105), (160, 160)])
    pygame.draw.polygon(screen, CADET, [(300, 182), (100, 205), (280, 170)])
    pygame.draw.polygon(screen, CADET, [(300, 182), (40, 177), (0, 217)])  
    pygame.draw.polygon(screen, CADET, [(250, 188), (130, 90), (64, 210)]) 
    pygame.draw.rect(screen, CADET, (40, 150, 60, 50))
    pygame.draw.ellipse(screen, PEACH, (20, 130, 70, 50))
    pygame.draw.polygon(screen, PEACH, [(89, 160), (70, 155), (126, 96)])    
    
    # Mountains in the middle.
    pygame.draw.polygon(screen, SLATE, [(80, 288), (250, 288), (160, 250)]) 
    pygame.draw.polygon(screen, SLATE, [(190, 288), (300, 288), (260, 210)])
    pygame.draw.polygon(screen, SLATE, [(190, 288), (210, 200), (260, 210)])
    pygame.draw.polygon(screen, SLATE, [(190, 288), (440, 288), (380, 230)])
    pygame.draw.polygon(screen, SLATE, [(440, 288), (570, 205), (640, 288)])
    pygame.draw.polygon(screen, SLATE, [(600, 288), (640, 288), (640, 160)])
    pygame.draw.polygon(screen, SLATE, [(600, 288), (615, 210), (640, 203)])
    pygame.draw.ellipse(screen, SLATE, (340, 210, 80, 70))
    pygame.draw.ellipse(screen, SLATE, (354, 210, 70, 40))
    pygame.draw.polygon(screen, SLATE, [(400, 288), (640, 288), (410, 220)])
    pygame.draw.ellipse(screen, LEMONE, (433, 215, 80, 40))
    pygame.draw.polygon(screen, LEMONE, [(433, 238), (402, 205), (450, 220)])
    pygame.draw.polygon(screen, SLATE, [(317, 268), (344, 230), (370, 280)])

    
    
    pygame.display.flip()
pygame.quit()



