rows=int(input("Enter the number of rows:"))
# it is used to print space
k=2*rows-2
# Outer loop in reverse order
for i in range(rows,-1,-1):
# Inner loop will print the number of space
    for j in range(k,0,-1):
        print(end="")
# This inner loop will print the number of stars 
    for j in range(0,i+1):
        print("*",end="")
    print("")

   
