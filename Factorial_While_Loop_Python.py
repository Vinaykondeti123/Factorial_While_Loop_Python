# printing factorial of number using while loop
n=int(input("Enter number to find factorial: "))
i=1
fact=1
while i<=n:
   fact*=i
   i+=1
print(fact)
   