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


### Tuples ###
## Charecterstick of List
# - Order
# - Imutuble
# - Allow Duplicates
# - Heterogeneous
# - Fixed Size

nubers = (1,2,5,8,6,11,44, 1,757,45)
print(nubers.index(45)) # represent of index number
print(nubers.count(1)) # duplicate value count
print(nubers[5:6]) #Slice in tuples
#loop in tupuls
for number in nubers:
    print(number)


### Set ###
##Charectersticks of set
# - Unorder
# - Mutable
# - Avoid Duplicate value
# - Heterogeneous
# - Dianamic size


nameSet = {"Sumon","Bristi","Tania","Leo"}
ageSet = {29,23,18,.2}
nameSet.add("Puti")
nameSet.update(["Minu","Khushi"])
nameSet.remove("Tania")
print(nameSet)

newSet = nameSet.union(ageSet)
print(newSet)

##Some method for higher math
# - intersection()
# - differnce()
# - issubset()
# - issuperset



for eachName in nameSet:
    print(eachName)


print(len(nameSet))



### Dictionary ###
## Characteristics of Dictionary
# - Key-Value Pair
# - Unordered (Python 3.6 and below), Ordered (Python 3.7+)
# - Mutable
# - Avoids Duplicate Keys
# - Heterogeneous
# - Dynamic Size

personDict = {"name": "Sumon", "age": 29, "city": "Dhaka"}
contactDict = {"email": "sumon@example.com", "phone": "123456789"}

personDict["gender"] = "Male"  # Adding a new key-value pair
personDict.update({"profession": "Developer", "country": "Bangladesh"})  # Updating multiple keys
personDict.pop("city")  # Removing a key-value pair

print(personDict)

newDict = personDict.copy()  # Creating a copy
newDict.update(contactDict)  # Merging two dictionaries
print(newDict)

## Some useful methods for dictionary
# - keys()
# - values()
# - items()
# - get()
# - pop()
# - clear()

for key, value in personDict.items():
    print(f"{key}: {value}")

print(len(personDict))  # Number of key-value pairs




### Function ###
## Characteristics of Function
# - Code Reusability
# - Modular Approach
# - Can Have Parameters
# - Can Return Values
# - Increases Readability

def greet(name):
    # Function to greet a person
    print(f"Hello, {name}!")

def add(a, b):
    # Function to add two numbers
    return a + b

def is_even(number):
    # Function to check if a number is even
    return number % 2 == 0

print(add(5, 3))  # Output: 8
print(is_even(10))  # Output: True

## Some useful function concepts
# - Default Parameters
# - *args (Variable-Length Arguments)
# - **kwargs (Keyword Arguments)
# - Lambda Functions
# - Recursion

# Function with default parameter
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()  # Output: Welcome, Guest!
welcome("Sumon")  # Output: Welcome, Sumon

# Function with *args (multiple arguments)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15

# Function with **kwargs (keyword arguments)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Bristi", age=23, city="Dhaka")

# Lambda function
square = lambda x: x * x
print(square(6))  # Output: 36

mylamFunc = lambda num,num2: num * num2
print(mylamFunc(2,3)) # Output: 6

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

### File Handling ###
## Characteristics of File Handling
# - Allows Reading and Writing Files
# - Supports Different Modes (r, w, a, r+)
# - Works with Both Text and Binary Files
# - Helps in Data Persistence
# - Can Handle Large Data Efficiently

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")
    file.write("Python makes it easy to work with files.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending data to a file
with open("example.txt", "a") as file:
    file.write("Appending a new line to the file.\n")

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# Checking if file exists before reading (to avoid errors)
import os
if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print("Safely reading the file:\n", file.read())
else:
    print("File not found.")

## Some important file handling methods
# - read() → Reads entire file content
# - readline() → Reads one line at a time
# - readlines() → Reads all lines as a list
# - write() → Writes data to the file
# - append() → Adds data at the end of the file
# - close() → Closes the file (automatically handled with 'with' statement)

# Deleting a file
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted successfully!")
else:
    print("File does not exist.")




    ### Directory Handling ###
## Characteristics of Directory Handling
# - Helps in Managing Files and Folders
# - Supports Creating, Renaming, and Deleting Directories
# - Works with Paths Efficiently
# - Useful for Organizing Large Data
# - Helps in Automating File Operations

import os

# Creating a new directory
dir_name = "my_directory"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created successfully!")

# Creating a nested directory
nested_dir = "parent_dir/child_dir"
if not os.path.exists(nested_dir):
    os.makedirs(nested_dir)  # Creates parent_dir and child_dir together
    print(f"Nested Directory '{nested_dir}' created successfully!")

# Listing files and directories in the current path
print("List of files and directories:", os.listdir("."))

# Renaming a directory
new_name = "renamed_directory"
if os.path.exists(dir_name):
    os.rename(dir_name, new_name)
    print(f"Directory renamed from '{dir_name}' to '{new_name}'")

# Deleting an empty directory
if os.path.exists(new_name):
    os.rmdir(new_name)
    print(f"Directory '{new_name}' deleted successfully!")

# Deleting a directory with files
import shutil
if os.path.exists("parent_dir"):
    shutil.rmtree("parent_dir")  # Removes a directory and its contents
    print("Parent directory and its contents deleted.")

## Some important directory handling methods
# - os.mkdir() → Creates a directory
# - os.makedirs() → Creates nested directories
# - os.listdir() → Lists files and directories in a given path
# - os.rename() → Renames a directory
# - os.rmdir() → Removes an empty directory
# - shutil.rmtree() → Removes a directory and all its contents

print("Directory operations completed successfully!")




### Zip File Handling ###
## Characteristics of Zip File Handling
# - Compress multiple files into a single archive
# - Supports both writing and extracting files
# - Useful for reducing file size and organizing data
# - Provides fast access to compressed files
# - Helps in efficient file storage and transfer

import zipfile
import os
import shutil

# Creating a zip file
with zipfile.ZipFile("new.zip", "w") as zip:
    print("Zip file is Created!")  # Confirms that the zip file has been created

# Creating 5 text files dynamically
for i in range(5):
    file_name = f"myfile{i}.txt"
    with open(file_name, "w") as myFile:
        print(myFile)  # Printing file object (for debugging)
        print(myFile)  # Unnecessary duplicate print (can be removed)

# Writing files into the zip archive
with zipfile.ZipFile("new.zip", "w") as myZip:
    for i in range(5):
        file_name = f"myfile{i}.txt"
        myZip.write(file_name)  # Adds each file to the zip archive

# Extracting all files from the zip archive
with zipfile.ZipFile("new.zip", "r") as myZip:
    myZip.extractall()  # Extracts all files in the current directory
    extracted_files = myZip.namelist()  # Lists extracted files
    print(extracted_files)  # Prints the list of extracted files

# Creating a directory if it doesn't exist
dir_name = "my_directory"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)  # Creates the directory

    # Creating and writing to files inside the directory
    for i in range(3):
        file_name = f"myfile{i}.txt"

        # Creating the file (w mode creates an empty file)
        with open(os.path.join(dir_name, file_name), "w"):
            fileList = os.listdir(dir_name)
            print(fileList)  # Prints files in the directory

        # Appending text to the file
        with open(os.path.join(dir_name, file_name), "a") as wFile:
            wFile.write(f"SL no: {i} Hello, this is written dynamically from the program.\n")

# Creating a zip archive of the entire directory
shutil.make_archive("new", "zip", dir_name)  # Compresses 'my_directory' into 'new.zip'

""" #Multiple Comment Finnished

### CSV File Handling ###
import csv
### CSV File Handling ###
## Characteristics of CSV File Handling
# - Stores data in a comma-separated format (CSV)
# - Useful for handling tabular data
# - Easily readable by both humans and programs
# - Supports efficient data import/export

import csv

# Sample data as a list of lists (Rows for CSV)
data = [
    ["ID", "Name", "Age", "City"],  # Header row
    [1, "Sumon", 29, "Dhaka"],
    [2, "Bristi", 23, "Chittagong"],
    [3, "Tania", 18, "Khulna"],
    [4, "Leo", 32, "Barisal"],
    [5, "Puti", 27, "Sylhet"],
    [6, "Minu", 30, "Rajshahi"],
    [7, "Khushi", 25, "Rangpur"]
]

# Writing data to a CSV file
with open("demo_CSV.csv","w",newline="",encoding="utf-8") as myCSV:
    writer = csv.writer(myCSV)
    writer.writerows(data)
    print("CSV file Created Successfully")

# # Reading data from the CSV file
# with open("demo_data.csv", "r", encoding="utf-8") as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         print(row)  # Prints each row
















