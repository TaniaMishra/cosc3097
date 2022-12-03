tower = input()

left_bars = 0
right_bars = 0
for char in tower:
    if char == "(":
        break
    elif char == "|":
        left_bars += 1

eye_end = tower.index(")")

for char in tower[eye_end:]:
    if char == "|":
        right_bars += 1

if left_bars == right_bars:
    print("Correct")
else:
    print("Fix")