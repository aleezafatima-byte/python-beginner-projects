print('Length UNIT CONVERTOR')

print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Meters to Feet")
print("4. Feet to Meters")

choice= int(input('choose one option(1-4):'))

if choice== 1 :
    km= float(input('Enter length in Kilometer:'))
    miles = km * 0.621371
    print('Length in Miles:',miles)

elif choice== 2 :
    miles= float(input('Enter length in miles:'))
    km = miles / 0.621371
    print("Length in kilometer:", km)

elif choice== 3 :
    Meters= float(input('Enter length in meters:'))
    Feet= Meters * 3.28084
    print("Length in feet:", Feet)

elif choice== 4 :
    Feet= float(input('Enter length in feet:'))
    Meters= Feet / 3.28084
    print("Length in meters:", Meters)
else:
    print("Invalid choice!")
