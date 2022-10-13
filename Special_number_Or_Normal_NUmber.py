n=input()
number=str(n)
n1=int(number[0])
n2=int(number[1])
if (((n1+n2)==7)or((n1%7==0)and(n1!=0)) or ((n2%7==0)and (n2!=0))or(n%7==0)):
    {
        print("Lucky.Number  :)")
    }
else:
    {
        print("Normal Number  :)")
    }