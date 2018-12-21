"""
Python exercises set 1.
These exercises go with "python_notes_part1.py".

Topic: "Pure" Python



################################# Question 1 #################################
  a. 
    Create a list that contains at least 5 elements, with at least 3 different 
    data types. Assign it to the variable "my_list".
  b.
    Print out the type of the first and last element in my_list.
  c.
    Use a for loop to print out the type of every element in my_list.
    If you can, print out what the element is as well in the same loop.
  d.
    Use a "for loop" and an "if" statement to print out only the elements in 
    my_list that are strings.
    Hint: remember Python's "comparison operator" is ==, not = (which is the
    "assignment operator")

################################# Question 2 #################################
  a.
    Suppose x = [1,2,55]
    Write a line that trebles this list/vector - i.e. you should get 
    [1,2,55,1,2,55,1,2,55].
    Hint: some of the mathematical operators work on lists...

  b.
    Use the same logic to write a function that trebles any given list/vector.
    Remember a function looks like this:

    def func_name(arguments):
        # code
    
    It needs a "def", a name, a colon and the body of the function should be 
    indented. Arguments (inputs for the function) are optional.

################################# Question 3 #################################

    ugly_string = r'     6*23H71*i31dD*8EN*/*3m5E*s35Sa60G984e*   '

    Suppose we wanted to extract some useful things from this string.

  a.
    Use a string method to get rid of the spaces at the beginning and end of
    ugly_string. Assign this to a new variable.
  b.
    Use a string method to replace all * characters in your new variable with
    an empty character. Assign this to a new variable.
  c.
    Use a string method to turn all the characters in your new variable to 
    lower case. Assign this to a new variable.
  d.
    Use a string method to find all the characters in your new variable that
    are letters. Assign this to a new variable. What's left?
    
    Hint: you can google how to do some of these if you don't know the name of
    the method to use.
    
    N.B: you can do more sophisticated pattern-searching in text using the
    "re" module (regular expressions)
    https://docs.python.org/3/howto/regex.html
    
    
    
################################# Question 4 #################################

    For this question we'll use a function from numpy's "random" module. Make 
    sure you import the module like so:
    from numpy import random
    
    This module generates random numbers. We'll generate some numbers from a 
    normal distribution. Generating a single number works like this:
    random.normal()
  a. 
    Pull up the documentation on random.normal in Python. What do the three
    optional (keyword) arguments do? What are their default values if you leave
    them blank?
  b.
    Generate a random number from a normal distribution with mean 10 and 
    standard deviation 3.
  c.
    Generate a list of 1000 numbers drawn from the same distribution as in b.
  d.
    Use the numpy module to calculate the mean and standard deviation of your
    list from c. Are they close to 10 and 3? 
    Hint: if you don't know what the numpy functions are for mean and standard
    deviation, google them!
    
  
"""





"""
Python exercises set 1 - solutions

FYI: There is rarely a definitive "right" answer - there are usually multiple 
ways to do the same thing. Go for the simpler one if you have to choose.
"""

#==============================================================================
# Question 1
#==============================================================================
# a.
# There are LOADS of types you could include, this list has 6 different types.
my_list = ['a',1,['nested_list'],True,range(10),'hi!!!',3.141]
# b.
print(type(my_list[0]))
print(type(my_list[-1]))
# c.
for thing in my_list: # you can call it "thing", "x", "element"; whatever
    print(type(thing))

# To also print out the element, this is my preferred way of doing it:
# in some older tutorials you will probably see something similar using "%s"
# or "%d" instead. They do the same thing.
for thing in my_list:
    print('Element {} has type {}!'.format(thing, type(thing)))

# you could also do something like this:
for thing in my_list:
    print(thing)
    print(type(thing))
    print('\n') # \n creates a line break

# d.
for i in my_list:
    if type(i) == str:
        print(i)

# you may also see people using the "isinstance" function to check types 
# instead of using ==


#==============================================================================
# Question 2
#==============================================================================
# a.
x = [1,2,55]
x*3

#b.
def trebler(some_vector):
    return some_vector*3

# example uses
trebler([1,2,55])
trebler(['a','b',1,3])
trebler([i for i in range(10)])

#==============================================================================
# Question 3
#==============================================================================

ugly_string = r'     6*23H71*i31dD*8EN*/*3m5E*s35Sa60G984e*   '
# a.
new_var = ugly_string.strip()
print(new_var)
# b.
new_var = new_var.replace('*','')
print(new_var)
# c.
new_var = new_var.lower()
print(new_var)
# d.
new_var = [i for i in new_var if i.isalpha()]
print(new_var)

# If you want you can stitch this back together into a new string like so:
new_var = ''.join(new_var)
print(new_var)

# you can do more sophisticated stuff with strings with the re module,
# but this is beyond the scope of the training.
# here's a sample shorter solution to this problem:
import re
ugly_string = r'     6*23H71*i31dD*8EN*/*3m5E*s35Sa60G984e*   '

message = ''.join(re.findall('[a-zA-Z]+',ugly_string)).lower()

#==============================================================================
# Question 4
#==============================================================================
# a.
# You can pull up the documentation like so:
# NB: if you get a NameError when trying this, you need to import the module:
from numpy import random
help(random.normal)
# This function returns a number drawn from a normal distribution.
# The first argument is "loc". This is the mean of of the distribution to draw 
# from, and the  default is zero.
# The second argument is "scale". This is the standard deviation of the 
# distribution to draw from. The default is 1.
# The third argument is "size". This tells is how many values to return. The
# default is None (which is practice just gives you one value)

# So if you were to call the function like so:
random.normal()
# You would get a single number drawn from the normal distribution with mean 0 
# and standard deviation 1. But you can alter these parameters easily like so:
random.normal(loc=100, scale=20, size=3)
# or you can omit the names if you want (but it's usually better to keep them
# in the clarity, otherwise you have to memorise the argument order):
random.normal(100, 20, 3)


# b.
random.normal(loc=10, scale=3)

# c.
list_of_nums = random.normal(loc=10, scale=3, size=100)

# note that this technically isn't a list:
type(list_of_nums)
# this is called a "numpy array", but you can convert this back to a list 
# easily:
list(list_of_nums)

# d.
import numpy as np
np.mean(list_of_nums)
np.std(list_of_nums)
