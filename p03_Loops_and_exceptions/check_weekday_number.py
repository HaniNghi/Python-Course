input = input("Enter a weekday number: ")
try:
    integer = int(input)
    if integer in range(1,8):
        print("OK")
    else:
        print("Please enter an integer between 1 and 7")
except ValueError:
        print("Please enter an integer between 1 and 7")


