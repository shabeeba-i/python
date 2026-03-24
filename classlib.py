class multipleFunction():
    #subfields
    def subfields():
        print("Sub-Fields in AI are: ")
        list=['Machine Learning','Neural Network','Vision','Speech Processing',
        'robotics','Naturl Language Processing']
        for i in list:
            print(i)
            Message = i
        return Message

    

    #oddEven
    def oddEven():
        num = int(input("Enter a number: "))
        if(num%2==0):
            print(num,"is even number")
            msg= num,"is even number"
        else:
            print(num,"is odd number")
            msg= num,"is odd number"
        return msg
    

    #Eligibility for marriage
    def eligible():
        gender=input("Your gender: ")
        age =int(input("Your age: "))
        if(gender=="male" and age>=21):
            print("Eligible")
            msg="Eligible"
        elif(gender=="female" and age>=18):
            print("Eligible")
            msg="Eligible"
        else:
            print("Not Eligible")
            msg="Not eligible"
        return msg
   

    #Percentage
    def percentage():
        sub1=int(input("Subject1 = "))
        sub2=int(input("Subject2 = "))
        sub3=int(input("Subject3 = "))
        sub4=int(input("Subject4 = "))
        sub5=int(input("Subject5 = "))
        total = sub1+sub2+sub3+sub4+sub5
        percentage= total/5
        print("Total:",total)
        print("Percentage:",percentage)
        return {"total":total,"percent":percentage}

    

    # area and perimeter of triangle
    def triangle():
        h= int(input("Height : "))
        b= int(input("Breadth : "))
        print("Area formula :(Height*Breadth/2)")
        area = h*b/2
        print("Area of triangle : ",area)
        h1= int(input("Height1 : "))
        h2= int(input("Height2 : "))
        b1= int(input("Breadth : "))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = h1+h2+b1
        print("Perimeter of triangle : ",perimeter)
        return{"Area":area,"Perimeter":perimeter}

    

