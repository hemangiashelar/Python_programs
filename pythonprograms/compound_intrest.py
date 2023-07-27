p=int(input("Enter a number"))
N=int(input("Enter a number"))
T=int(input("Enter a number"))
R=int(input("Enter a number"))

temp=R/N

CI=(p*(1+temp)**(N*T))-p
print(CI)

