"""
    _______            ______
|_   __ \         .' ___  |
  | |__) |_   __ / .'   \_|  ,--.   _ .--..--.  .---.
  |  ___/[ \ [  ]| |   ____ `'_\ : [ `.-. .-. |/ /__\\
 _| |_    \ '/ / \ `.___]  |// | |, | | | | | || \__.,
|_____| [\_:  /   `._____.' \'-;__/[___||__||__]'.__.'
         \__.'
"""
import math
import pygame
import time
import numpy as np
from SudokuSolverClass import solver

pygame.init()
pygame.font.init()
start = time.time()

solver = Solver([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 9)


class Grid:
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    def __init__(self, rows, columns, width, height, extra_gap):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.strikes = 0
        self.extra_gap = extra_gap
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(columns)]
                      for i in range(rows)]
        self.start = time.time()
        self.prev_time = 0
        self.test = 0

    def draw(self, window):
        increment_x = self.width // self.columns
        increment_y = self.height // self.rows
        subBox = math.sqrt(self.rows)
        for x in range(1, self.rows):
            thick = 10 if x % subBox == 0 else 3
            pygame.draw.line(window, (0, 0, 0), (0, increment_x * x), (self.width, increment_x * x), thick)
            pygame.draw.line(window, (0, 0, 0), (increment_y * x, 0), (increment_y * x, self.height), thick)
        for row in self.cubes:
            for cube in row:
                cube.draw(window)
        fntSize = int(self.extra_gap * 1.2307692308)
        font = pygame.font.SysFont('Courier New Bold', fntSize)
        strike_display = font.render(str("X") * self.strikes, True, (255,20,147))
        window.blit(strike_display, (0, self.height - 10))

        if self.complete_board():
            font = pygame.font.Font('couriernewbold.ttf', 100)
            win_dis = font.render("COMPLETE:(", True, (0,0,128))
            window.blit(win_dis, (0, 200))



    def complete_board(self):
        complete = True
        for row in self.cubes:
            for cube in row:
                if cube.value == 0:
                    complete = False
                    break
        return complete

    def solve_board(self, solve_bool, window):
        half_sec_time = round(time.time() - self.start, 1)
        if self.prev_time + .5 == half_sec_time:
            print(half_sec_time)
            self.prev_time += .5
            if solve_bool:
                solved_board = Solver(self.board, self.rows)
                solved_board.solve_board()
                self.clearSelect()
                for i in range(self.rows):
                    for j in range(self.columns):
                        cur_cube = self.cubes[i][j]
                        if cur_cube.value == 0:
                            cur_cube.change_val(solved_board.board[i][j])
                            break


    def time_display(self, window):
        elapsed_time = int(time.time() - self.start)
        clock = time.strftime("%M:%S", time.gmtime(elapsed_time))
        fntSize = int(EXTRA_GAP * 1.2307692308)
        font = pygame.font.Font('couriernewbold.ttf', fntSize)
        cur_time = font.render(str(clock), True, (255, 20, 147))
        window.blit(cur_time, (SCREEN_WIDTH - 245, SCREEN_HEIGHT - 10))
        test_time = round(time.time() - self.start, 1)
        # if self.test + .5 == test_time:
        #     print(test_time)
        #     self.test += .5

    def clearSelect(self):
        for row in self.cubes:
            for cube in row:
                cube.selected = False
                cube.temp = 0

    def highlight(self, window, pos_x, pos_y, key):
        self.clearSelect()
        for row in self.cubes:
            for cube in row:
                cube.select(window, pos_x, pos_y, key)

    def confirm_place(self):
        model = []
        num_placed, placed_y, placed_x = 0, 0, 0
        for i in range(self.rows):
            cur_row = []
            for j in range(self.columns):
                if self.cubes[i][j].value != 0 or self.cubes[i][j].value == 0 and self.cubes[i][j].temp == 0:
                    cur_row.append(self.cubes[i][j].value)
                elif self.cubes[i][j].value == 0 and self.cubes[i][j].temp != 0:
                    print(f"This num was placed amirite? {self.cubes[i][j].temp}")
                    num_placed = self.cubes[i][j].temp
                    placed_y, placed_x = i, j
                    cur_row.append(self.cubes[i][j].temp)
            model.append(cur_row)

        possible_placement = Solver(self.board, self.rows)
        possible_solve = Solver(model, self.rows)
        if possible_placement.possible(placed_y, placed_x, num_placed) and possible_solve.solve_board():
            self.cubes[placed_y][placed_x].change_val(self.cubes[placed_y][placed_x].temp)
            self.clearSelect()
        else:
            self.strikes += 1




class Cube:
    totalRows = 9
    totalColumns = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.temp = 0
        self.selected = False
        self.increment_x = self.width / self.totalColumns
        self.increment_y = self.height / self.totalRows
        self.top_left_corner = (self.col * self.increment_x, self.row * self.increment_y)

    def draw(self, window):
        fntAdjust = int(self.width / 60)
        if self.value != 0:
            fntSize = int(self.width / 9.2307692308)
            font = pygame.font.Font('couriernewbold.ttf', fntSize)
            num = font.render(str(self.value), True, (0, 0, 0))
            window.blit(num, (self.increment_x * self.col + fntAdjust, self.increment_y * self.row))
        elif self.value == 0 and self.temp != 0:
            fntSize = int(self.width / 12.7659574468)
            font = pygame.font.Font('couriernewbold.ttf', fntSize)
            num = font.render(str(self.temp), True, (255, 0, 0))
            window.blit(num, (self.increment_x * self.col + fntAdjust, self.increment_y * self.row))

    def select(self, window, pos_x, pos_y, key):
        bottom_right_corner = (self.top_left_corner[0] + self.increment_x, self.top_left_corner[1] + self.increment_y)
        thick = 5
        if self.top_left_corner[0] <= pos_x <= bottom_right_corner[0] and self.top_left_corner[1] <= pos_y <= \
                bottom_right_corner[1]:
            pygame.draw.rect(window, (0, 0, 255),
                             (self.top_left_corner[0], self.top_left_corner[1], self.increment_x, self.increment_y),
                             thick)
            self.selected = True
            self.temp = key

    def change_val(self, num):
        self.value = num

    def change_temp(self, num):
        self.temp = num




SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
EXTRA_GAP = 65
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + EXTRA_GAP))
window.fill((255, 255, 255))
board = Grid(9, 9, SCREEN_WIDTH, SCREEN_HEIGHT, EXTRA_GAP)

carryOn = True
pos_x, pos_y = -100, -100
key = 0
solve = False

while carryOn:
    window.fill((255, 255, 255))
    board.draw(window)
    board.solve_board(solve, window)
    board.time_display(window)
    board.highlight(window, pos_x, pos_y, key)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            key = 0
            pos_x, pos_y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9
            if event.key == pygame.K_ESCAPE:
                # print("esc pressed")
                key = 0
                board.clearSelect()
            if event.key == pygame.K_RETURN:
                # print("return pressed")
                board.confirm_place()
            if event.key == pygame.K_SPACE:
                print("space pressed")
                solve = True
    pygame.display.update()
