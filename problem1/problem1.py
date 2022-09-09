output = open("output.txt", "a")
input = open("input.txt", "r")
for line in input:
    if line == "0 0":
        break
    space = line.index(" ")
    m = int(line[0:space])
    n = int(line[space+1:])
    value = str(pow(m,n))
    lastDigit = value[-1]
    output.write(f"{lastDigit}\n")

input.close()
output.close()