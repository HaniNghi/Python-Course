gig = int(input("Number of gigs: "))
gigPerString = int(input("Gigs to be played with the same set of strings: "))
setPrice = float(input("Price of a set of guitar strings: "))

print("")
if gig%gigPerString == 0:
    print(f"The guitarist needs {gig//gigPerString} new sets of guitar strings")
    print(f"The total cost is {setPrice*(gig//gigPerString):.2f} euros")
else :
    print(f"The guitarist needs {gig//gigPerString + 1} new sets of guitar strings")
    print(f"The total cost is {setPrice*(gig//gigPerString + 1):.2f} euros")