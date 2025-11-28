strings = []
isStop = False

strings.append(str(input("Enter first string: ")).lower())
if (strings[0].lower() == "quit"):
    isStop = True
else:
    while(isStop == False):
        string = str(input("Enter next string: ")).lower()
        if (string.lower() != "quit"):
            strings.append(string)
        elif (string.lower() == "quit"):
            isStop = True

    print(f"{strings.count("pearl")} pearls")
print("Bye!")
