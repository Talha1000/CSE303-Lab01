n = int(input("Enter :"))
total = 0
total = (n*(n+1)*(2*n+1))/6
for i in range(1,n+1):
    if(i != n):
        print("%d^2 + " %i, end = '')
    else:
            print("{0}^2 = {1}".format(i, total))
            