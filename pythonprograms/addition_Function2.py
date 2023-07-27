#No argument but return a value

def add():
    a=int(input("Enter a number"))
    b=int(input("Enter a second number"))
    c=a+b
    return (c)
p=add()
print("Addition=",p)