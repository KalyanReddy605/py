number=int(input())
for i in range(number):
    pattern=""
    k=number-1
    for j in range(i+1,k+1):
        pattern=pattern+(str(j)+" ")
    print(pattern)
      