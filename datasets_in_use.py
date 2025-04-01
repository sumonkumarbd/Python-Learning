
print("\n $$$Datasets$$$ \n")

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