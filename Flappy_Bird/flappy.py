def flappy():
    import pygame,random, math,time

    pygame.init()
    carryOn = True
    screen = pygame.display.set_mode((1000, 600))
    over = pygame.font.Font('freesansbold.ttf',160)


    background = pygame.image.load('./Resources/clouds.png').convert()

    flappyicon = pygame.image.load("./Resources/flap.png")
    pygame.display.set_icon(flappyicon)

    ychange = 5
    pipechange = -10
    angle = 0
    adjustx = 0
    adjusty = 0
    birdx = 300
    birdy = 300
    currentpipex =  1000
    nextpipex = 500
    pipey= -500
    scorex = 10
    scorey = 10


    pipepoints = []
    diffpipes = []
    for x in range(3):
        diffpipes.append(pygame.image.load("./Resources/Top Pipe.png"))
        diffpipes.append(pygame.image.load("./Resources/Bottom Pipe.png"))
        pipepoints.append(random.randint(-900,-500))

    flappy = pygame.image.load('./Resources/flap.png')
    angry_bird = pygame.image.load('./Resources/angry-bird-icon.png')
    toppipe = pygame.image.load("./Resources/Top Pipe.png")
    bottompipe = pygame.image.load("./Resources/Bottom Pipe.png")
    score_ = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    over = pygame.font.Font('freesansbold.ttf',60)


    def player(x,y,tilt):
        flap = pygame.transform.rotate(angry_bird,tilt)
        screen.blit(flap,(x,y))
    def pipes(x,y):
        screen.blit(toppipe,(x,y))
        screen.blit(bottompipe,(x,y+1070))
    def isCollison(birdx,birdy,pipex,pipey):
        topy = pipey + 940
        bottomy = topy + 120
        actualx = pipex + 25
        birdx += 40
        birdy += 40
        possible = []
        possible.extend([(birdx, birdy),(birdx, birdy + 30),(birdx + 30, birdy), (birdx, birdy - 30),(birdx - 30, birdy),(birdx + 30, birdy + 30),(birdx + 30, birdy - 30), (birdx - 30, birdy + 30),(birdx - 30, birdy- 30 )])
        for z in possible:
            x = z[0]
            y = z[1]
            if ((actualx - 30) <= x <= (actualx + 30)) and (topy <= y <= bottomy):
                return True
            elif ((actualx - 30) <= x <= (actualx + 30)) and (y > topy or y < bottomy):
                return False
    def game_over():
        over_ = over.render('GAME OVER',True, (0,0,0))
        screen.blit(over_, (500,300))
    def show_score(x,y):
        score = font.render('Score: ' + str(score_),True, (255,255,255))
        screen.blit(score,(x,y))

    print(pipepoints[1])
    print(diffpipes)


    while carryOn:
        screen.blit(background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn= False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ychange = -4
                    angle = 45
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    ychange = 5
                    angle = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Pipe System: {(currentpipex,pipey)} Pipe clicked: {pygame.mouse.get_pos()}")
                print(f"Bird System: {(birdx, birdy)} Bird clicked: {pygame.mouse.get_pos()}")
        birdy += ychange
        currentpipex+= pipechange
        player(birdx,birdy,angle)
        pipes(currentpipex,pipey)
        if currentpipex <= 0:
            currentpipex = 1000
            pipey = random.randint(-900,-500)
        if birdy <=-64:
            birdy=-64
        if isCollison(birdx,birdy,currentpipex,pipey) is True:
            score_ += 1
        if isCollison(birdx,birdy,currentpipex,pipey) is False or birdy >= 530:
            ychange = 0
            pipechange = 0
            display = over.render('GAME OVER',True,(0,0,0))
            screen.blit(display,(300,300))
            pygame.display.update()
        show_score(scorex,scorey)
        pygame.display.update()
