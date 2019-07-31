#Conway Game of Life creating Copperhead


import numpy as np
import pylab as plt
import matplotlib.animation as animation

fig = plt.figure()
N = 25
X = int(input("How may transition you would like to do: "))
f1 =\
[[0, 1, 1, 0, 0, 1, 1, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[1, 0, 1, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 1],
[0, 1, 1, 0, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0]]

board = np.zeros([N,N], dtype = int)
board[7:19,6:14] = f1


def plot(board):
    im = plt.imshow(board, cmap = 'binary', animated = True)
    return im

def check(board,row,col):
    sum = 0
    for pos in [(row+1,col), (row+1,col+1), (row,col+1), (row-1,col+1), (row-1,col), (row-1, col-1), (row,col-1), (row+1,col-1)]:
        try:
            if board[pos[0]][pos[1]] == 1:
                sum +=1
        except:
            pass
    return sum


ims = []
for i in range(X):
    v = []
    for rows in range(N):
        for columns in range(N):
            if board[rows][columns]  == 0 and check(board,rows,columns) == 3:
                v.append([rows,columns,1])
            elif board[rows][columns] == 1 and (check(board,rows,columns) < 2 or check(board,rows,columns) > 3):
                v.append([rows,columns,0])
    for i in v:
        board[i[0]][i[1]] = i[2]
    ims.append([plot(board)])

ani = animation.ArtistAnimation(fig, ims, interval = 100, repeat_delay = 1000)

plt.show()
