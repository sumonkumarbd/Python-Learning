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

""" #Multiple Comment Finnished

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
