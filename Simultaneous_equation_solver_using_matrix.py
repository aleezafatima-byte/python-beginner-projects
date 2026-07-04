print("Simultaneous Equation Solver (Matrix Inverse Method)")

print("\nEnter coefficients for the first equation:")
x1 = int(input("Enter x's coefficient: "))
y1 = int(input("Enter y's coefficient: "))
z1 = int(input("Enter constant: "))

print("\nEnter coefficients for the second equation:")
x2 = int(input("Enter x's coefficient: "))
y2 = int(input("Enter y's coefficient: "))
z2 = int(input("Enter constant: "))

# Coefficient matrix
A = [
    [x1, y1],
    [x2, y2]
]

# Constant matrix
B = [
    [z1],
    [z2]
]

# Calculate determinant
detA = x1 * y2 - y1 * x2

# Check if inverse exists
if detA == 0:
    print("\nThere is no unique solution because the determinant is zero.")

else:
    # Calculate inverse of A
    A_inverse = [
        [ y2 / detA, -y1 / detA],
        [-x2 / detA,  x1 / detA]
    ]

    # Multiply A_inverse × B
    X = [
        [A_inverse[0][0] * B[0][0] + A_inverse[0][1] * B[1][0]],
        [A_inverse[1][0] * B[0][0] + A_inverse[1][1] * B[1][0]]
    ]

    print("\nCoefficient Matrix (A):")
    print(A)

    print("\nConstant Matrix (B):")
    print(B)

    print("\nInverse Matrix (A⁻¹):")
    print(A_inverse)

    print("\nSolution Matrix (X):")
    print(X)

    print("\nSolution:")
    print("x =", X[0][0])
    print("y =", X[1][0])