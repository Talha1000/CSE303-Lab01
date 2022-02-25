def prime_find_2019_1_60_209(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    for x in range (2,n):
        if (n % x==0):
            return True
        return False
n = int(input("Enter : "))
print(prime_find_2019_1_60_209(n))