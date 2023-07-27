
size = 5
a=size*2-1
b=1
for  i in range (1, size+1):
    for j in range (1, size*2+1):
        if (j==b or j==a):
            print(i,end='')
        else:
            print(" ", end= "")
            b+=1
            a-=1
            print()