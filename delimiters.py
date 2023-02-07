# Introduction to split method of string

var3 = "John,M,42,8000,Software Developer"

# assigning values to multiple variables in one line
#name, age = "Alex", 24

name, gender, age, salary, role = var3.split(sep=",")

#isNumeric method
#check isNumeric before converting and performing numerical operations

salary.isnumeric()
salary = float(salary)

# strip() equivalent to trim() in java
# can provide other characters to remove, same as spaces

var4 = "John    ,M,42,  8000  ,   Software Developer\n"
name, gender, age, salary, role = var4.split(sep=',')

name = name.strip()
salary = salary.strip()

role = role.strip('\n')
var4.strip()

#lstrip - removes leading or left
#rstrip - removes trailing or right

role = role.lstrip()

#replace method
var13 = "John plays football. John plays tennis."
print(var13)

varC = input("Current value to be replaced : ")
varN = input("Please enter the new value : ")
count = input("Number of instances to be removed: ")

var13.replace(varC, varN, int(count))

# data is not always standard and sometimes needs to be modified



