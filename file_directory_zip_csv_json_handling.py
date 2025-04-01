
print("\n $$$File & folder handling$$$ \n")

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


### CSV File Handling ###
import csv
### CSV File Handling ###
## Characteristics of CSV File Handling
# - Stores data in a comma-separated format (CSV)
# - Useful for handling tabular data
# - Easily readable by both humans and programs
# - Supports efficient data import/export


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

# Reading data from the CSV file
with open("demo_CSV.csv","r") as myCSV:
    reader = csv.reader(myCSV)
    for row in reader:
        print(row)


### Exception Handling ###
## Characteristics of Exception Handling
# - Prevents program crashes due to unexpected errors
# - Uses try-except blocks to catch exceptions
# - Helps in debugging and error logging
# - Allows graceful program termination
# - Can handle multiple exception types

try:
    # User input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Attempting division (may cause ZeroDivisionError)
    result = num1 / num2

    # Writing to a file (may cause FileNotFoundError)
    with open("output.txt", "w") as file:
        file.write(f"Result: {result}")

    print("Operation successful!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input! Please enter numeric values.")

except FileNotFoundError:
    print("Error: The file could not be found!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Execution completed!")  # This runs regardless of an exception




### JSON File Handling ###
## Characteristics of JSON
# - Stores data in key-value pairs (similar to Python dictionaries)
# - Supports structured and hierarchical data
# - Lightweight and human-readable
# - Used for data interchange (e.g., APIs, config files)
# - Compatible with multiple programming languages

import json

# Sample data (Python dictionary)
data = {
    "employees": [
        {"ID": 1, "Name": "Sumon", "Age": 29, "City": "Dhaka"},
        {"ID": 2, "Name": "Bristi", "Age": 23, "City": "Chittagong"},
        {"ID": 3, "Name": "Tania", "Age": 18, "City": "Khulna"},
        {"ID": 4, "Name": "Leo", "Age": 32, "City": "Barisal"}
    ]
}

#python Object -> JSON String
employeesJSON = json.dumps(data, indent=4)
# print(employeesJSON)

# Json String -> Python Object
pcJSON = '{"Motherboard":"MSI", "Proccesor":"Ryzen","SSD":"Ntac","RAM":"PNY"}'
pcObj = json.loads(pcJSON)
# print(pcObj["SSD"])


with open("data.json","w",encoding="utf-8") as json_file:
    json_file.write(employeesJSON)


with open("data.json","r") as readJson :
    jsonS = json.load(readJson)
    jsonS = json.dumps(jsonS,indent=4)
    print(jsonS)
