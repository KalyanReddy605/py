Name=input()
Name=str(Name)
length=len(Name)
First=Name[:2]
Middle="*"*(length-4)
Last=Name[length-2:length]
print(First+Middle+Last)