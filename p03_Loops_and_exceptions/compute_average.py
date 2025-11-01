first_number = float(input("Enter first number: "))
sum = first_number
count = 1

if first_number == 0:
    print("Nothing to be calculated")
else:
    next_number = float(input("Enter next number: "))
    while(next_number != 0):
        sum = sum + next_number
        next_number = float(input("Enter next number: "))
        count +=1
    print(f"The average is {sum/count:.2f}")