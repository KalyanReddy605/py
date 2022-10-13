n=int(input())
m=int(input())
for i in range(1,m+1):
    if(i%2!=0):
        print("+ "*n)
    else:
        print("- "*n)