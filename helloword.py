import math
# newVar = "hello world"
# print(newVar)

# firstName = "Tonty"
# lastName = "Stark"
# isGenius = True

# # name = input("what is your name")

# # print(name)

# age = input("Your age")


# nextYearAge = int(age) + 1

# print(nextYearAge)

# first = input("enter num")
# second = input("enter num 2")

# sum = int(first) + int(second)

# print(sum)

# strings

name = "Bruce Wayne"

print(name.upper())

print(name.find('W'))

print(name.replace("Bruce", ""))

# arithmetic operations

print(5 /2) # divide
print(5 +2) # add
print(5 - 2)# subtract
print(5   * 2)# multiply
print(5   ** 2)# power
print(5 //2)# divide and round to int
print(5 %2)# mod

newNum= 4
newNum += 2
print(newNum)

#logical operators

print(2>3 or 2> 1)
print(2<3 and 2<9)
print(not 2 < 3 )

age = 13

if age >= 18:
    print("you are 18")
elif age < 18 and age >3:
    print("something")
else:
    print("not 18")


print(range(5))

i = 1
while i< 10:
    print(i)
    i += 1

for item in range(5):
    print(item)

marks = [95, 90, 92, 87]

marks.append(99)
marks.insert(0,99)

print(marks[-1])
print(marks[0:2])
# marks.clear() empty the list

for grade in marks:
    print(grade)

print(99 in marks)
print(len(marks))

students = ["bruce", "cena", "hbk", "bill"]

for name in students:
    if name == "cena":
        continue;
    print(name)


newMarks = (90, 80 , 91) # tuple
# newMarks = {90, 80 , 91} # set 

print(newMarks.count(90))


newGrade = {"math": 90, "chem": 91, "phy": 80}
newGrade["comp"] = 88;

print(newGrade["chem"])


print(dir(math))


def printName(name):
    print(name)

name =input("hats your name")
printName(name)

def printSum(first = 0, second = 0 ):
    print( first + second)

printSum(1)