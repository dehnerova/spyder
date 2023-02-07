a = 10

b = 10.0

c = 10j

print(a, b, c)

type(c)

#Change the data type from Integer to Float or Float to Integer
#Casting an int to float (float needs decimal)

x = float(a)

#Casting float to int

y = int(9.7)

#cannot convert complex to int/float

x = float(c)

d = complex(a)

#most used functions in numeric variables

#abs or absolute 

x = -9.5
abs(x)

# round function to round off after decimal point

c = 10.8714623
round(c, 2)
# ^ float, number of ints after decimal

#pow or power function
#a = 10, to the power of 2
pow(a, 2)

var1 = 6
var2 = 8

var1exp = x**2 #square of x
var2exp = x**3 #cube of x

x += 10 #same as x = x + 10, etc


# math functions

a = 20 

import math

math.isfinite(a)
math.isnan(a)
math.sqrt(a)
math.exp(a)
math.log(a)
math.pi