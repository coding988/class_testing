# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print("hello")




import pandas as pd


import datetime

x=10
y=5.1
z=x*y
print(z)

print(type(z))
print(type(x))
print(type(y))

x=100
x=+15
print(x)


x=10
y=11
print(x==x)
print(x==y)


x= "hello"
y='hello'
print(x==y)

x='abc'
y='123'
print(x+y)

x+=y
x

#MAHNOOR
#### fix the following errors!
#### do not use any web-based resources to figure them out

##LAB2##

#1
x='10'
y='20'
print(x + y)



#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list)
print(len(my_list))



#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z[2] = 'd'
print (z)

#5 run all these lines at once. why does the x not display 10,
#followed by the 200? Fix it so it does.
x = 10
x
y = 20
print(x * y)
#6
name="blue"
color = 'My favorite color is {}, what is yours?'.format(name)
print(color)
#7
name="yellow"
color = 'My favorite color is {}, what is yours?'.format(name)
print(color)
#8
name="red"
color = f'My favorite color is {name}, what is yours?'
print(color)
#### answer the following questions by adding lines, but without changing the code

#9 make the entries in this list unique
schools = (set['harris', 'booth', 'crown', 'harris', 'harris'])

print(schools)

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])

animals[2] = 'cat'  
animals = tuple(animals)  
print(animals)

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
lower_case= my_sent.lower()
print(lower_case)
space_string=my_sent.split()
print(space_string)

