#Root of Quadratic Equation

import math


a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))

d=(b*b)-(4*a*c)

if(d==0):
    print("Root are equal")
    x=-b/(2*a)
    print("sdfs")

elif(d>0):
    print("Root are unequal")
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("sfs")
    print("fdfd")

else:
        print("fsdfs")
