def tic_tac_toe():
    import pygame,time
    import numpy as np
    pygame.init()

    screen = pygame.display.set_mode((900,900))

    red = (255,0,0)
    carryOn = True
    board = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,}

    over = pygame.font.Font('freesansbold.ttf',160)

    shape = 'x'

    def draw():
        pygame.draw.line(screen,red,(300,0),(300,900),10)
        pygame.draw.line(screen,red,(600,0),(600,900),10)
        pygame.draw.line(screen,red,(0,300),(900,300),10)
        pygame.draw.line(screen,red,(0,600),(900,600),10)
    (q,w) = (0,0)
    def center_of_square(num):
        nonlocal q,w
        if 1<=num<=3:
            (q,w) = (150*(2*num-1),150)
        elif 4<=num<=6:
            (q,w) = (int(150*(2*(num%3)-1)),450) if num%3 != 0 else (int(150*(2*(num/2)-1)),450)
        elif 7<=num<=9:
            (q,w) = (int(150*(2*(num%3)-1)),750) if num%3 != 0 else (int(150*(2*(num/3)-1)),750)
        return (q,w)

    def click():
        position = pygame.mouse.get_pos()
        for i in range(1,10):
            (x,y) = center_of_square(i)
            range1 = (x-150,y-150)
            range2 = (x+150,y+150)
            if range1[0] <= position[0] <= range2[0] and range1[1] <= position[1] <= range2[1]:
                return i
            else:
                continue

    def square(number):
        nonlocal shape
        if number is not None:
            if board[number] == 0:
                (r1,r2) = center_of_square(number)
                if shape == 'o':
                    pygame.draw.circle(screen,red,(r1,r2),150,10)
                    board[number] = 'o'
                    shape = 'x'
                elif shape == 'x':
                    pygame.draw.lines(screen,red,False,[(r1,r2),(r1-150,r2+150),(r1+150,r2-150),(r1-150,r2-150),(r1+150,r2+150)],10)
                    board[number] = 'x'
                    shape = 'o'




    def listofdict(dictionary):
        values = list(dictionary.values())
        listoflist = np.array(np.split(np.array(values),3)).tolist()
        return listoflist

    def game_over(player):
        over_ = over.render(player + ' WINS',True, (0,0,0))
        screen.blit(over_, (350,350))


    def check_rows(board):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0
    def check_diagonals(board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[0+i][2-i] for i in range(len(board))])) ==1:
            return board[0][2]
        return 0
    def check_win(board):
        for newboard in [board,np.array(board).transpose().tolist()]:
            res = check_rows(newboard)
            if res:
                return res
        return check_diagonals(board)
    a = {1:'o',2:'x',3:'o',4:'x',5:'o',6:'x',7:'x',8:'o',9:'x',}

    print(check_win(listofdict((a))))





    bb = None

    t ='x'
    l='o'
    while carryOn:
        t,l = l,t
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bb = click()
                print(listofdict(board))
                print(check_win(listofdict(board)))

        if check_win(listofdict(board)) == 'x':
            display = over.render('X WINS',True,(255,105,180))
            screen.blit(display,(160,375))
            pygame.display.update()
        if check_win(listofdict(board)) == 'o':
            display = over.render('O WINS',True,(255,105,180))
            screen.blit(display,(160,375))
            pygame.display.update()

        square(bb)
        pygame.display.update()
