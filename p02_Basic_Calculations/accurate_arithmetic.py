from decimal import Decimal

firstNumber = Decimal(input("Enter first number: "))
secondNumber = Decimal(input("Enter second number: "))

sum = firstNumber + secondNumber

print("")
print(f"{firstNumber} + {secondNumber} = {sum}")