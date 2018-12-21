"""
This script contains notes to accompany the Python training lectures/practical
sessions.

This section of the notes handles working the data using the pandas module.

It is intended that the user works through exercises alongside this script.


WIP
"""


#==============================================================================
# Reading and writing data.
#==============================================================================

# Pandas is a module for python which adds functionality similar to R's
# dataframes to python. This is a very good thing to have and it has a lot
# of really powerful built in capability.

import os
import numpy as np
import pandas as pd # pd is the typical alias for the module
import string

# Reading CSVs
"""
First run the following block to create some dummy data to experiment with.
This script will write a csv file to your D: drive, if that's not a suitable
place then change the "savepath" variable to something more suitable.
"""
savepath = 'D:/'
alphabet = string.ascii_lowercase
nrows = len(alphabet)
data = pd.DataFrame({'person_id':[l for l in string.ascii_lowercase],
                     'age':np.random.randint(low=1, high=100, size=nrows),
                     'eye_colour':np.random.choice(['blue','green','brown'], size=nrows),
                     'password':[''.join(np.random.choice([l for l in string.ascii_letters], size=8))\
                                 for i in range(nrows)]
                     })
data.to_csv(savepath+'dummy.csv', index=None)


# Ok, let's read in this dataset and store it in a variable called "df"
# (for DataFrame). We'll use the read_csv function from pandas:

df = pd.read_csv(savepath+'dummy.csv')
# NOTE: be careful, python works in memory, that means your entire file
#       is read into RAM as part of this function. 
#       This should be your biggest consideration when you are writing programs
#       working with data.

# let's have a look at some of the properties that are built into the
# data frame object
print(df.shape)
df.head()
?df.shape
?df.head
?df.tail # for the opposite end

# What type of object is df?
type(df)
dir(df)# there's loooads of things we can do with it, in general you should 
       # ignore anything in this list beginning with an underscore.

## There are loads and loads of different formats available built in to pd.
## pd.read_<tab>
pd.read_sas
pd.read_table
pd.read_excel
pd.read_csv
pd.read_stata
pd.read_fwf


# There are more options as well with read_csv, its arguments let you specify
# all kinds of things. Can you find out how to see the arguments in your
# preferred editor? How else might you get them?


# Writing CSVs
# We already saw how to do this above, just use the pd.to_csv function:

## doing this from a dataframe is really easy.
# this will save in the current working directory if you don't specify
# a filepath
df.to_csv(savepath+'new_csv_file.csv')
# try opening this with excel
# What about this file don't you like?

# try this instead:
try:
    df.to_csv(savepath+'new_csv_file.csv', index=False)
except:
    print('Oops, it didn\'t work - maybe the file is open in excel?')

# we'll come onto try/except later. it's pretty darn useful.



# Suppose you wanted to write an excel file instead of a csv, the basic syntax is:
# (run this as a block)

# this basically specifies the filename to write to
writer = pd.ExcelWriter(savepath+'first_excel_file.xlsx') 
df.to_excel(writer, sheet_name='my_sheet') # write df to the file, specifying the sheetname
writer.save() # save

#==============================================================================
# Handling data.
#==============================================================================
# Once you've successfully read your data, what are some common things you
# might do with it?
df = pd.read_csv(savepath+'dummy.csv')

# inspect the columns
print(df.columns)
# access just the 'age' column:
df['age'] # df.age is also valid, but not preferred
df['age'].head()
# what type of object is this column?
type(df['age'])
# Series and DataFrame are the two main data types pandas works with.



# inspect the rows
print(df.index) # pandas creates an "index" to go with the DataFrame 
# (row names, the default is just 0-n), but you could set a column as the index,
# e.g.:
df.set_index('person_id')
# this method hasn't actually changed df, it's just showing you what would 
# happen if you applied this on df.
# you can apply it by assiging it to a new variable (df)
df = df.set_index('person_id')

# access a particular row:
df.loc['x']
df.iloc[0]
df.iloc[10:] # slicing
# use loc to access a row by it's actual index value, and iloc to access a row
# by it's numerical position (0 = first row)

# let's reset the index back to how it was before:
df = df.reset_index()

# add a new column!
df['ones'] = 1 # adds a column of ones
df['age_plus_one'] = df['age'] + 1 # add a column based on another column

# sorting data:
data.sort_values(by='age') # default is low to high
data.sort_values(by='age', ascending=False) # high to low

# Filtering rows based on a single condition.

# In order to filter rows we need to pass a series of True and False values
# through the square brackets indicating whether each row is to be kept or
# ignored.

# Let's think back to the control flow section
df['eye_colour'] == 'green'

# Then using this as the argument to the square brackets:
df[ df['eye_colour'] == 'green' ]
# you can read this as "df where eye_colour equals green"


# Alternatively:
green_eyes = df['eye_colour'] == 'green'
df[ green_eyes ]
## This is perfectly fine code.

# Subsetting rows on multiple conditions
# use an & for AND and a | for OR
df[ (df['eye_colour'] == 'blue') | (df['age'] > 30) ] 
df[ (df['eye_colour'] != 'brown') & (df['age'] >= 18) ] 

# checking for range of values:
particular_people = ['a','g','j','v']
df[ df['person_id'].isin(particular_people) ]

# negating a condition, use tilda (~):
df[ ~(df['person_id'].isin(particular_people)) ]
    

# applying string methods to columns of strings.
# remember the string methods like .upper, .capitalize, .replace? we can use
# them on pandas DataFrames!!

# to let pandas know we're using a string method, we need to preface the method
# with ".str"
df['password'].str.upper() # upper case of password col
df[ df['password'].str.contains('e') ] # df where password column contains a lower case 'e'
df['password'].str.len() # length of each password string

# here's a few other particularly useful DataFrame methods, there are many more...
df['eye_colour'].value_counts()
df.T # transpose
df.drop_duplicates()
df.describe() # summary stats on the numerical cols
df['age'].values # converts pandas object to a numpy array
df.sample(frac=0.1, replace=False) # random sampling
df['age'].astype(float) # convert the type of a column


#==============================================================================
# Checking for nulls/dodgy data
#==============================================================================

"""
let's tamper with some of the rows.
open df in excel and make some of the cells empty, and add some spaces
to the beginning/end of some of the passwords.

Then we'll fix them in python.
"""
# re-read, after making the changes:
df = pd.read_csv(savepath+'dummy.csv')

df.isnull() # True/False if value is null across whole DataFrame
df['age'].isnull() # in a particular col

# count nulls in each column
df.isnull().sum() # why does this work? what is True+True?

# DataFrame with no nulls in age column:
df[ df['age'].notnull() ]

# Handling nulls: drop or fill
df.fillna(0) # fill nulls with zeroes
df.fillna(method='ffill') # take previous value
df.dropna() # drop the rows entirely. 


df[df['eye_colour'] == 'brown']

df['eye_colour'] = df['eye_colour'].str.strip()


# Removing spaces from either side of the real data:
# check where password length is greater than 8:
df[ df['password'].str.len() > 8 ]
df['password'].str.strip() # or .rstrip() and .lstrip() to take from a specific side.



#==============================================================================
# Merging data
#==============================================================================

# here's a simple example to illustrate the main types of merge:
left_df = pd.DataFrame({'id':['a','b','c'],
                        'left_value':[100,200,300]})

right_df = pd.DataFrame({'id':['b','c','d'],
                        'right_value':[5000,3000,6000]})

# the inner merge:
inner = left_df.merge(right_df, how='inner', on='id')
# equivalent alternative:
inner = pd.merge(left=left_df, right=right_df, how='inner', on='id')

# the outer merge:
outer = left_df.merge(right_df, how='outer', on='id')
# in fact, an inner join is equivalent to outer.dropna()

# you can also do left and right joins:
left_df.merge(right_df, how='left', on='id')
left_df.merge(right_df, how='right', on='id')


# when merging, be careful that the data types of the ID column are the same!!
left_df = pd.DataFrame({'id':[1,2,3],
                        'left_value':[100,200,300]})

right_df = pd.DataFrame({'id':['1','2','3'],
                        'right_value':[5000,3000,6000]})

left_df.merge(right_df, how='inner', on='id')
# didn't work! need to convert to a common data type first, e.g.
left_df['id'] = left_df['id'].astype(str)


# Slightly different: concatenate two dataframes.

top = pd.DataFrame({'column_in_both':[1,2,3]})
bottom = pd.DataFrame({'column_in_both':[4,5,6],
                       'column_only_in_bottom':['a','b','c']})

pd.concat([top, bottom], axis=0)

# use axis=1 if you want to concatenate row-wise

#==============================================================================
# Groupby
#==============================================================================
# Groupby is useful if you want to analyse your data in different groups.
# For example, imagine you had some cross sectional data on male vs female earnings:
group_df = pd.DataFrame({'earnings':np.random.randint(0,10**5,size=1000),
                         'age':np.random.randint(18,65,size=1000),
                         'gender':np.random.choice(['male','female'],size=1000)})

# we can use groupby to compute statistics about
group_df.groupby('gender').mean()

# similar to:
group_df[group_df['gender'] == 'male'].mean()
group_df[group_df['gender'] == 'female'].mean()

# view the aggregations available:
g = group_df.groupby('gender')
type(g) # a "GroupBy" object
dir(g)

# we can do different aggregations for different variables:
g.agg({'age':'min', 'earnings':'median'})

# you can also group by multiple variables.
# create a new "age_bracket" column:
group_df['age_bracket'] = pd.cut(group_df['age'], 2, labels=['young','old'])
group_df.head(10)

group_df.groupby(['gender','age_bracket']).mean()


# N.B. you can achieve a similar result with the pd.pivot_table function.


#==============================================================================
# Applying custom functions
#==============================================================================

# Suppose you've defined your own function:
    
def my_func(x):
    """ Takes a string, x, and returns the string going backwards
    """
    return x[::-1]


# you can apply this function to a column on your DataFrame like so:
df['func_applied'] = df['eye_colour'].apply(my_func)
df.head()

# you can use applymap to apply a funtion to all columns, but usually this will
# only work if they're the same data type.

# This might be a good time to mention lambda functions...

# Sometimes you will see something like this:
    
df['age_squared'] = df['age'].apply(lambda x: x**2)

# this syntax is basically applying a function without a name. people tend
# to use it for quick-and-easy functions that they don't feel the need to 
# explicitly define. (an "anonymous" function)

# this would exactly the same as:
def square(x):
    return x**2

df['age_squared'] = df['age'].apply(square)



#==============================================================================
# Creating a column based on a condition.
#==============================================================================

# this is a bit like using =IF in excel:
    
data = pd.DataFrame({'val':[1,2,3,4,5,6,7,8,9]})


# suppose you wanted a new column. if val is <5, it gets the value "low".
# otherwise, it gets the value "high":

data['high_or_low'] = np.where(data['val'] < 5, # condition
                               'low',           # value if True
                               'high')          # value if False
    
# FYI: there are alternative ways of doing this using .loc syntax, but using
# no.where is quite popular.



"""
This covers a lot of the basic operations you might want to do with DataFrames.
For more complex operations, consulting StackOverflow is usually the best 
option.

As a general tip, try to avoid using loops in your DataFrame.

E.g. you might be tempted to do something like this to replace values
in your data:

for col in df.columns:
    for row in df.index:
        value = df[col].loc[row]
        if value == '':
            df[col].loc[row] = 'missing'

DON'T DO THIS! this is very inefficient. instead, use the appropriate
DataFrame method. In this case that would be:
df.replace('', 'missing')

This methods are optimised, and will be much faster than a loop.

Other topics still to cover:
    - dictionaries
    - working with dates
    - plotting    
    - possibly more advanced stuff if there's interest...
"""


