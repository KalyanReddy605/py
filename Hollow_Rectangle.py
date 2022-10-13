from tokenize import Number


Number=int(input())
m=int(input())
First_Line="+" +("-"*Number)+ "+"
print(First_Line)
for i in range(1,m+1):
    print("|"+(" "*Number)+"|")
print(First_Line)