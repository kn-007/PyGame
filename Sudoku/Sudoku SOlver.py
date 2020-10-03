import numpy as np
import time
start = time.process_time()
BOARD_LEN = 3
TOTAL = BOARD_LEN ** 2
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

# board = [
#     [4,3,0,0],
#     [1,2,3,0],
#     [0,0,2,0],
#     [2,1,0,0]
# ]
def open_board():
    global board
    for y in range(TOTAL):
        for x in range(TOTAL):
            if board[y][x] == 0:
                return y,x
    return False

def possible(y,x,num):
    global board
    for i in range(TOTAL):
        if board[y][i] == num and i != x:
            return False
        if board[i][x] == num and i != y:
            return False
    box_y = (y//BOARD_LEN) * BOARD_LEN
    box_x = (x//BOARD_LEN) * BOARD_LEN
    for i in range(box_y, box_y + BOARD_LEN):
        for j in range(box_x, box_x + BOARD_LEN):
            if board[i][j] == num:
                return False
    return True

print(possible(0,3,1))


def solve_board():
    global board
    if open_board() is False:
        return True
    else:
        i,j = open_board()
        for num in range(1, TOTAL + 1):
            if possible(i,j,num):
                board[i][j] = num
                if solve_board():
                    return True

        board[i][j] = 0
    return False

solve_board()
print(np.array(board))
print(f"Consumed: {time.process_time() - start}")
