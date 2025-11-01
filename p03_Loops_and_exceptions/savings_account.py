interest_rate = float(input("Enter interest rate: "))
tax_rate = float(input("Enter capital income tax rate: "))
deposit = float(input("Enter initial deposit: "))
year = int(input("Enter number of years: "))
print()
balance = deposit
for i in range(1, year +1):
    balance = balance + interest_rate/100*(1-tax_rate/100)*balance
    print(f"Year {i}: {balance:.2f}" )