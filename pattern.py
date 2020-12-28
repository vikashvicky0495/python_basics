n = int(input("Enter the limit for row"))

for i in range(0, n):
    for j in range(0, i):
        print("*", end="")
    print("\r")
