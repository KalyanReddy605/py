n=int(input())
a=int(n/500)
b=int((n-(a*500))/50)
c=int((n-(a*500)-(b*50))/10)
d=int((n-(a*500)-(b*50)-(c*10))/1)
print("500:"+" "+str(a)+" "+"50:"+" "+str(b)+" "+"10:"+" "+str(c)+" "+"1:"+" "+str(d))