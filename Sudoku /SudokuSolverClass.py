import numpy as np
import math
class Solver:
    def __init__(self, board, total_len):
        self.total_len = total_len
        self.sub_box_len = int(math.sqrt(total_len))
        self.board = board

    def open_board(self):
        for y in range(self.total_len):
            for x in range(self.total_len):
                if self.board[y][x] == 0:
                    return y, x
        return False

    def possible(self, y, x, num):
        for i in range(self.total_len):
            if self.board[y][i] == num and i != x:
                return False
            if self.board[i][x] == num and i != y:
                return False
        box_y = (y // self.sub_box_len) * self.sub_box_len
        box_x = (x // self.sub_box_len) * self.sub_box_len
        for i in range(box_y, box_y + self.sub_box_len):
            for j in range(box_x, box_x + self.sub_box_len):
                if self.board[i][j] == num:
                    return False
        return True


    def solve_board(self):
        if self.open_board() is False:
            return True
        else:
            i, j = self.open_board()
            for num in range(1, self.total_len + 1):
                if self.possible(i, j, num):
                    self.board[i][j] = num
                    if self.solve_board():
                        return True

            self.board[i][j] = 0
        return False
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
solved = Solver(board, 9)
print(solved.solve_board())
print(solved.board)