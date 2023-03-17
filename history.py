if salary >= 7000 and age >= 45:
    print("auto approved")
else:
    print("approved manually")
salary = int(input("Please enter your salary: "))

age = int(input("Please enter your age: "))

# new line
print("")

if salary >= 7000 or age >= 45:
#if salary >= 7000 and age >= 45:
    print("auto approved")
else:
    print("approved manually")
string = "python is programming is fun"

sub = input("Please enter the keyword to search: ")

print("")

string = "python is programming is fun"

sub = input("Please enter the keyword to search: ")

print("")

if sub in string:
    print("keyword"  + sub + " is present")
else:
    print("search is empty")

string = "python is programming is fun"

sub = input("Please enter the keyword to search: ")

print("")

if sub in string:
    print("keyword '"  + sub + "' is present")
else:
    print("search is empty")

i = 0

while i < 10:
    print(i)
debugfile('/Users/alexandralozser/.spyder-py3/while_loops.py', wdir='/Users/alexandralozser/.spyder-py3')

i = 0

while i < 10:
    print(i)
    i += 2

i = 0
var1 = True 

#while i < 10:
while var1:
    print(i)
    i += 2
    
    if i >= 10:
        var1 = False
debugfile('/Users/alexandralozser/.spyder-py3/while_loops.py', wdir='/Users/alexandralozser/.spyder-py3')


name = input("Please enter a name: ")

i = 1

for letters in name:
    print("character number {} is {} ".format(i, letters))
    i += 1
debugfile('/Users/alexandralozser/.spyder-py3/for_loops.py', wdir='/Users/alexandralozser/.spyder-py3')

for i in range(1, 10, 2):
    print(i)



for i in range(1, 10, 2):
    print(i)

nameRange = input("Please enter a name: ")

# i needs to start at 0, end at the end of the name

length = len(nameRange)


for j in range(0, length, 1):
    print("character number {} is {} ".format(j+1, nameRange[i])) #adding +1 to j so that the first character is 1 and not 0
    j += 1
nameRange = input("Please enter a name: ")

# i needs to start at 0, end at the end of the name

length = len(nameRange)


for j in range(0, length, 1):
    print("character number {} is {} ".format(j+1, nameRange[i])) #adding +1 to j so that the first character is 1 and not 0
    j += 1
nameRange = input("Please enter a name: ")

# i needs to start at 0, end at the end of the name

length = len(nameRange)


for j in range(0, length, 1):
    print("character number {} is {} ".format(j+1, nameRange[j])) #adding +1 to j so that the first character is 1 and not 0
    j += 1
nameEnum = input("Please enter a name: ")

# Initializing x not necessary
# x = 1

# Run the for loop
# This allows you to increment x without needing to explicitly write x+=1
for x, letters in enumerate(nameEnum, start=1):
    print("character number {} is {} ".format(x, letters))
#    x += 1
for i in range(1, 20, 1):
    for j in range(1, 11, 1):
        result = i * j
        print(result)


for i in range(1, 20, 1):
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
for i in range(1, 20, 1):
    print("")
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
for i in range(1, 20, 1):
    if (i%2) != 0:
        continue
    
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
    
    print("")
for i in range(1, 20, 1):
    
    if i > 20:
        break
    
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
    
    print("")
for i in range(1, 20, 1):
    
    if i > 10:
        break
    
    for j in range(1, 11, 1):
        result = i * j
        print(result, end=" ")
    
    print("")

list1 = ["Jitesh, John, Alex"]
print(list1)
list2 = []
print(list2)
list2 = list1

# values get moved to list3's new storage space
list3 = list1.copy()

list1.append("Alia")

## ---(Mon Jan 23 19:04:13 2023)---

print(list[2])


list1 = ["Jitesh, John, Alex"]
print(list1)

# 2. 
# no values yet
list2 = []
print(list2)

# below is the same thing as above except using the list() function

#3. 
#list2 = list()
#print(list2)

# 4. 
# assigning the label, but everything remains in storage where it was
# referring to the same memory location, so changes are reflected in both places
list2 = list1

# values get moved to list3's new storage space
# copied and stored in a different location
list3 = list1.copy()

list1.append("Alia")


# ----------------------------------------------------------------------------
# Accessing list elements
# ----------------------------------------------------------------------------

print(list[2])
print(list1[2])

list1 = ["Jitesh, John, Alex"]
print(list1)

# 2. 
# no values yet
list2 = []
print(list2)

# below is the same thing as above except using the list() function

#3. 
#list2 = list()
#print(list2)

# 4. 
# assigning the label, but everything remains in storage where it was
# referring to the same memory location, so changes are reflected in both places
list2 = list1

# values get moved to list3's new storage space
# copied and stored in a different location
list3 = list1.copy()

list1.append("Alia")


# ----------------------------------------------------------------------------
# Accessing list elements
# ----------------------------------------------------------------------------

print(list1[2])

list1 = ["Jitesh", "John", "Alex"]
print(list1)

# 2. 
# no values yet
list2 = []
print(list2)

# below is the same thing as above except using the list() function

#3. 
#list2 = list()
#print(list2)

# 4. 
# assigning the label, but everything remains in storage where it was
# referring to the same memory location, so changes are reflected in both places
list2 = list1

# values get moved to list3's new storage space
# copied and stored in a different location
list3 = list1.copy()

list1.append("Alia")


# ----------------------------------------------------------------------------
# Accessing list elements
# ----------------------------------------------------------------------------

print(list1[2])
print(list1[-1])

print(list1[1:4])
print(list1[:3])
print(list1[:])
print(list1[1:])
print(list1[-3:1])
print(list1[-3:-1])
for name in list1:
    print(name)


searchName = input("Please enter the name to search: ")

if searchName in list1:
    print("We have found the name")
else:
    print("we have not found the name YET")
list1 = ["Jitesh", "John", "Alex"]
print(list1)

list2 = []
print(list2)

list2 = list1

list3 = list1.copy()


list1.append("Alia")

list1.insert(1, "Frans")

list[2] = "Chris"

list1[2] = "Chris"

list1[2] = "Chris"

newName = input("submit new name to replace Chris: ")

if "Chris" in list1:
    list1[2] = newName
else:
continue
newName = input("submit new name to replace Chris: ")

if "Chris" in list1:
    list1[2] = newName
else:
    continue
if "Chris" in list1:
    list1[2] = newName
newName = input("submit new name to replace Chris: ")

if "Chris" in list1:
    list1[2] = newName
newName = input("submit new name to replace Chris: ")

if "Jobe" in list1:
    list1["Jobe"] = newName

newName = input("submit new name to replace Chris: ")

if list1.__contains__("Jobe"):
    list1[2] = newName

del list3[1]
list3.remove("Jitesh")


list3.pop(0)
list2 = list1
list3 = list1.copy()
list3.Clear()
list3.clear()
list3 = list1.copy()

list3.replace("Jitesh", "Ali")
list3.clear()
varT = True
num_list = []

# Accept input until user enters 0

while varT:
    num = int(input("Enter a number: "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)


len(num_list)


list2 = [45, 15, 35]

conList = num_list + list2
varT = True
num_list = []


# Accept input until user enters 0
while varT:
    num = int(input("Enter a number: "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)




# Finding the length of the list/ num of elements
len(num_list)


# Concatenate the lists

list2 = [45, 15, 35]

conList = num_list + list2
num_list = num_list + list2
while varT:
    num = int(input("Enter a number: "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)

varT = True
num_list = []


# Accept input until user enters 0
while varT:
    num = int(input("Enter a number: "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)
num_list.extend(list2)
for num in list2:
    total += num
total = 0
# Calculating the average of the list

for num in list2:
    total += num
total = 0

total = 0
# Calculating the average of the list

for num in list2:
    total += num


average = total/2
total = 0
# Calculating the average of the list

for num in list2:
    total += num


average = total/3
average = sum(list2)/len(list2)

varT = True
num_list = []


# Accept input until user enters 0
while varT:
    num = int(input("Enter a number: "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)




# Finding the length of the list/ num of elements
len(num_list)


# Concatenate the lists

list2 = [45, 15, 35]

conList = num_list + list2




# num_list = num_list + list2  <- can add contents of list2 to num_list
# OR
# use extend() method

num_list.extend(list2)


# Calculating the average of the list

average = sum(list2)/len(list2)

varT = True
num_list = []


# Accept input until user enters 0
while varT:
    num = int(input("Enter a number: "))
    
    if num == 0:
        varT = False
    else:
        num_list.append(num)




# Finding the length of the list/ num of elements
len(num_list)
average = sum(list2)/len(list2)
 Calculating the average of the list

average = sum(num_list)/len(num_list)
average = sum(num_list)/len(num_list)
for num in num_list:
    total += num

newAv = total/len(num_list)
total = 0

for num in num_list:
    total += num

newAv = total/len(num_list)
num_list.sort()
num_list.sort(reverse=True)
position = num_list.index(snum)


snum = int(input("please enter the number to search for: "))

position = num_list.index(snum)

snum = int(input("please enter the number to search for: "))

position = num_list.index(snum)

print("we have found the number {} at position {}.".format(snum, position))
list1 = [20, 15, 42, "Frans", 55]
runfile('/Users/alexandralozser/.spyder-py3/listPartFour_MultiDimList.py', wdir='/Users/alexandralozser/.spyder-py3')

list1 = [[20, 15], 42, "Frans", 55]

list1[0]
subList[0]


list1 = [[20, 15], 42, "Frans", 55]

subList = list1[0]

subList[0]


list1 = [[20, 15], 42, "Frans", 55]

subList = list1[0]

list1[0][0]
list1 = [[[20, 15], [65, 12]], 42, "Frans", 55]

subList = list1[0]


# Accessing the sublist first, then the first element inside the sublist
list1[0][0]

list1 = [[[20, 15], [65, 12]], 42, "Frans", 55]

subList = list1[0]


# Accessing the sublist first, then the first element inside the sublist
list1[2][0]
list1 = [[[20, 15], [65, 12]], 42, "Frans", 55]

subList = list1[0]


# Accessing the sublist first, then the first element inside the sublist
list1[0][0]

list1 = [[[20, 15], [65, 12]], 42, "Frans", 55]

subList = list1[0]


# Accessing the sublist first, then the first element inside the sublist
list1[0][0][0]


list1 = [[[20, 15], [65, 12]], 42, "Frans", 55]

subList = list1[0]


# Accessing the sublist first, then the first element inside the sublist
list1[0][0][1]

list1 = [[[20, 15], [65, 12]], 42, "Frans", 55]

subList = list1[0]


# Accessing the sublist first, then the first element inside the sublist
list1[0][2][1]

list1 = [[[20, 15], [65, 12]], 42, "Frans", 55]

subList = list1[0]


# Accessing the sublist first, then the first element inside the sublist
list1[0][1][1]
t1 = (1, 2, 3)
tuple1 = ("Jitesh", "John", "Alia", "Lise")

t1 = (1, 2, 3)

print(t1[1])
len(t1)
address = {'Street' : '180 Adams Street',
           'City'   :  'Chicago',
           'State'  : 'IL',
           'Country': 'USA'}


print(address['Street'])
address = {'Street' : '180 Adams Street',
           'City'   :  'Chicago',
           'State'  : 'IL',
           'Country': 'USA'}


print(address['Country'])


address['Street'] = '181 Adams Street'
address['Zip'] = '60611'
address['Zip'] = 60611
address['Zip'] = '60611'


del address['Zip']

address['Zip'] = '60611'

len(address)
del address['Zip']

len(address)

address.keys()
keys = address.keys()

keys = list(address.keys())

values = list(address.values())
%clear



while isStaying:
    input = print("Hello! Welcome to your personal Contact book.\nWould you like to -\n\n1. 'S' = Search for a contact.\2. 'A' = Add a new contact.\n3. 'E' = Exit the system.")

"""
# ~ Phonebook Project ~
# ----------------------------------------------------------------------------


# boolean for if the user has selected to stay in the menu
isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


while isStaying:
    input = print("Hello! Welcome to your personal Contact book.\nWould you like to -\n\n1. 'S' = Search for a contact.\2. 'A' = Add a new contact.\n3. 'E' = Exit the system.")
lexandralozser
"""
# ~ Phonebook Project ~
# ----------------------------------------------------------------------------


# boolean for if the user has selected to stay in the menu
isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


while isStaying:
    input = print("Hello! Welcome to your personal Contact book.\nWould you like to -\n\n1. S = Search for a contact.\2. A = Add a new contact.\n3. E = Exit the system.")
    print


isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


while isStaying:
    input = print("Hello! Welcome to your personal Contact book.\nWould you like to -\n\n1. S = Search for a contact.\2. A = Add a new contact.\n3. E = Exit the system.")
    print(input)

isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}

input = print("Hello! Welcome to your personal Contact book.\nWould you like to -\n\n1. S = Search for a contact.\2. A = Add a new contact.\n3. E = Exit the system.")


while isStaying:
    print(input)
intro = print("Hello! Welcome to your personal Contact book.")

input = print("Would you like to -\n\n1. S = Search for a contact.\2. A = Add a new contact.\n3. E = Exit the system.")

intro = print("Hello! Welcome to your personal Contact book.")

input = print("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.")


isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


intro = print("Hello! Welcome to your personal Contact book.")

selection = input("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.")

selectionLower = selection.lower

while isStaying:
    if selectionLower == "s" or selection == "search":
        print("searching")
    elif selectionLower == "a" or selection =="add":
        print("adding")
    elif selectionLower == "e" or selection == "exit":
        isStaying = False
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")



isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


intro = print("Hello! Welcome to your personal Contact book.")

selection = input("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.")

selectionLower = selection.lower

while isStaying:
    if selectionLower == "s" or selectionLower == "search":
        print("searching")
    elif selectionLower == "a" or selectionLower =="add":
        print("adding")
    elif selectionLower == "e" or selectionLower == "exit":
        isStaying = False
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
"""
# ~ Phonebook Project ~
# ----------------------------------------------------------------------------


# boolean for if the user has selected to stay in the menu
isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


print("Hello! Welcome to your personal Contact book.")

selection = input("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.")



while isStaying:
    if selection == "s" or selection == "search":
        print("searching")
    elif selection == "a" or selection =="add":
        print("adding")
    elif selection == "e" or selection == "exit":
        isStaying = False
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')





isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


print("Hello! Welcome to your personal Contact book.")



selectionLower = "enter"


if isStaying and selectionLower != "e":
    
    selection = input("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.")
    selectionLower = selection.lower()
    
    
    if selectionLower == "s" or selectionLower == "search":
        print("searching")
    elif selectionLower == "a" or selectionLower =="add":
        print("adding")
    elif selectionLower == "e" or selectionLower == "exit":
        isStaying = False
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")
else:
    print("Quitting. Goodbye")
@author: alexandralozser
"""
# ~ Phonebook Project ~
# ----------------------------------------------------------------------------


# boolean for if the user has selected to stay in the menu
isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


print("Hello! Welcome to your personal Contact book.")



selectionLower = "enter"


if isStaying and selectionLower != "e":
    
    selection = input("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.\n")
    selectionLower = selection.lower()
    
    
    if selectionLower == "s" or selectionLower == "search":
        print("searching")
    elif selectionLower == "a" or selectionLower =="add":
        print("adding")
    elif selectionLower == "e" or selectionLower == "exit":
        isStaying = False
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")
else:
    print("Quitting. Goodbye")


isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


print("Hello! Welcome to your personal Contact book.")



selectionLower = "enter"


if isStaying and selectionLower != "e":
    
    selection = input("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.\n")
    selectionLower = selection.lower()
    
    
    if selectionLower == "s" or selectionLower == "search":
        print("searching")
    elif selectionLower == "a" or selectionLower =="add":
        print("adding")
    elif selectionLower == "e" or selectionLower == "exit":
        isStaying = False
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")
else:
    print("Quitting. Goodbye")
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')

isStaying = True

# list for storing dictionary entries
list = []

# dictionary for storing contact info
phonebook = {}


print("Hello! Welcome to your personal Contact book.")



selectionLower = "enter"


while isStaying and selectionLower != "e":
    
    selection = input("Would you like to -\n\n1. S = Search for a contact.\n2. A = Add a new contact.\n3. E = Exit the system.\n")
    selectionLower = selection.lower()
    
    
    if selectionLower == "s" or selectionLower == "search":
        print("searching")
    elif selectionLower == "a" or selectionLower =="add":
        print("adding")
    elif selectionLower == "e" or selectionLower == "exit":
        isStaying = False
    else:
        print("Not a valid option. Please choose S, A, or E to exit.")
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/dictionariesPartOne.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
%clear
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/listPartFour_MultiDimList.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
%clear
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
runcell(0, '/Users/alexandralozser/.spyder-py3/PhonebookProject.py')
%clear
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')

## ---(Sat Feb 18 21:38:50 2023)---
runfile('/Users/alexandralozser/untitled4.py', wdir='/Users/alexandralozser')
runfile('/Users/alexandralozser/NodeTraversalExample.py', wdir='/Users/alexandralozser')
debugfile('/Users/alexandralozser/NodeTraversalExample.py', wdir='/Users/alexandralozser')
runfile('/Users/alexandralozser/NodeTraversalExample.py', wdir='/Users/alexandralozser')
debugfile('/Users/alexandralozser/NodeTraversalExample.py', wdir='/Users/alexandralozser')
runfile('/Users/alexandralozser/NodeTraversalExample.py', wdir='/Users/alexandralozser')
debugfile('/Users/alexandralozser/NodeTraversalExample.py', wdir='/Users/alexandralozser')

## ---(Sun Feb 19 16:24:37 2023)---
runfile('/Users/alexandralozser/NodeTraversalExample.py', wdir='/Users/alexandralozser')
%clear
runfile('/Users/alexandralozser/AnagramExample.py', wdir='/Users/alexandralozser')
debugfile('/Users/alexandralozser/AnagramExample.py', wdir='/Users/alexandralozser')

## ---(Sat Feb 25 19:20:38 2023)---
runfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')
debugfile('/Users/alexandralozser/.spyder-py3/PhonebookProject.py', wdir='/Users/alexandralozser/.spyder-py3')

import datetime

date1 = datetime.date(2014, 12, 31)

import datetime

date1 = datetime.date(2014, 12, 31)

year = date1.year

import datetime

date1 = datetime.date(2014, 12, 31)

year = date1.year
month = date1.month
day = date1.day

year1 = 2018
month1 = 11
day1 = 31

date2 = datetime.date(year1, month1, day1)

year1 = 2018
month1 = 11
day1 = 30

date2 = datetime.date(year1, month1, day1)

time1 = datetime.time()
print(time1)
time1 = datetime.time(23, 59, 59, 1000)
print(time1)


datetime.datetime()

dt = datetime.datetime(2023, 2, 25)


d1 = datetime.date.today()


d1 = datetime.datetime.today()


s1 = input("Please enter first string: ")
s2 = input("Enter second string: ")


# first check if the length is the same for both

if len(s1) > len(s2) or len(s1) < len(s2):
    print("not an anagram")
else:
    print("same length")
runfile('/Users/alexandralozser/.spyder-py3/AnagramChallenge.py', wdir='/Users/alexandralozser/.spyder-py3')





s1 = input("Please enter first string: ")
s2 = input("Enter second string: ")


# first check if the length is the same for both

if len(s1) > len(s2) or len(s1) < len(s2):
    print("not an anagram")
else:
    print("same length")
    for ch in s1:
        print(ch)



s1 = input("Please enter first string: ")
s2 = input("Enter second string: ")


# first check if the length is the same for both

if len(s1) > len(s2) or len(s1) < len(s2):
    print("not an anagram")
else:
    print("same length")
    for ch in s1:
        print(ch)  
        for ch2 in s2:
             print(ch2)
debugfile('/Users/alexandralozser/.spyder-py3/AnagramChallenge.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/AnagramChallenge.py', wdir='/Users/alexandralozser/.spyder-py3')
debugfile('/Users/alexandralozser/.spyder-py3/AnagramChallenge.py', wdir='/Users/alexandralozser/.spyder-py3')
runfile('/Users/alexandralozser/.spyder-py3/AnagramChallenge.py', wdir='/Users/alexandralozser/.spyder-py3')
+

date1.isoweekday()
from datetime import datetime

date1 = datetime(2017, 11, 10, 21, 45, 19)

str(date1)
%clear
runcell(0, '/Users/alexandralozser/.spyder-py3/DateFormatting.py')

file1 = open('sales.txt', 'r')

# Check the open mode


file1 = open('/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')
runfile('/Users/alexandralozser/.spyder-py3/Files_IO_Processing.py')

file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')
%clear


file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

# Check the open mode
file1.mode


# Read the file - One record at a time using readline 
record1 = file1.readline()

records = file1.readlines()

file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

# Check the open mode
file1.mode


# Read the file - One record at a time using readline 
record1 = file1.readline()

# Reposition the file pointer
file1.seek(0)

# Read all the records from the current pointer
records = file1.readlines()


# Close the file
file1.close()
%clear

file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

# Read all the records from the current pointer
records = file1.readlines()


total = 0.0

for record in records:
    order_id, trans_value = record.split(",")
    total += float(trans_value)


total = round(total, 2)
"""

# Open the file
file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

# Read all the records from the current pointer
records = file1.readlines()

# READLINES IS NOT RECOMMENDED WHEN USING LARGE FILES


total_2 = 0.0

for record in file1:
    order_id, trans_value = record.split(",")
    total_2 += float(trans_value)


# specifying how many digits after the period do we want
total = round(total_2, 2)
file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

# Read all the records from the current pointer
records = file1.readlines()

# READLINES IS NOT RECOMMENDED WHEN USING LARGE FILES


total_2 = 0.0

for record in file1:
    order_id, trans_value = record.split(",")
    total_2 += float(trans_value)


# specifying how many digits after the period do we want
total = round(total_2, 2)


file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

# Read all the records from the current pointer
#records = file1.readlines()

# READLINES IS NOT RECOMMENDED WHEN USING LARGE FILES


total_2 = 0.0

for record in file1:
    order_id, trans_value = record.split(",")
    total_2 += float(trans_value)


# specifying how many digits after the period do we want
total = round(total_2, 2)
file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')

# going through the file, checking if the second float is above 150.0

file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'ra')

# going through the file, checking if the second float is above 150.0
file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')
file2 = open('salestype.txt', 'w')
runfile('/Users/alexandralozser/.spyder-py3/WritingToFiles.py')

file1 = open('/Users/alexandraLozser/Desktop/Python Masterclass Materials/Skillshare Classroom Handsons/sales.txt', 'r')
file2 = open('salestype.txt', 'a')

# going through the file, checking if the second float is above 150.0
# if yes, add an H after
#if no, add an L after

comparator = 150.00

for record in file1:
    order_id, trans_value = record.split(",")
    
    if float(trans_value) < 150.00:
        file2.write(record + ",L")
    else:
        file2.write(record + ",H")
runfile('/Users/alexandralozser/.spyder-py3/WritingToFiles.py')
debugfile('/Users/alexandralozser/.spyder-py3/WritingToFiles.py')
runfile('/Users/alexandralozser/.spyder-py3/WritingToFiles.py')
debugfile('/Users/alexandralozser/.spyder-py3/WritingToFiles.py')
runfile('/Users/alexandralozser/.spyder-py3/WritingToFiles.py')
runfile('/Users/alexandralozser/.spyder-py3/OpenWithFiles.py')
%clear
runfile('/Users/alexandralozser/.spyder-py3/functions.py')
runfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
debugfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
runfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
debugfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
runfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
debugfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
runfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
debugfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
runfile('/Users/alexandralozser/.spyder-py3/taxCalculationFunctionExercise.py')
runfile('/Users/alexandralozser/.spyder-py3/twoSumChallenge.py')
debugfile('/Users/alexandralozser/.spyder-py3/twoSumChallenge.py')