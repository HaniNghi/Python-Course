femaleStudent = int(input("Enter the number of female students: "))
maleStudent = int(input("Enter the number of male students: "))

print("")

if femaleStudent == 0 & maleStudent == 0 :
    print("Female: 0.0 %")
    print("Male: 0.0 %")
else:
    print(f"Female: {femaleStudent/(femaleStudent+maleStudent)*100:.1f} %")
    print(f"Male: {maleStudent/(femaleStudent+maleStudent)*100:.1f} %")
