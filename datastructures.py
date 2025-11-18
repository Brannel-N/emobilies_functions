#list datastructres
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0]) # output apple
print(fruits[1]) # banana
print(fruits[2]) #cherry

fruits[0] = "banana" #changes position of banana to be first one

#list is ordered
#has indexse
#its changeable
#allows duplicate values
#set data structures

#tuple datastructures
cars=("mercedea","BMW","Audi")
print(cars)
print(f"{cars[0]} are manufactured in German")

majina={"Bran","Gessy","Zibia"}
majina.add("antiny")
print(majina)

#sets are unordered
#sets allow duplicates

#Dictionary
staff={"Name":"Bran","Age":24,"Gender":"Male"}
print(f"staff name is {staff['Name']} and age is {staff['Age']}")
#dictionary have key values pairs
#if//else state
num=int(input("Enter a number"))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    #if elif else statement
    marks=int(input("Enter your marks:"))
    if marks >= 80 and marks <= 100:
        print(f"{marks} is an A")
    elif marks >= 70 and marks < 80:
        print(f"{marks} is a B")
    elif marks >= 60 and marks < 70:
        print(f"{marks} is a C")
    elif marks >= 50 and marks < 60:
        print(f"{marks} is a D")
    else:
        print(f"{marks} is an E")
