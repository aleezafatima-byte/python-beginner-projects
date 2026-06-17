print("FACTORIAL CALCULATOR")

n=int(input("enter n="))

if n== 0:
    print("Factorial of 0 (0!) is 1")
elif n<0:
    print(" Invalid!")
elif n>0:
    factorial= 1
    for i in range(1,n+1):
        factorial=factorial * i
    print("factorial of n is n!=", factorial)



