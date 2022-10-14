t = int(input("Number of Test Cases: "))
harvests = []

for case in range(t):
    harvests.append(input("Harvest: "))

def isGoodHarvest(harvest):
    corn = 0
    potato = 0
    zuchinni = 0
    rotten = 0
    for crop in harvest:
        if crop == "C":
            corn += 1
        if crop == "P":
            potato += 1
        if crop == "Z":
            zuchinni += 1
        if crop == "R":
            rotten += 1
    total_crops = corn + potato + zuchinni + rotten
    rotten_percent = (rotten / total_crops) * 100
    if corn < 2 or potato < 4 or zuchinni < 5 or total_crops < 15 or rotten_percent > 10:
        return False
    return True


for harvest in harvests:
    if isGoodHarvest(harvest):
        print("This year's harvest is good!")
    else:
        print("This year's harvest is bad!")

