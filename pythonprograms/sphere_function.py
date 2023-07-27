def sphere():
    r=float(input("Enter a radious"))

    a=4*3.14*r*r
    v=(4/3)*3.14*r*r*r
    return (a,v)

a,v=sphere()

print("Area of sphere",a)
print("Volume of  sphere",v)