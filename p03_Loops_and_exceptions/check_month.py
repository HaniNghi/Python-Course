isOk = False

while isOk == False:
    input_month = input("Enter a month number: ")
    try:
        month_number = int(input_month)
        if month_number in range (1, 13):
            print("OK")
            isOk = True
        else:
            print(f"{month_number} is not a valid month number")
            print("")
    except ValueError:
        print(f"'{input_month}' is not a valid month number")
        print("")
