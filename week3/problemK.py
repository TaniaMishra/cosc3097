sequence = input("Sequence: ")

while (len(sequence) > 20 or len(sequence) % 2 != 0 or "?" not in sequence):
    print("Invalid sequence.")
    sequence = input("Sequence: ")

startingBrackets = []
endingBrackets = []
needToAdd = []
unknown = []

def checkEnding(index, item):
    endPair = ""
    startPair = ""
    if (item == "?"):
        unknown.append(index)
    elif (item == "("):
        startingBrackets.append(index)
        endPair = ")"
    elif (item == "["):
        startingBrackets.append(index)
        endPair = "]"
    elif (item == "{"):
        startingBrackets.append(index)
        endPair = "}"
    elif (item == "<"):
        startingBrackets.append(index)
        endPair = ">"
    elif (item == ")"):
        if (index not in endingBrackets):
            endingBrackets.append(index)
        startPair = "("
    elif (item == "]"):
        if (index not in endingBrackets):
            endingBrackets.append(index)
        startPair = "["
    elif (item == "}"):
        if (index not in endingBrackets):
            endingBrackets.append(index)
        startPair = "{"
    elif (item == ">"):
        if (index not in endingBrackets):
            endingBrackets.append(index)
        startPair = "<"

    if (endPair != "" and endPair not in sequence and sequence.index(endPair) in endingBrackets):
        needToAdd.append(index)
    
    if (startPair !=  "" and startPair in sequence and sequence):
        if (item in needToAdd):
            needToAdd.remove(item)
        if (startPair not in sequence):
            needToAdd.append(index)


for i in range(len(sequence)):
    checkEnding(i, sequence[i])
    print(f"{sequence[i]}:\n Starting Brackets: {startingBrackets}, Ending Brackets: {endingBrackets}, Need To Add: {needToAdd}, Uknowns: {unknown}")


