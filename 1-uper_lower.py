ch=input("please Enter your own character:")
if(ord(ch) >= 65 and ord(ch)<=90):
   print(ch,"is an uppercase")
elif(ord(ch) >=97 and ord(ch)<=122):
   print(ch, "is a lowercase")
else:
   print(ch, "is not a lower or uppercase")
