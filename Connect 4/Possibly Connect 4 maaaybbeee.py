import numpy as np
board = list(range(1,43))
new = (np.array(np.split(np.array(board),6)))
t = [0 for x in range(42)]
test = (np.array(np.split(np.array(t),6)))
# test[0,6] = 1
# test[1,5] = 1
# test[2,4] = 1
# test[3,3] = 1
print(np.count_nonzero(test == 1))
print(test)
# def index_finder(name_list, element):
#     return np.array(np.where(name_list == element))
# print(index_finder(new,1))

# print(new[1,0])
flipped = np.array(new[:,-1:-8:-1])
print(new)
def diagonal(board,num):
    loop = np.nditer(board[:3,0:4],flags = ['multi_index'])
    for x in loop:
        index = loop.multi_index
        diagonal_list = []
        for i in range(0,4):
            diagonal_list.append((board[index[0] + i, index[1] + i]))
        if diagonal_list.count(num) == 4:
            return True
    return False

def rows_columns(board,num):
    rows = np.count_nonzero(board == num, axis=1)
    columns = np.count_nonzero(board == num, axis=0)
    if 4 in rows:
        return True
    if 4 in columns:
        return True
    return False
test_flipped = np.array(test[:,-1:-8:-1])
print(test)
# print(diagonal(test_flipped,1))
player1 = 1
player2 = 2

while True:
    column_num = int(input("Enter a column to place your mark: ")) - 1
    position = np.amax(np.where(test[:,column_num] == 0))
    test[position,column_num] = player1
    print(test)
    if rows_columns(test, player1) or diagonal(test,player1) or diagonal(np.array(test[:,-1:-8:-1]),player1):
        print('player',player1,'wins')
        break
    player1, player2 = player2, player1


print(test[:,0])
print(np.amax(np.where(test[:,0] == 0)))





