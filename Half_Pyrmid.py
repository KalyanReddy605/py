from ast import pattern


n=int(input())
for i in range(1,n+1):
    pattern=""
    for j in range(1,i+1):
        pattern=pattern+str(j)+" "
    print(pattern)
    