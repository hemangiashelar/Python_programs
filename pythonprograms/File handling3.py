n=input("Enter your name")
f=open("a3.txt","w")
f.write(n)
p=input("Enter your sirname")
f.write(p)

print("Full name is",n,p)