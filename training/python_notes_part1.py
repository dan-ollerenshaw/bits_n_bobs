"""
This script contains notes to accompany the Python training lectures/practical
sessions.

This section of the notes handles "pure Python" stuff (i.e. the building blocks
of the language). It's important to understand this before moving on to working
with data. 

It is intended that the user works through exercises alongside this script.

Some background on Python:
- It's a general purpose programming language. People use it in many different
  domains. At ONS, we typically use it for processing and analysing data.
- It's very popular (easily in the top 5 languages worldwide by usage). So much
  so that it's now being taught in schools.
- It's considered one of the easier languages to learn.
- It was named after Monty Python!


Additional info:
- To install Python at ONS, you'll need to submit a service desk request.
  I Want Something -> Software/Applications -> Desktop/Laptop Software ->
  Add/Remove.
  Look for "PYTHON 3.6" (the latest version at the time of writing, don't use
  Python 2.7)
- This is a ".py" file, which means it contains Python code. You can open it
  in a Python IDE (e.g. Spyder) or in a text editor like Notepad.
- Any line beginning with a "#" is a comment.
- Multiple lines enclosed in triple quotation marks (like this block) are
  also comments.
- You may also see "#%%" lines in some .py files. These are specific to the
  Spyder IDE, and delimit different "cells", so you can run the code bit by
  bit.
"""

#==============================================================================
# Working with different data types.
#==============================================================================
"""
A fundamental part of programming is dealing with data "types".
Some of the common types that we will explore here:
  - Integer (whole numbers)
  - Float (numbers with a decimal point)
  - String (text)
  - Boolean (True or False)
  - List (a "sequence" of data)
"""

print()


# Do some maths:
# addition/subtraction
1+1
2+1.1
5-3
# multiplication/division
10*2
4/2
7/3 # anything odd about this?
# some more operators
2**3 # exponent
10//3 # floor division
5%3 # modulo

# Integers and floats usually interact with each other nicely.

# Quick note on the print() function:
# You can do the same as above like this:
print(1+1)

# The print() function pops up it's input to the screen.
# If you're working in an IDE like Spyder, entering 1+1 without wrapping it
# in print() will achieve the same thing. However, if you want to run your
# scripts as programs from the command line, you'll need to wrap statements
# in print() if you want them to show up.


# Text (alphanumeric)
# Anything that is text needs to be enclosed in apostrophes/speech marks
# There are a few ways you can do this:

'This is text'
"So is this"
''' me too '''
""" and me! """
# I tend to prefer the first one.


# Some mathematical operators also work with strings, and some don't:
'hello' + 'world'
'hello' * 3
'hello' + 1 # error!


# Special string characters.
# What do these do?
print('hello\tthere')
print('hello\nthere')
print('hello \'SIR\'')
print('\u2665')


# if you want to ignore the behaviour of these, you can use a "raw string":
print(r'hello\tthere')
#for the last one:
print("'hello 'SIR'")

# There are some other useful things we can do with strings beyond using 
# the mathematical operators  by using a . after the text. This allows
# yoo to access so-called "methods" and "attributes" (explained later)

# what do these do?
'mississippi'.upper()
'mississippi'.capitalize()
'mississippi'.count('s')
'mississippi'.replace('s','_',3)

# how do you find out exactly how to use these?
# all three of these are pretty much equivalent.
str.replace?
?str.replace
help(str.replace)



# for some functions, if you include two question marks, you can get the
# full source code!

# you can also find a full list of available functions for that data type:
dir(str) # remember this one!!
# Different data types will have different functions available for it.

# There is another data type that is extremely useful to us and that is a
# BOOLEAN data type. This is extra fancy-schmancy speak for 'true or false'.
# We access these in python by using the keywords
True
# and
False
# Note that you must capitalise them like this or you won't get your desired
# functionality. It will help that other ways of writing them won't turn the
# colour you expect.

# Boolean values have some interesting attributes available to them.
# e.g.
True.real

# What does this mean your computer reads True as?


# There is a built in way in which we can find out what type of object we are
# working with:
type('mississippi')
type(19)
type(3.141)
type(False)


#==============================================================================
# Assigning variables
#==============================================================================

# Worked example
# assign first_int the value 6, assign first_float the value 3.1 and set
# first_bool to be true (how many ways can you do this?)
first_int = 6
first_float = 3.1
first_bool = True

print(first_int + first_float)

# when you run this line, Python will wait for you to enter something.
name = input('Who\'s your hero? ')


# print statements including variable values
#-------------------------
print('Wow! %s is a great role model!' % name)
#or
print('Wow!', name, ', is a great role model!')

print('Wow! ' + first_int + ', is a great role model!') # what happens here?

# The recommended way to do this in python 3 is this:
print('Wow! {} is a great role model!'.format(name))

# You can be quite expressive with this, and it also accepts most non-strings:
print('This statement combines {} and {}!'.format(name, first_int))

# or:
print('This statement combines {name} and {number}!'.format(name=name,
                                                            number=first_int))

# Multi-line:
print("""
This string spans many lines.
      

          
woah. Nice one {}.
     """.format(name)
     )


# Now that we know about variables, let's introduce another data type, list:
# lists are enclosed in square brackets.
my_list = [7,'z',True]
type(my_list)

# what do you think will happen if you enter this?
my_list[1]

#not what you expected? in programming, we start counting at zero!
my_list[0]

# what would you have to do to print the "True" value?
my_list[2] # correct
my_list[-1] # also correct, counting backwards


# a few more things with lists:
my_list * 3

another_list = [1,2,[3,4]] # there's a "nested" list here

combined_list = my_list + another_list

# how would you access to "4" from combined_list?
combined_list[-1][-1]


# you may also encounter the " tuple" type. This is very similar to a list,
# and is created with round brackets
my_tuple = ('a','b','c')
type(my_tuple)

# There's a crucial difference though, items in lists can be changed, but
# items in tuples cannot:
my_list[0] = 'new value!'
my_tuple[0] = 'new value!' # error!



#==============================================================================
# Comparison operators and "control flow"
#==============================================================================
"""
When you write a python program, you may want it to take one of many possible
"branches".

E.g., 
- if this variable is positive, do this, but if it's negative, do that.
- if your data has more than 10 missing values, do this, 1-9, do that, 0, do 
nothing.

How do we do this?
"""

# checking for equality
1 == 0
1 == '1'
# note difference between "=" and "=="
# "=" assigns variables, "==" compares two things.
1 != 0 # not equal to
10 <= 20

# equivalents for strings...
'a' in 'alphabet'
'beta' not in 'alphabet' # looks for whole string

('un' in 'statistics is fun'.split()) # why is this one false?
                                      # what does .split() do?

# and lists...
1 in [1,2,3]

# combine two:
(1 > 0) and ('a' == 'b') # you might see "&" instead of and (ampersand)
(1 > 0) or ('a' == 'b') # you might see "|" instead of or (pipe)
  


"""
Quick note on whitespace:
    
Python has some rules about how you structure your code.
Specifically, indentation is required in certain cases, particularly
for defining functions, using loops, and writing "if/elif/else" conditions
(we'll come onto all of these).

Either 2 spaces or 4 spaces are acceptable indent levels.
I recommend 4 spaces.
In most IDEs, pressing tab creates 4 spaces, which makes it easy.
"""

# Using correct indentation: running the following lines as a block won't work,
# be consistent!
x = 1
 y = 2
  print('something')


#==============================================================================
# if / elif / else: conditional statements
#==============================================================================
response = input('Press A or Z.')
print(response)

# Let's start with a simple condition
# note the indentation!
if response == 'A':
    print("some kind of response to A")

# Looking at the instructions the user might think that pressing the A key
# is all that is needed and might not consider capitalisation - there is a way
# to deal with this:
if response.upper() == 'A':
  print("some kind of response to A")

# And that deals with the one scenario. but what if they pressed Z? 
# how do we account for that?

# We could write multiple IF statements:
if response.upper() == 'A':
    print("some kind of response to A")
if response.lower() == 'z':
    print('Well, z is the better option.')

# but this is cumbersome and CPU intensive (it tests all conditions every time)
# instead we have the ability to test for an A and if it isn't an A then test
# for a Z:
if response.upper() == 'A':
    print("some kind of response to A")
elif response.lower() == 'z':
    print('Well, z is the better option.')


# There is also the chance that your user is not paying attention to what you
# want them to do and go off on their own and press some other key. There is a
# mechanism by which we can catch this without more IF statements:
if response.upper() == 'A':
    print("some kind of response to A")
elif response.lower() == 'z':
    print('Well, z is the better option.')
else:
    print("Oops, you didn't press either!!!")


# here's another if/elif/else example!
# try running this and see what happens!!
# can you follow the logic, even if some of the code is unfamiliar>
import getpass # we'll explain this later.
your_username = getpass.getuser()
vowels = ('a','e','i','o','u')
vowel_count = 0
# this is a "for loop"
for vowel in vowels:
    count = your_username.count(vowel)
    vowel_count += count # this syntax is very common. equivalent to:
    # vowel_count = vowel_count + count
print('Your username has {} vowels!'.format(vowel_count))


#==============================================================================
# For loops
# (and while loops, briefly)
#==============================================================================
# Loops are great, you can do lots of things at once!
# they require you to indent, just like with if/elif/else:

my_list = ['a','b','c',1,2,3]

for item in my_list:
    print(item)

# I've chosen to call each thing "item" arbitrarily, but you can call it 
# anything. (but preferably call it something relevant)

# whitespace is crucial, these two loops produce different results:
    
# can you tell what each of these do before trying it?
a = 0
for i in [1,2,3]:
    a = a+i
print(a)

a = 0
for i in [1,2,3]:
    a = a+i
    print(a)

# what if you want the numbers 1-10, and you don't want to type them all out?
# list function does what it says on the tin:
list(range(10))
# does it do exactly what you expect?

# other uses of range() function:
list(range(5,20))

list(range(0, 10, 2))

range? # (start, stop, step)


# While loops:
# what do you think this will do?
x = 0
while x < 10:
    x = x+1
    print(x)

# use for loops when you know exactly how many times you want to do something,
# and while loops when you just want to do something until a particular
# condition is met.

# be careful with loops though... what does this one do?
a = 0
while True:
    a += 1    # same as a = a + 1
    if a%10 == 1:
        print(a)



# Quick note on "list comprehensions"
# Sometimes you will see people using the following type of shortcut when using
# a for loop:

#regular version:
even_numbers = [] # start with empty list
for i in range(20):
    if i%2 == 0: # this is another way of saying "if i is even"
        even_numbers.append(i) # add it to list
print(even_numbers)
    
[i for i in range(20) if i%2 == 0] # identical

# This is called a list comprehension.


#==============================================================================
# An introduction to functions
#==============================================================================


# Functions exist to allow you to write blocks of code that you will re-use
# over and over without having to write that same code again and again. You
# have already seen some functions above: help, dir and print.

# To CALL a function you say its name and then give the arguments that it
# expects in order to be able to run and perform its functionality.

# To CREATE a function we have to use some built-in python
# functionality and make use of whitespace.


def hello_world():     										      # Function header
    """ This is a docstring, these are important! """		# Function body
    print('Hello world!')										   # Function body


# Notice that everything that belongs to the functionality of hello_world is
# indented after that line and it is all indented the same amount
# We end the definition of the body of the function [its functionality] by
# moving back to the level of indentation that begins the definition [0 here]

# "call" the function:
hello_world()

# find out how it works:
help(hello_world) # neat!


# Our hello world function is pretty simple, it doesn't accept any arguments
# and prints out a single thing every time, let's extend it to say hello to
# whatever we tell it to say hello to.
def hello(txt):
	""" say hello to txt """
	say_hello = 'Hello {}!'.format(txt)
	print(say_hello)

hello('bob')
# Now we have a more general function that says hello to anything we want!

# If we don't enter an argument, the function won't work:
hello()

# but we can change the function to have a "default" value if nothing is
# entered for txt:
def hello(txt='world'):
	""" say hello to txt """
	say_hello = 'Hello {}!'.format(txt)
	print(say_hello)

hello()
hello('bob')


# Let's look at a more mathematical example. Suppose we want to take any number
# and return the value of that number squared.

def square(n):
    """ Function to return [note: not print!] n squared """
    squared_value = n**2
    return squared_value

# Let's check that it works:
five_squared = square(5)
print(five_squared)


# What's the difference between return and print? see below:
def square_and_print(n):
    """ Function to return [note: not print!] n squared """
    squared_value = n**2
    print(squared_value)


square(5) + 10
square_and_print(5) + 10 # error!
# print only flashes up the answer on screen, you can't keep the answer
# for use further on. Use "return" for this.


# A (very) brief introduction to scope
#-------------------------------------
# In the above we have defined square_value as a new variable inside the
# square function.
# We have already run the function once, on n=5 so let's see if we can just
# access the value
print(squared_value)

# The reason that this doesn't work is that squared_value only exists inside
# the function square, this is called the 'local scope' of the function.
# As soon as the function finishes what it is doing, all of the variables
# created inside it are deleted and not available to anything any more.
# so be careful!



#==============================================================================
# Modules (aka libraries)
#==============================================================================
"""
So far, we've pretty much exclusively used "pure" python functions. But the
beauty of an open-source language like Python is that users can contribute
their own code as "modules", which you can then use yourself!

To use a module, you just need to import it.

Most of the modules you'll want to use come pre-installed with Anaconda.
If you want to install a new one, the procedure is a little tricky at ONS
since we can't download directly from the internet, ask me if you need to do 
so.
"""

# importing modules one by one, retaining their names
import os
import sys

# alternatively: import os, sys

# importing a module but giving it a nickname
# these ones we use a lot!!!
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



""" 
So what does "importing" something do?

It allows you to access functions within that module.
I can now enter "os.listdir()" for example.
Without importing the os module first, I cannot use the .listdir() function.


You should only import modules you actually intend to use, otherwise you're
"polluting your namespace". Basically this means you avoid naming clashes
with your variables vs. functions from imports (for example).
"""

# what do these do?
os.getcwd() # "get current working directory"
os.chdir('C:/') # "change directory"
os.listdir() # list directory contents
# there are many more...

# what about the ones we used a nickname (alias) for, e.g. numpy?
np.mean([1,2,3])
np.max([1,2,3])

# saves us having to type numpy.function every time
# if we just want a few functions, we can also import them specifically:
from math import pi
print(pi)

# the alternative gives the same answer:
import math
print(math.pi)



# The next notes script will introduce the pandas module, which is a powerful
# library for working with data. (pandas = panel-data)

#==============================================================================
# Annex: coding style guidance
#==============================================================================
"""
As a beginner, you should focus mainly on writing code that works first
and foremost. However, as you gain more experience, you should be aware
of how your code is structured (more than just indenting properly).

The official style guide is here:
https://www.python.org/dev/peps/pep-0008/

In general you should keep the following things in mind:
- COMMENT YOUR CODE!!! Even if no one else reads it, if you come back to it
  in 6 months and there's no explanation of what's going on, your code won't be
  much use.
- Your code should be as simple and easy to read as possible.
- Try to keep each line of code to a maximum of 100 characters.
"""

