print("Vector Toolkit")

def print_vector(V):
    print(f"{V[0]}i + {V[1]}j + {V[2]}k")

a = int(input("How many vectors do you have (1 or 2) = "))

if a != 1 and a != 2:
    print("Invalid choice")

elif a == 1:
    print("Enter the vector:")
    x = float(input("Enter x component = "))
    y = float(input("Enter y component = "))
    z = float(input("Enter z component = "))
    A = [x, y, z]

    print("The vector is ", end="")
    print_vector(A)

    print("THE OPERATION YOU WANT TO PERFORM:")
    print("1) Magnitude (length)")
    print("2) Scalar Multiplication")
    print("3) Scalar Division")
    print("4) Normalization (making the vector have length 1)")

    b = int(input("Choose one of above (1,2,3,4) = "))

    if b == 1:
        magnitude = (x**2 + y**2 + z**2)**0.5
        print(f"The magnitude of the given vector is {magnitude}")

    elif b == 2:
        alpha = float(input("Enter the scalar alpha = "))
        x = x * alpha
        y = y * alpha
        z = z * alpha
        B = [x, y, z]

        print("The scalar multiplication is ", end="")
        print_vector(B)

    elif b == 3:
        alpha = float(input("Enter the scalar alpha = "))

        if alpha == 0:
            print("Division by zero is invalid")

        else:
            x = x / alpha
            y = y / alpha
            z = z / alpha
            B = [x, y, z]

            print("The scalar division is " , end="")
            print_vector(B)

    elif b == 4:
        magnitude = (x**2 + y**2 + z**2)**0.5

        if magnitude == 0:
            print("Cannot normalize the zero vector.")

        else:
            x = x / magnitude
            y = y / magnitude
            z = z / magnitude
            B = [x, y, z]

            print("The normalization is " , end="")
            print_vector(B)

    else:
        print("Invalid operation")

elif a == 2:

    print("Enter the first vector:")
    x1 = float(input("Enter x component = "))
    y1 = float(input("Enter y component = "))
    z1 = float(input("Enter z component = "))
    A = [x1, y1, z1]

    print("Enter the second vector:")
    x2 = float(input("Enter x component = "))
    y2 = float(input("Enter y component = "))
    z2 = float(input("Enter z component = "))
    B = [x2, y2, z2]

    print("The first vector is " , end="")
    print_vector(A)
    print("The second vector is " , end="")
    print_vector(B)

    print("THE OPERATION YOU WANT TO PERFORM:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Distance between vectors")
    print("4) Dot product")
    print("5) Cross product (3D)")

    c = int(input("Choose the operation: "))

    if c == 1:
        C = [A[i] + B[i] for i in range(len(A))]
        print("The addition of these two vectors is " , end="")
        print_vector(C)
    elif c == 2:
        C = [A[i] - B[i] for i in range(len(A))]
        print("The subtraction of these two vectors is " , end="")
        print_vector(C)
    elif c == 3:
        C = [A[i] - B[i] for i in range(len(A))]
        distance = (C[0]**2 + C[1]**2 + C[2]**2)**0.5
        print(f"The distance between these two vectors is {distance}")

    elif c == 4:
        C = [A[i] * B[i] for i in range(len(A))]
        dot_product = C[0] + C[1] + C[2]
        print(f"The dot product of these two vectors is {dot_product}")

    elif c == 5:
        x = (y1 * z2) - (z1 * y2)
        y = -(x1 * z2) + (z1 * x2)
        z = (x1 * y2) - (y1 * x2)

        C = [x, y, z]
        print("The cross product of these two vectors is ", end="")
        print_vector(C)


    else:
        print("Invalid operation")



