# Check if s list contains a palindrome of a element


lis=[]
lis.append(input("Enter 1st element:"))
lis.append(input("Enter 2nd element:"))
lis.append(input("Enter 3rd element:"))
lis.append(input("Enter 4th element:"))
lis2=lis[::-1]
if(lis2==lis):
    print("You entered", lis,"which when reversed is",lis2,",so it is a palindrome")
else:
    print("You entered", lis,"which when reversed is",lis2,",so it is not a palindrome")
