import numpy as np

grid = [[0,0,8,2,0,9,0,0,0],
        [1,0,0,0,0,0,0,0,0],
        [4,7,0,0,0,5,0,3,0],
        [0,0,5,0,0,0,0,0,1],
        [8,0,0,4,0,0,0,0,6],
        [0,2,0,8,0,0,0,0,0],
        [0,0,0,5,0,0,4,2,0],
        [0,0,7,0,0,0,9,0,0],
        [0,0,0,0,9,7,0,8,0]]

def possible_move(x, y, n):
    global grid
    for i in range(9):
        if grid[x][i] == n:
            return False
    for i in range(9):
        if grid[i][y] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[i + x0][j + y0] == n:
                return False
    return True


def solver():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible_move(x, y, n):
                        grid[x][y] = n
                        solver()
                        grid[x][y] = 0
                return
    print(np.matrix(grid))

def main():
    solver()

if __name__ == '__main__':
    main()
