#24331A05E3
#Compound Intrest
p=float(input("Enter principle amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time period(in yr): "))
a=p*(1+r/100)**t
CI=a-p
print("Compound Intrest is ",CI)
