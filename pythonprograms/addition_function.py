#Has argument and return a value

def add(a,b):
    c=a+b
    return (c)

a=int(input("Enter a 1st number"))
b=int(input("Enter a 2nd number"))

c=add(a,b)
print("Addition =",c)