from ast import pattern


number=int(input())
b=1
for i in range(0,number):
    pattern=""
    for j in range(b,b+i+1):
        pattern=pattern+(str(j)+" ")
        b=b+1
    print(pattern)  