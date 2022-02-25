def compound_interest_2019_1_60_209(P,T,R):
    A = P*(pow((1+R/100), T))
    return A

P = float(input("Enter the principal amount : "))
T = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
A = compound_interest_2019_1_60_209(P,R,T)
print("Compound Interest : {}  ".format(A))