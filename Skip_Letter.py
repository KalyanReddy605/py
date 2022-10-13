name=input()
name=str(name)
L=len(name)
N=input()
N=int(N)
first=name[0:N-1]
Last=name[N+1:L]
print(first+Last)