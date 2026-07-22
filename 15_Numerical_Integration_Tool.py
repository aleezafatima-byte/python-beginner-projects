print("Nmerical Integration Tool")

from math import *

print("Choose the method you would like to use from the following:")

print("1. Trapezoidal Rule")
print("2. Simpson's 1/3 Rule")
print("3. Simpson's 3/8 Rule")

choice=int(input("Enter your choice:"))

#Creating functions
def trapezoidal():
    
    print("\n Trapezoidal Rule: ")

    function = input("Enter function f(x): ")
    a = float(input("Enter lower limit (a): "))
    b = float(input("Enter upper limit (b): "))

    try:
        x = a
        fa = eval(function)

        x = b
        fb = eval(function)

        integral = (b - a) * (fa + fb) / 2

        print(f"\nApproximate Integral = {integral}")

    except:
        print("Invalid function!")


def simpson_one_third():

    print("\n Simpson's 1/3 Rule: ")

    function = input("Enter function f(x): ")
    a = float(input("Enter lower limit (a): "))
    b = float(input("Enter upper limit (b): "))

    try:
        x = a
        fa = eval(function)

        x = b
        fb = eval(function)

        m = (a + b) / 2

        x = m
        fm = eval(function)

        h = (b - a) / 2

        integral = (h / 3) * (fa + 4 * fm + fb)

        print(f"\nApproximate Integral = {integral}")

    except:
        print("Invalid function!")


def simpson_three_eight():

    print("\n--- Simpson's 3/8 Rule ---")

    function = input("Enter function f(x): ")
    a = float(input("Enter lower limit (a): "))
    b = float(input("Enter upper limit (b): "))

    try:
        h = (b - a) / 3

        x = a
        fa = eval(function)

        x1 = a + h
        x = x1
        fx1 = eval(function)

        x2 = a + 2 * h
        x = x2
        fx2 = eval(function)

        x = b
        fb = eval(function)

        integral = (3 * h / 8) * (fa + 3 * fx1 + 3 * fx2 + fb)

        print(f"\nApproximate Integral = {integral}")

    except:
        print("Invalid function!")


if choice==1:
    #Trapezoidal rule
    trapezoidal()

elif choice==2:
    # Simpson 1/3 Rule
    simpson_one_third()

elif choice==3:
    #Simpson 3/8 Rule
    simpson_three_eight()


else:
    print("Invalid choice!")
