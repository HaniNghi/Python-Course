try:
    price = float(input("Enter price: "))
    priceIncludedVat = price * 1.24

    print(f"The price with VAT is {priceIncludedVat:.2f}")
except ValueError:
    print("Invalid price")