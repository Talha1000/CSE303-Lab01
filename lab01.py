def add_num(a,b):
    product = a*b
    if (product < 1000):
        return product
    else:
            return a+b
x = int(input("Enter : "))
y = int(input("Enter : "))
result = add_num(x,y)
print("The result is : ", result)