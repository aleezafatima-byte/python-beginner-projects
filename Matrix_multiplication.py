rows1=int(input("enter no of rows in first matrix:"))
column1=int(input("enter no of columns in first matrix:"))

matrix1=[]

for i in range(rows1):
    a=[]
    for j in range(column1):
        x=int(input("enter value of element:"))
        a.append(x)
    matrix1.append(a)

for i in range(rows1):
    for j in range(column1):
        print(matrix1[i][j],end=" ")
    print()

rows2=int(input("enter no of rows in second matrix:"))
column2=int(input("enter no of columns in second matrix:"))

matrix2=[]

for k in range(rows2):
    b=[]
    for l in range(column2):
        y=int(input("enter value of element:"))
        b.append(y)
    matrix2.append(b)

for k in range(rows2):
    for l in range(column2):
        print(matrix2[k][l],end=" ")
    print()

if column1==rows2:

    matrix_multiply=[]

    for i in range(rows1):

        c=[]

        for l in range(column2):

            z=0

            for j in range(column1):

                z=z+(matrix1[i][j]*matrix2[j][l])

            c.append(z)

        matrix_multiply.append(c)

    print("multiplication matrix is")

    for i in range(rows1):
        for l in range(column2):
            print(matrix_multiply[i][l],end=" ")
        print()

else:
    print("matrix multiplication not possible")