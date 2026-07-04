print("Simultaneous equation solver")

print("Enter coefficients for first equation:")

a= int(input("enter x's coefficient:"))
b= int(input("enter y's coefficient:"))
c= int(input("enter constant:"))

print("Enter coefficients for second equation:")

p= int(input("enter x's coefficient:"))
q= int(input("enter y's coefficient:"))
r= int(input("enter constant:"))

print("\nThe equations are:")
print(f"{a}x + {b}y = {c}")
print(f"{p}x + {q}y = {r}")

determinant = a*q - b*p

if determinant == 0:
    print("There is no unique solution.")
else:
    x = (c*q - b*r) / determinant
    y = (a*r - c*p) / determinant

