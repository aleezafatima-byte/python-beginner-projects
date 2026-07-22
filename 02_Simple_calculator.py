print('SIMPLE CALCULATOR')

print("1.Addition +")
print("2. Substraction -")
print("3. Multiplication *")
print("4. Division /")
print("5. Power ^")
print("6. Percentage %")
print("7. Remainder r")

Choice= int(input("choose one option(1-6):"))

Value1 = float(input("Enter value 1:"))
Value2 = float(input("Enter value 2:"))

if Choice ==1 :
    Addition = Value1 + Value2
    print(Value1, '+', Value2,'=', Addition)

elif Choice ==2 :
    Substraction = Value1 - Value2
    print(Value1, '-', Value2,'=', Substraction)

elif Choice ==3 :
    Multiplication = Value1 * Value2
    print(Value1, '*', Value2,'=', Multiplication)

elif Choice ==4 :
    if Value2 == 0:
        print("Cannot divide by zero!")

    else :
        Division = Value1 / Value2
        print(Value1, '/', Value2, '=', Division)

elif Choice ==5 :
    Power = Value1 ** Value2
    print(Value1, '^', Value2,'=', Power)

elif Choice ==6 :
    Percentage = Value1 / Value2 * 100
    print(Value1, '%', Value2,'=', Percentage)

elif Choice ==7 :
    Remainder = Value1 % Value2
    print(Value1, 'r', Value2,'=', Remainder)

else :
    print("Invalid value!")

