time = input("Time: ")

while (len(time) != 4):
    print("Invalid time.")
    time = input("Time: ")

def binaryWatchGrid(time):
    grid = []
    for i in range(len(time)):
        digit = int(time[i])
        # order: 8, 4, 2, 1
        column = [".", ".", ".", "."]
        if digit >= 8:
            column[0] = "*"
            digit -= 8
        if digit >= 4:
            column[1] = "*"
            digit -= 4
        if digit >= 2:
            column[2] = "*"
            digit -= 2
        if digit >= 1:
            column[3] = "*"
            digit -= 1
        grid.append(column)
    return grid

def printGrid(grid):
    for i in range(4):
        print(f"{grid[0][i]} {grid[1][i]}  {grid[2][i]} {grid[3][i]}")

grid = binaryWatchGrid(time)
printGrid(grid)
    