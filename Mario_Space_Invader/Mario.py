def mario():
    import pygame, random, math,time
    from pygame import mixer
    import os.path

    print(os.path.abspath('Mario_Space_Invader/backround2.jpg'))

    pygame.init()

    screen =  pygame.display.set_mode((800,800))
    pygame.display.set_caption("Game same")

    background = pygame.image.load("./Resources/backround.jpg").convert()

    marioicon = pygame.image.load("./Resources/mariocharacter.png")
    pygame.display.set_icon(marioicon)

    mixer.music.load("./Resources/dolphin shoals.mp3")
    mixer.music.play(-1)


    mario = pygame.image.load("./Resources/mariocharacter.png")
    playerX = 400
    playerY = 600
    player_x_change = 0
    player_y_change = 0

    enemies = []
    enemyX = []
    enemyY = []
    enemy_y_change = []
    enemy_x_change = []
    numenemies = 10
    for x in range(numenemies):
        enemies.append(pygame.image.load("./Resources/bowser.png"))
        enemyX.append(random.randint(30,700))
        enemyY.append(random.randint(50,150))
        enemy_x_change.append(8)
        enemy_y_change.append(50)
    print(enemies)

    fireball = pygame.image.load("./Resources/fireball.png")
    bulletX = 0
    bulletY = 600
    bullet_x_change = 0
    bullet_y_change = 11
    bullet_state = 'ready'

    score_ = 0
    font = pygame.font.Font('freesansbold.ttf',32)

    scorex = 10
    scorey = 10

    def show_score(x,y):
        score = font.render('Score: ' + str(score_),True, (255,255,255))
        screen.blit(score,(x,y))

    def player(x,y):
        screen.blit(mario, (x,y))
    def enemy(x,y,i):
        screen.blit(enemies[i], (x,y))
    def fire_bullet(x,y):
        nonlocal bullet_state
        bullet_state = 'fire'
        screen.blit(fireball,(x+16,y+10))
    def isCollision(enemyX,enemyY,bulletX,bulletY):
        distance = math.sqrt((bulletX-enemyX)**2 + (bulletY-enemyY)**2)
        if distance < 27 :
            return True
        else:
            return False

    over = pygame.font.Font('freesansbold.ttf',60)

    def game_over():
        over_ = over.render('GAME OVER',True, (255,255,255))
        screen.blit(over_, (200,400))
        mixer.music.stop()









    carryOn = True


    while carryOn:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                mixer.music.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -9.5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 9.5
                if event.key == pygame.K_UP:
                    player_y_change = -9.5
                if event.key == pygame.K_DOWN:
                    player_y_change = 9.5
                if event.key == pygame.K_SPACE:
                    if bullet_state is 'ready':
                        sound = mixer.Sound('./Resources/fire sound.wav')
                        sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_ESCAPE:
                    break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player_x_change = 0
                if event.key == pygame.K_RIGHT:
                    player_x_change = 0
                if event.key == pygame.K_UP:
                    player_y_change = 0
                if event.key == pygame.K_DOWN:
                    player_y_change = 0

        playerX += player_x_change
        # playerY += player_y_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736


        if bullet_state is 'fire':
            fire_bullet(bulletX,bulletY)
            bulletY -= bullet_y_change
        if bulletY <= 0:
            bulletY = 600
            bullet_state = 'ready'


        player(playerX, playerY)

        for i in range(numenemies):

            if enemyY[i] > 560:
                for x in range(numenemies):
                    enemyY[x] = 2000
                game_over()
                break


            enemyX[i] += enemy_x_change[i]
            if enemyX[i] <= 0:
                enemy_x_change[i] = 4
                enemyY[i] += enemy_y_change[i]
            elif enemyX[i] >= 736:
                enemy_x_change[i] = -4
                enemyY[i] += enemy_y_change[i]
            collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
            if collision:
                bruh = mixer.Sound('./Resources/Bruh Sound Effect #2.wav')
                bruh.play()
                bulletY = 600
                bullet_state = 'ready'
                score_ += 1
                enemyX[i] = random.randint(0,736)
                enemyY[i] = random.randint(50,150)
            enemy(enemyX[i],enemyY[i],i)
        show_score(scorex,scorey)
        pygame.display.update()
