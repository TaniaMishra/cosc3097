alice_nums = input("Alice's Cards (card1 card2): ")
a1 = -1
a2 = -1
if (int(alice_nums[0]) > int(alice_nums[2])):
    a1 = int(alice_nums[2])
    a2 = int(alice_nums[0])
else:
    a1 = int(alice_nums[0])
    a2 = int(alice_nums[2])
a1_check = False
a2_check = False


order = input("Card Order: ")    

output = ""

if order[0] == "B" and (order[1] == "A" and a1 > 2):
    output = "-1"
elif order[0] == "B" and order[1] == "B" and a1 > 3:
    output = "-1"
else:
    next_card = a1
    numbers = []
    for i in range(len(order)):
        if order[i] == "A":
            if a1_check == False:
                if a1 == next_card:
                    numbers.append(next_card)
                    next_card = a1 + 1
                    a1_check = True
                else:
                    output = "-1"
                    break
            else:
                if a2 == next_card:
                    numbers.append(next_card)
                    next_card = a2 + 1
                    a1_check = True
                else:
                    output = "-1"
                    break
        else:
            numbers.append(next_card)
            next_card += 1

if (output == "-1"):
    print(output)
else:
    print(f"{numbers[1]} {numbers[2]}")