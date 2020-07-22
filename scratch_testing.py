for i in range(9):
    for j in range(9):
        print(i, j)

list = [[(i,j) for j in range(9)] for i in range(9)]
print(list)