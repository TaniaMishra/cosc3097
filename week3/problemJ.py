n = int(input("Grid Size: "))
while ((n < 2 and n > 24) or (n%2 != 0)):
    print("Invalid size")
    n = int(input("Grid Size: "))

grid = []
for num in range(n):
    row = input(f"Row {num}: ")
    while (len(row) != n):
        print("Invalid row")
        row = input(f"Row {num}: ")
    grid.append(row)

def check_squares(values):
    # No row or column has 3 or more consecutive squares of the same color
    if ("BBB" in values or "WWW" in values):
        return False
    # Every row or column has the same number of black squares as it has white squares
    black = 0
    white = 0
    for square in values:
        if square == "B":
            black += 1
        elif square == "W":
            white += 1
    if black == white:
        return True
    return False

correct_grid = True
# check rows
for row in grid:
    if (not check_squares(row)):
        correct_grid = False
        break
# check columns
for num in range(n):
    if (not correct_grid):
        break
    col = ""
    for row in grid:
        col = col + row[num]
    if (not check_squares(col)):
        correct_grid = False
        break

if correct_grid:
    print("Output: 1")
else:
    print("Output: 0")