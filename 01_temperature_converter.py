# temperature convertor

temp = float(input("Enter temperature in Celsius: "))

print("1. Convert to Fahrenheit")
print("2. Convert to Kelvin")

choice = input("Enter choice: ")

if choice == "1":
    print("Fahrenheit =", (9/5) * temp + 32)

elif choice == "2":
    print("Kelvin =", temp + 273.15)

else:
    print("Invalid choice")
