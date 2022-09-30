n = int(input("N: "))
while (n < 1 or n > 10):
    print("Invalid N value.")
    n = int(input("N: "))

if (n % 4 == 0):
    print("Even")
elif (n % 4 == 1 or n % 4 == 3):
    print("Either")
elif (n % 4 == 2):
    print("Odd")

# 1 - either
# 2 - odd
# 3 - either
# 4 - even
# 5 - either
# 6 - odd
# 7 - either
# 8 - even
