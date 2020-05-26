def atari_breakout():
    import pygame,random,time
    WIDTH=1000
    HEIGHT=600

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    over = pygame.font.Font('freesansbold.ttf',160)

    # Test comment to check git
    # Another
    # Test 2

    carryOn = True

    def draw_rect(x,y,width,height):
        pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    def draw_circle(x,y,radius):
        pygame.draw.circle(screen,(0,0,255),(x,y),radius)
    def game_over():
        display = over.render('GAME OVER', True, (255, 105, 180))
        screen.blit(display, (0,250))


    rect_x = 200
    rect_change = 0
    circle_x = 500
    circle_y = 300
    circle_direction = [1,1]
    circle_speed = [2,2]
    radius = 10
    while carryOn:

        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False
                if event.key == pygame.K_LEFT:
                    rect_change = -8
                if event.key == pygame.K_RIGHT:
                    rect_change = 8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    rect_change = 0
                if event.key == pygame.K_RIGHT:
                    rect_change = 0
        if circle_x - radius <= 0 or circle_x + radius >= 1000:
            circle_x += 10 if circle_x - radius <= 0 else -10
            circle_direction[0] *= -1
            circle_speed = [x * random.randint(2, 9) for x in circle_direction]
        elif circle_y - radius <= 0 or (circle_y + radius >= 575 and rect_x <=circle_x<= rect_x + 125) :
            circle_y += 10 if circle_y - radius <= 0 else -10
            circle_direction[1] *= -1
            circle_speed = [x * random.randint(2, 9) for x in circle_direction]
        elif circle_y + radius >= 600:
            circle_speed = [0,0]
            rect_change = 0
            game_over()
        if rect_x + 125 >= 1000 or rect_x <= 0:
            rect_x = 0 if rect_x <= 0 else 1000-125
        circle_x += circle_speed[0]
        circle_y += circle_speed[1]
        rect_x += rect_change
        draw_rect(rect_x,575,125,25)
        draw_circle(circle_x,circle_y,radius)
        pygame.display.update()

