def largest():
    a=int(input("Enter a number"))
    b=int(input("Enter a second number"))

    if(a>b):
        c=a
    else:
        c=b


    return(c)

c=largest()
print("Largest number is=",c)