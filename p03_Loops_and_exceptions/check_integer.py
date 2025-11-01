input = input("Enter an integer: ")
try:
    integer = int(input)
    print("OK")
except ValueError:
    print(f"'{input}' is not an integer")