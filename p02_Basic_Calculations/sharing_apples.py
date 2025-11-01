apple = int(input("How many apples? "))
children = int(input("How many children? "))

print("")

print(f"Each child will get {apple//children:.0f} apples.")
print(f"There will be {apple%children} leftover apples.")

