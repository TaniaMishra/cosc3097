def isValidSolution(solution):
    # Check rows
    for row in solution:
        validRow = checkPart(row)
        if not validRow:
            return False
    # Check columns
    for i in range(4):
        col = [solution[0][i], solution[1][i], solution[2][i], solution[3][i]]
        validCol = checkPart(col)
        if not validCol:
            return False
    # Check boxes
    for i in range(0, 4, 2):
        box = [solution[i][0], solution[i][1], solution[i+1][0], solution[i+1][1]]
        validBox = checkPart(box)
        if not validBox:
            return False
        box = [solution[i][2], solution[i][3], solution[i+1][2], solution[i+1][3]]
        validBox = checkPart(box)
        if not validBox:
            return False
    # if none of the checks were false, then the solution is valid
    return True

def checkPart(part):
    if "1" in part and "2" in part and "3" in part and "4" in part:
        return True
    else:
        return False

testCases = input("Number of Test Cases: ")
solution = []
output = ""
for t in range(int(testCases)):
    solution = []
    row = input()
    solution.append(row.split(" "))
    row = input()
    solution.append(row.split(" "))
    row = input()
    solution.append(row.split(" "))
    row = input()
    solution.append(row.split(" "))
    if isValidSolution(solution):
        output = output + "Valid\n"
    else:
        output = output + "Invalid\n"

print(output)