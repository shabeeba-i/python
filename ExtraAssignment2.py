#Print 0 to 20 by using range
for i in range(0,20):
    print(i)

#print range 10 to 20
for i in range(10,20):
    print(i, end=" ")

# Print number of items in the list by using 'len'
list =[10,20,55,14,43,87,76]
print(list,"Number of item in the list:",len(list),sep="\n")

#Artificial Intelligence
word ="Artificial Intelligene"
print(word)
for i in word:
    print(i)

#
print("-Your Name-")
print("-Your Age-")
print("-Your Profession-")

#print mixed datatype
tup=(1,'Welcome',2,'Hope')
print(tup)

#Merging 2 tuples
tup1=(1,2,3,4,5)
tup2=('Python','Hope')
tup3=(tup1,tup2)
print(tup3)

#print odd nummber in list
list=[20,10,16,19,25,1,276,188]
for i in list:
    if(i%2==1):
        print(i,"is odd")

#print even nummber in list
list=[20,10,16,19,25,1,276,188]
for i in list:
    if(i%2==0):
        print(i,"is even")