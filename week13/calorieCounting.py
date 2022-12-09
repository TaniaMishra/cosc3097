calories = open("calories.txt", "r")

total_cals = []
sum = 0
for line in calories:
    if line == "\n":
        total_cals.append(sum)
        sum = 0
    else:
        sum += int(line)

greatest = total_cals[0]
for elf_cal in total_cals:
    if elf_cal > greatest:
        greatest = elf_cal

print(greatest)
calories.close()