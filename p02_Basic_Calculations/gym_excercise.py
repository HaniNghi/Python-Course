day = int(input("Enter the number of days of gym visits per year: "))
dayPassPrice = float(input("Enter price for a day pass: "))
yearlyFee = float(input("Enter yearly membership fee: "))

dayPassCal = day * dayPassPrice

print("")

if dayPassCal < yearlyFee:
    print(f"Buying day passes is {yearlyFee - dayPassCal:.2f} euros cheaper")
elif dayPassCal > yearlyFee :
    print(f"Paying the yearly membership fee is {dayPassCal - yearlyFee:.2f} euros cheaper")
else:
    print("There is no price difference")