sum = 0

x = int(input("Enter an integer: "))

if x <= 0:
    print("Nothing to be printed")
else:
    for i in range (x, 0, -1):
        sum = sum + i
        print(i, end=" ")
    print(f"\nThe sum is {sum}")