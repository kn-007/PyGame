import time, pygame

pygame.init()

BOARD_SUBOX_LEN = 3
TOTAL = BOARD_SUBOX_LEN ** 2
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]

board_is_highlighted = [[False for x in range(9)] for y in range(9)]

black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
WIDTH = 700
HEIGHT = 700
EXTRA_SPACE = 100
INCREMENT_X = int(WIDTH/TOTAL)
INCREMENT_Y = int(HEIGHT/TOTAL)
GRID_THICKNESS = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT+EXTRA_SPACE))
screen.fill((255,255,255))
carryOn = True
courier_new = pygame.font.Font('couriernewbold.ttf',100)
time_font = pygame.font.Font('couriernewbold.ttf',90)

def draw_grid():
    for x in range(1, TOTAL):
        if x % BOARD_SUBOX_LEN == 0:
            pygame.draw.line(screen, red, (0, (INCREMENT_X) * x), (WIDTH, (INCREMENT_X) * x), GRID_THICKNESS)
            pygame.draw.line(screen, red, ((INCREMENT_Y) * x, 0), ((INCREMENT_Y) * x, HEIGHT), GRID_THICKNESS)
        else:
            pygame.draw.line(screen,black,(0, (INCREMENT_X) * x),(WIDTH, (INCREMENT_X) * x), GRID_THICKNESS)
            pygame.draw.line(screen, black, ((INCREMENT_Y) * x, 0), ((INCREMENT_Y) * x, HEIGHT), GRID_THICKNESS)



def cube_corner_finder(y,x):
    return INCREMENT_X * x, INCREMENT_Y * y
    
    

def cube_num_placer():
    for i in range(TOTAL):
        for j in range(TOTAL):
            if board[i][j] != 0:
                num = courier_new.render(str(board[i][j]), True, (0, 0, 0))
                x,y = cube_corner_finder(i,j)
                screen.blit(num,(x+15,y))

def click_checker():
    position = pygame.mouse.get_pos()
    # if 0 <= position[0] <= WIDTH and HEIGHT <= position[1] <=  HEIGHT + EXTRA_SPACE:
    #     return position
    #     print("Can't click here")
    for i in range(TOTAL):
        for j in range(TOTAL):
            corner_coordinate = cube_corner_finder(i,j)
            if corner_coordinate[0] <= position[0] <= corner_coordinate[0] + INCREMENT_X and corner_coordinate[1] <= position[1] <= corner_coordinate[1] + INCREMENT_Y:
                return i,j #Returned i,j assuming top left corner square is (0,0)



def square_highlighter_bool(y,x):
    cube_corner = cube_corner_finder(y,x)
    # adjusted_corner = (cube_corner[0] + GRID_THICKNESS,cube_corner[1] + GRID_THICKNESS)
    # end_rect_corner = (adjusted_corner[0] + INCREMENT_X - (GRID_THICKNESS * 2), adjusted_corner[1] + INCREMENT_Y - (GRID_THICKNESS * 2))
    for i in range(9):
        for j in range(9):
            if board_is_highlighted[i][j]:
                board_is_highlighted[i][j] = False
    board_is_highlighted[y][x] = True

def square_highlighter_draw():
    for i in range(9):
        for j in range(9):
            if board_is_highlighted[i][j]:
                pygame.draw.rect(screen, blue, cube_corner_finder(i,j) + (INCREMENT_X,INCREMENT_Y), 10)

def highlighted_square_updater(num):
    for i in range(9):
        for j in range(9):
            if board_is_highlighted[i][j] and board[i][j] == 0:
                board[i][j] = num


start = time.time()

def time_display():
    global start
    elapsed_time = int(time.time() - start)
    clock = time.strftime("%M:%S", time.gmtime(elapsed_time))
    current_time = time_font.render(str(clock), True, (0, 0, 0))
    screen.blit(current_time, (600, 900))



def window_update():
    screen.fill((255,255,255))
    draw_grid()
    cube_num_placer()
    square_highlighter_draw()
    time_display()

while carryOn:
    window_update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_y, pos_x = click_checker()
            print(pos_y,pos_x)
            square_highlighter_bool(pos_y,pos_x)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                highlighted_square_updater(1)
            if event.key == pygame.K_2:
                highlighted_square_updater(2)
            if event.key == pygame.K_3:
                highlighted_square_updater(3)
            if event.key == pygame.K_4:
                highlighted_square_updater(4)
            if event.key == pygame.K_5:
                highlighted_square_updater(5)
            if event.key == pygame.K_6:
                highlighted_square_updater(6)
            if event.key == pygame.K_7:
                highlighted_square_updater(7)
            if event.key == pygame.K_8:
                highlighted_square_updater(8)
            if event.key == pygame.K_9:
                highlighted_square_updater(9)
    pygame.display.update()

