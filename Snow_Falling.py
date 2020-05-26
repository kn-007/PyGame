def snow_falling(screen_x,screen_y):
    import pygame
    import random
    pygame.init()
    colors = [(0,0,255),(255,0,0),(0,255,0),(0, 255, 251),(250, 250, 0),(255, 0, 174),(119, 255, 0),(0,0,0),(179, 9, 222)]
    random_coordinate = []
    screen_name = pygame.display.set_mode((screen_x,screen_y))
    carryOn = True
    pygame.init()
    for i in range(50):
        a=[random.randint(0,screen_x), random.randint(0,screen_y)]
        random_coordinate.append(a)
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
        screen_name.fill((0,0,0))
        for r in random_coordinate:
            pygame.draw.circle(screen_name, random.choice(colors), r, 4)
            r[1] += 1
            if r[1] == screen_y:
                r[1] = 1
                r[0] = random.randint(0,screen_x)
        pygame.display.update()
