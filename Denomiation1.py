n=int(input())
a=int(n/100)
b=int((n-(a*100))/50)
c=int((n-(a*100)-(b*50))/20)
d=int((n-(a*100)-(b*50)-(c*20))/10)
print("100 Notes:"+" "+str(a))
print("50 Notes:"+" "+str(b))
print("20 Notes:"+" "+str(c))
print("10 Notes:"+" "+str(d))