from re import I


number=int(input())
a=0
for i in range(1,number+1):
    if(i%2==0):
        a=a+i
print(a)