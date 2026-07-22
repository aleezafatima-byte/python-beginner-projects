print("DOT PRODUCT CALCULATOR")

print("For vector compoenents:")

dim=(int(input("The dimension of vectors=")))

a=[]
b=[]

for i in range(dim):
    x= float(input("enter compoenents of first vector="))
    a.append(x)
       
for j in range(dim):
    y= float(input("enter compoenents of second vector="))
    b.append(y)

print(a)
print(b)

dot_product = 0

for i in range(dim):
    dot_product += a[i] * b[i]

print("a.b=", dot_product)



