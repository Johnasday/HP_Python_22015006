print ("Number from 1,100:")

for n in range(1,101):

    if n % 3 == 0 and n % 5 == 0:

       print("couples",end=",")

    elif n % 3 == 0:

       print("boys",end=",")

    elif n % 5 == 0:

       print("girls",end=",") 

    else:

       print(n,end=",")
