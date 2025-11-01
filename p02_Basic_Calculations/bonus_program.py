price = float(input("Enter the car's selling price: "))

if price < 50000:
    saleBonus = price * 1/100
else :
    saleBonus = price * 1.5/100

if saleBonus < 200:
    saleBonus = 200

print(f"The bonus is {saleBonus:.2f} euros.")
