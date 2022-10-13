n=int(input())
if(n%400==0):
    {
        print("it's a leap Year")
    }
elif((n%4==0)and(n%100!=0)):
    {
        print("It's a Leap Year")
    }
else:
    {
        print("It's Not a Leap Year")
    }