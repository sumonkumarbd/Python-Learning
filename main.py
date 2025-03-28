import math

###Oparator Prsidence###
#Exponentiation (**)
#Unary plus -> Unary minus -> Bitwise NOT (+x, -x, ~x)
#Multiplication -> Division -> Floor division -> Modulus (*, /, //, %)
#Addition -> Subtraction (+, -)
#Bitwise shift (<<, >>) -> #Bitwise And (&) -> Bitwise XOR (^) -> Bitwise OR (|)
#Comparisins -> Identy -> Membership (==, != , >, <, >=, <=, is, is not, in, not in)
#Logical Not (not) -> Loagical AND (and) -> Logical OR (or)

#Multiple Comment Start
"""

###Console program....###
user_input = input("Please Enter your name: ")
print("Your Name is " + user_input +"!")
print("Python Simple Calculator")
num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enater your secound number: "))
result = num_1+num_2
print("Sum is : " , result)


###String Oparations & Methods ###
text = " hello world! "
print(text.upper())
print(text.lower())
print(text.swapcase())
print(text.replace("world","Sumonkmr"))
splitTxt = "Hello-world-Sumon-kmr"
print(splitTxt.split("-"))
arrTxt = ['Hello', 'world', 'Sumon', 'kmr']
print(" ".join(arrTxt))
print(text.strip())
print(text.lstrip())
print(text.rstrip())

###Another String Oparations & Methods ###
mytext = "This is a Simple String"
manuplateTxt = mytext.startswith("This")
manuplateTxt = mytext.endswith("String!")
manuplateTxt = mytext.find("S")
manuplateTxt = mytext.count("i")
manuplateTxt = mytext.isalnum()
manuplateTxt = mytext.replace(" ","").isalpha()
print(manuplateTxt)
manuplateTxt = mytext.isalpha()
manuplateTxt = mytext.title().istitle()
manuplateTxt = mytext.title().istitle()
print(manuplateTxt)


###Number Oparations###
a = 10
b = 5
c = 3.17

result = a+b #Additions
result = a-b #Subtractions
result = a*b #Multiplication
result = a%g #Modulas
print(result)


###Math Oparations###
print(math.sqrt(16)) #Square root
print(math.pow(4,2)) #Power
print(math.sin(math.radians(90))) #Trigonometric
print(math.cos(math.radians(90))) #Trigonometric
print(math.log(10)) #Logarithmic
print(math.log10(10)) #Logarithmic base 10
print(math.factorial(5)) #Factorial
print(math.fabs(-7.5)) #Absolute value
print(math.floor(3.7)) #Floor
print(math.ceil(3.7)) #Celing
print(math.pi) #Constants
print(math.e) #Constants


##Gratest Common Divisor
num1 = 12
num2 = 18
print(math.gcd(num1,num2)) #Losagu
print(math.lcm(num1,num2)) #Gosagu


### if-else ###
# if elase statement
val = False
if  val:
    print("yes")
else: 
    print("no")


#Nested if-else Statement

if val:
    if type(val) == bool:
        print("Veriable type is Boolian")
    else:
        print("Veriable type is not Boolian")
else:
    print("The Veriable 'val' is False")


###Loop###
fruitsList = ["Apple", "Bananna", "Pine Apple", "Cherry", "Coconut"]
examResult = {
    "Bangla": 85,
    "English": 95,
    "Math": 88,
    "History": 69,
    "Biology": 98
}
# #for Loop
#example 1
for eachItem in fruitsList:
    print(eachItem)

print("\nfor loop") #for new line

# #exmaple 2
for subject,marks in examResult.items():
    print("{}:{}".format(subject,marks))

print("\nexample for break and continue in loop") #for new Line

# example for break and continue in loop
for num in range(10):
    if num == 5:
        break
    print(num)

print("\nWhile loop") #for new line

# #while loop
index = 0
while index<len(fruitsList):
    print(fruitsList[index])
    index = index+1

print("\nWhile loop in Dictionary")


index = 0
subject = list(examResult.keys())
while index<len(subject):
    eachSubject = subject[index]
    output = "Subject: "+eachSubject+"\n Marks = "+ str(examResult[eachSubject])
    print(output)
    index = index+1


print("\nNote for Loop")
print("In python, there are for and while loops, but there is no direct equivalent to the do-while loop found in some other programming language syntax specifically like in JavaScript")


### Logical Oparators ###
minmumAge = 18
hasPermision = True
nominiName = input("Enter Your Name: ")
nominiAge = int(input("Enter Your Age: "))
nominiHobby = input("Enter Your Hobby: ")

if not nominiAge <= minmumAge and hasPermision:
    print("Congratulation! You Are In the Club.")
else:
    print("Sorry, You're not meet the minimum citeria of membership rulls.")


### Comparision Oparator ###
a = 5
b = 10

print(a == b)   # Equal to         → False
print(a != b)   # Not equal to      → True
print(a > b)    # Greater than      → False
print(a < b)    # Less than         → True
print(a >= b)   # Greater than or equal to → False
print(a <= b)   # Less than or equal to   → True

""" #Multiple Comment Finnished

### List ###
## Charecterstick of List
# - Order
# - Mutable
# - Allow duplicates
# - Heterogeneous
# - Dynamic size

## List Methods
# - append() Adds an element to the end of the list
# - insert() Inserts an element at a specified position
# - extend() Extend the list by adding elements from another list
# - remove() Removes the first occurrence of the specified element
# - pop() Last element slice and returns it
# - clear() Removes all elements from the list
# - index() Returns the index of the first occurrence of the specified element
# - count() Returns the number of occurrences of specified element
# - sort() Sort the list in Assending order
# - reverse() reverse the list in Dessending order of a Sort list
# - len() Counting the size of list
# - list[3:5] list slicing

cities_part1 = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "London", "Paris"]
cities_part2 = ["Berlin", "Tokyo", "Beijing", "Dhaka", "Mumbai", "Delhi", "Sydney", "Sydney"]

# add_city = cities_part1.append("Honnoy")
# insert_city = cities_part1.insert(4,"Dubai")
# cities_part1.extend(cities_part2)
# cities_part1.remove("Los Angeles")
# cityinpop = cities_part1.pop(2)
# print(cityinpop)
# cities_part1.clear()
# getIndex = cities_part1.index("Chicago")
# print(getIndex)
# element_count = cities_part2.count("Sydney")
# print(element_count)
# cities_part1.sort()
# cities_part1.reverse()
# slice_list = cities_part1[2:5]
# print(slice_list)
print(cities_part1)
# print(cities_part1)




