
print("\n $$$Loops$$$ \n")

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
