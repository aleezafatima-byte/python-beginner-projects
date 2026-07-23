print("Root finder tool")

from math import *

print("From below choose any one method:")

print("1. Bisection Method")
print("2. Newton-Raphson Method")
print("3. Secant Method")

choice= int(input("Enter your choice (in integer only):"))

# Creating functions
def Bisection():

    try:
        function = input("Enter your function:")
        a = float(input("Enter lower limit:"))
        b = float(input("Enter upper limit:"))

        # Calculate f(a)
        x = a
        fa = eval(function)

        # Calculate f(b)
        x = b
        fb = eval(function)

        iterations = int(input("Enter the maximum iterations:"))

        # Check whether a root exists in the interval
        if fa * fb < 0:

            for i in range(iterations):

                # Midpoint
                c = (a + b) / 2

                # Calculate f(c)
                x = c
                fc = eval(function)

                # Check if root is found
                if fc == 0:
                    print(f"The root is: {c}")
                    break

                # Root lies in [a, c]
                elif fa * fc < 0:
                    b = c

                    # Since b changed, calculate new f(b)
                    x = b
                    fb = eval(function)

                # Root lies in [c, b]
                else:
                    a = c

                    # Since a changed, calculate new f(a)
                    x = a
                    fa = eval(function)

            else:
                print(f"Approximate root is: {c}")

        else:
            print("No root exists in the given interval.")

    except:
        print("Invalid function.")



def Newton_Raphson():

    try:
        function = input("Enter your function:")
        x0 = float(input("Enter your initial guess:"))
        df = input("Enter the derivative of function:")
        iteration = int(input("Enter the maximum iterations:"))

        for i in range(iteration):

            x = x0
            fx0 = eval(function)

            x = x0
            fy = eval(df)

            if fy != 0:

                xi = x0 - (fx0 / fy)

                x = xi
                fxi = eval(function)

                if fxi == 0:
                    print(f"The root is {xi}")
                    break

                else:
                    x0 = xi

            else:
                print("Derivative became zero. Newton-Raphson cannot proceed.")
                break

        else:
            print(f"Approximate root is: {xi}")

    except:
        print("Invalid function")

def Secant():

    try:
        function = input("Enter your function:")
        x0 = float(input("Enter your initial guess:"))
        x1 = float(input("Enter second guess:"))
        iteration = int(input("Enter the maximum iterations:"))

        for i in range(iteration):

            x = x0
            fx0 = eval(function)

            x = x1
            fx1 = eval(function)

            if fx1 - fx0 != 0:
                x2 = x1 - (fx1 *(x1 - x0))/(fx1 - fx0)

                x= x2
                fx2= eval(function)

                if fx2 == 0:
                    print(f"The root is {x2}")
                    break
                
                else:
                    x0=x1
                    x1=x2

            else:
                print("Denominator became zero. Secant Method cannot proceed.")
                break


        else:
            print(f"Approximate root is: {x2}")
            

    except:
        print("Invalid function")



if choice== 1:
    Bisection()

elif choice== 2:
    Newton_Raphson()

elif choice==3:
    Secant()

else:
    print("Invalid choice:")
