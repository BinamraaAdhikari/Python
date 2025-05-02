#Check if a number entered is even or odd


num=int(input("Enter a number:"))
remainder=num%2
if(remainder==0):
    print("Its an even number")
else:
    print("Its an odd number")
