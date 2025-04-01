
print("\n Logical Oparators \n")

### $$$Oparators$$$ ###
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