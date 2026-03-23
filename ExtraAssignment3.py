
#print 'correct' if i==10
value=int(input("Value:"))
if(value==10):
    print("Correct")
else:
    print("not correct")

#check the password, using if and else
passw="HOPE@123"
password= input("Enter the Password: ")
if(password==passw):
    print("Your Password is correct")
else:
    print("Your Password is incorrect")

#catagory the people
age=int(input("Age: "))
if(age<18):
    print("child")
elif(age<40):
    print("Adult")
elif(age<60):
    print("Citizens")
else:
    print("senior citizens")

#find whether num is positive or negative
num = int(input("enter any number: "))
if(num>0):
    print("No is positive")
else:
    print("No is negative")

#divisible of 5
number= int(input("enter the number to check: "))
if(number%5==0):
    print("No is divisible by 5")
else:
    print("No is not divisible by 5")