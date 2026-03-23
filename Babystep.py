#Welcome to assignment1
print("Welcome to Asssignment-1")

#addition
Num1 =int(input("enter the value for Num1"))
Num2 =int(input("enter the value for Num2"))
add= Num1+Num2
print(add)

#Body Mass Index

BMI=int(input("Enter the BMI index:"))
if(BMI<=18.5):
    print("under weight")
elif(BMI<=25):
    print("Normal")
elif(BMI<=30):
    print("overweight")
else:
    print("very overweight")
