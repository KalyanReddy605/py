n=input()
n=str(n)
length=len(n)
first_letter=n[0]
Last_Letter=n[0-1]
stars="*" *(length-2)
result=first_letter+stars+Last_Letter
print(result)