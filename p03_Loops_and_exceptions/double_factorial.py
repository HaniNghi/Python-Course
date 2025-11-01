input = input("Enter a non-negative integer: ")
result = 1

integer = int(input)
if integer < 0:
    print("Please enter a non-negative integer")
else:
    if integer%2==0:
        for i in range (2, integer +1,2):
            result =  result*i
    else:
        for i in range (3, integer + 1, 2):
            result = result*i
    print(f"{integer}!! = {result}")