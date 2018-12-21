"""
The Dictionary: a nice data type for storing lots of information
Like lists, but instead of being indexed by numbers, they can be indexed by 
any "immutable" data type (e.g. strings)
Dicts are structured in such a way that they are very speedy at looking up items.

Dictionaries crop up EVERYWHERE in Python.
(FYI: They're a variant on a more general computer science construct called a 
"hash table").

"""


#You can construct one with curly braces like so:
my_dict = {'key1':'hello',
           'key2':'world'}

#or bit by bit:
my_dict = {} # or dict()
my_dict['key1'] = 'hello'
my_dict['key2'] = 'world'

# and lookup like so:
my_dict['key1']

type(my_dict)

# 'Keys' are immutable, 'values' are mutable. Values can be pretty much 
# anything, including DataFrames :)
# For efficiency purposes, they are also unordered
my_dict[0] 
# error! dicts 0 is not a key, and it doesn't make sense to look 
# at the "first" key in a dictionary

# you can check all your keys/values like this:
my_dict.keys()
my_dict.values()

# and both at once:
my_dict.items() # useful for looping
    
for key, val in my_dict.items():
    print('Key "{}" goes with value "{}"'.format(key, val))


#==============================================================================
# One use of a dictionary: as a "mapper"
#==============================================================================

import pandas as pd
from numpy import random

# create some dummy data
data = pd.DataFrame(
        {'codes':random.randint(0,high=10,size=30), # random numbers from 1-10
         'more_data':random.normal(size=30) # random numbers from normal distribution
         } 
        )
                    
# Now what if we want to map some descriptions onto these codes?
# We can capture this information in a dictionary:
description_mapper = { 1:'Industry 1',
                       2:'Industry 2',
                       3:'Industry 3',
                       4:'Industry 4',
                       5:'Industry 5',
                       6:'Industry 6',
                       7:'Industry 7',
                       8:'Industry 8',
                       9:'Industry 9',
                       0:'N/A'
        }

data['descriptions'] = data['codes'].map(description_mapper)
# easy!

#==============================================================================
# Another use: storing lots of DataFrames in one dict.
#==============================================================================

# This example will write some files out to your current working directory,
# read them all in to one dictionary, then delete them again.

import os

#optional: switch to D drive
os.chdir('D:/')

# create the data and save them as individual csv files
# this will write them out to the current working directory.
for file in range(1,6):
    my_data = pd.DataFrame({'var1':[i for i in range(10)],
                            'var2':random.randint(10,size=10)})
    my_data.to_csv('my_data file {}.csv'.format(file))

# now here's where a dictionary might come in handy: we can read all of these
# files at once and store them in a single dictionary. That's much easier
# than writing out a read_csv for each file and storing it in it's own variable.

data_store = {} # start with empty dict
for file in range(1,6):
     # create a key for each one and read in the data as its value
    data_store['File {}'.format(file)] = \
    pd.read_csv('my_data file {}.csv'.format(file))
   
# so what are my keys?
data_store.keys()
# and how can I access the data?
df = data_store['File 1']
# easy!

# now to delete those dummy files using an os function 
# (be careful with your use of this one!)
for file in range(1,6):
    file_to_delete = 'my_data file {}.csv'.format(file)
    try:
        os.remove(file_to_delete)
        print('Deleted {}!'.format(file_to_delete))
    except FileNotFoundError:
        pass
    

#==============================================================================
# Miscellaneous useful things.
#==============================================================================
# (1) What if you look up a key that doesn't exist?
my_dict = {'fishes':3,
           'cats':6,
           'dogs':4}


my_dict['horses'] # this throws a KeyError

# suppose instead you want any missing key to return something else, like
# the string "missing_value":
my_dict.get('horses', 'missing_value!') # returns 'missing_value!'
my_dict.get('dogs', 'missing_value!') # returns 4


# (2) How do you invert a dictionary? (mapping values to keys)
# (this won't work if your keys are certain data types like lists)
inverted_dict = {v:k for k,v in my_dict.items()}
# note how you can perform "dictionary comprehensions" just like lists 
# comprehensions!

# (3) Using a dictionary to pass arguments to a function

def lots_of_args(arg1, arg2, arg3, arg4, arg5):
    """ Example function.
    """
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
    print(arg5)
    
# you can use a dictionary like so:
arg_dict = {'arg1':'some_value',
            'arg2':'another_value',
            'arg3':'and_another',
            'arg4':'yet_another',
            'arg5':'final_value'}

lots_of_args(**arg_dict)

# you have to include all the arguments in the dictionary. you can specify
# some of them separately in the function call too:
arg_dict = {'arg1':'some_value',
            'arg2':'another_value',
            'arg3':'and_another'}

lots_of_args(arg4='a',arg5='b', **arg_dict)

#==============================================================================
# For info: extensions on dictionaries (more advanced)
#==============================================================================
# you can use this one to have the dictionary retain the order of key insertion
# (although this somewhat defeats the point of having a dictionary)
from collections import OrderedDict

# also see defaultdict


"""
One more thing: you can save dictionaries to your computer if you like, however
you will have to use a special format.

Both the "JSON" and "pickle" formats allow you to save dictionaries.

Examples below:

"""

import json # JavaScript Object Notation: very general storage format (not python-specific)
import pickle # storage format specific to python - can store almost any python object


test_dict = {'a':1,
             'b':2,
             'c':3} 

# write out to D:/ drive as a json:
with open('D:/dict_to_json.json', 'w') as f: # w = write
    json.dump(test_dict, f)

# and to read again:
with open('D:/dict_to_json.json', 'r') as f: # r = read
    reloaded_test_dict = json.load(f)
print(reloaded_test_dict)
    
# very similar for pickle:    
with open('D:/dict_to_pickle.pickle', 'wb') as f: # wb = write binary
    pickle.dump(test_dict, f)

with open('D:/dict_to_pickle.pickle', 'rb') as f: # rb = read binary
    reloaded_test_dict_pickle = pickle.load(f)
print(reloaded_test_dict_pickle)
