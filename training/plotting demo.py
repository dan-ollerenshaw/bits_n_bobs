"""
Introduction to plotting in python.

Modules used:
- pandas
- matplotlib

For more options see:
https://blog.modeanalytics.com/python-data-visualization-libraries/
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import getpass
import re

# This time we'll use real data, download it from:
# https://www.ons.gov.uk/economy/grossdomesticproductgdp/datasets/ukgdpolowlevelaggregates
# filename might differ...

# you'll probably need to change this if you're following along
filepath = 'C:/users/{}/downloads/llaqna.xls'.format(getpass.getuser())

# fix the format of the data:
def read_and_fix(filepath):
    """ Read the data, and change the format of the sheet to one we can plot.
    """
    df = pd.read_excel(filepath,
                   sheetname='CVM £ Millions',
                   header=4,
                   index_col=2)
    df.columns = [str(col) for col in df.columns]
    sic2_cols = [col for col in df.columns if bool(re.search('\d{2}', col)) and not 'Unnamed' in col]
    df = df[sic2_cols]
    df = df.iloc[9:]
    year_indices = [i for i in df.index if str(i).isnumeric()]
    df = df.loc[year_indices]
    df = df.dropna(axis=1)
    df = df.applymap(lambda x: int(x))
    
    return df

df = read_and_fix(filepath)

#==============================================================================
# Basic plots with pandas
#==============================================================================
# we can do some basic pandas plots using the .plot method:
# let's plot output in the retail industry (47)
df['47'].plot(kind='line') # line is the default
df['47'].plot(kind='bar')
df['47'].plot(kind='barh')
df['47'].plot(kind='pie')
df['47'].plot(kind='area')

# we can do more sophisticated graphs with a module designed for it!

#==============================================================================
# Matplotlib
#==============================================================================
# Let's do the same line chart as before in matplotlib:

# the input for this is flexible, common inputs could be:
# a pandas Series (like below)
# a python list
# a numpy array
plt.plot(df['47']) # looks pretty much the same

# Let's see what else we can do with matplotlib

# we can add bits and bobs to make our chart more interesting - just put
# each addition on a new line and run the block together, e.g.:
    
plt.plot(df['47'], color='red', linestyle='--', label='retail')
plt.title('Output in the retail industry', fontsize=16)
plt.xlabel('Year'),
plt.ylabel('£ Millions')
plt.ylim([0,max(df['47'])*1.1])
plt.grid()
plt.legend(loc='upper left')

# this is just scratching the surface - you have pretty much unlimited 
# customisation with matplotlib - but you'll probably need to google a fair bit!

# for saving a plot, just add .savefig() at the end:
# make the folder:
try:
    os.mkdir('D:/test_python_charts/')
except FileExistsError:
    pass
    
plt.plot(df['47'], color='red', linestyle='--', label='retail')
plt.title('Output in the retail industry', fontsize=16)
plt.xlabel('Year'),
plt.ylabel('£ Millions')
plt.ylim([0,max(df['47'])*1.1])
plt.grid()
plt.legend(loc='upper left')
plt.savefig('D:/test_python_charts/example.png')

# some more matplotlib plots:
y2017 = df.loc[2017]

#==============================================================================
# histogram
#==============================================================================
plt.hist(y2017,
         bins=50,
         edgecolor='black'
         )
plt.xlabel('Output, £m')
plt.ylabel('Number of 2 digit SIC industries')


#==============================================================================
# bar chart, retail
#==============================================================================
plt.bar(range(df.shape[0]), df['47'])
plt.xticks(range(df.shape[0]), df.index, rotation=90);

# bar chart, retail and wholesale
# slightly more complex to set up
# quite a good way to find out how to do this is look up demos online.
n_years = df.shape[0]

fig, ax = plt.subplots()

index = np.arange(n_years)
bar_width = 0.35

bars1 = ax.bar(index, df['47'], bar_width, color='b', label='retail')
bars2 = ax.bar(index + bar_width, df['46'], bar_width, color='r', label='wholesale')

ax.set_xlabel('Year')
ax.set_ylabel('Output (£m)')
ax.set_title('Output in the wholesale and retail industries')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(list(df.index), rotation=90)
ax.legend()

plt.show()


#==============================================================================
# Plotting many graphs at once using a loop
# (1) dummy example
#==============================================================================

# Just one plot first
x_values = [np.random.randint(1,high=10) for i in range(10)]
y_values = [np.random.randint(1,high=10) for i in range(10)]
plt.scatter(x_values, y_values, s=50, marker='*', alpha=0.9) # s is the size of the dots
plt.xlim(0,10)
plt.ylim(0,10)
plt.savefig('D:/test_python_charts/scatter.png')

from matplotlib import colors
# Now in a loop - with more stars!!
# full list of 'named' colours
colours = list(colors.cnames.keys())
# taking a random 10 of them
my_colours = np.random.choice(colours, 10, replace=False)

# I'm also going to time how long it takes to run each time.
from time import clock

for colour in my_colours:
    start = clock()
    fig = plt.figure()
    x_values = [np.random.randint(1,high=10) for i in range(30)]
    y_values = [np.random.randint(1,high=10) for i in range(30)]
    plt.scatter(x_values,y_values,s=50,marker='*',alpha=1,color=colour)
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.title('{} stars!'.format(colour))
    plt.savefig('D:/test_python_charts/{} graph.png'.format(colour),dpi=150)
    plt.close() # otherwise it will save them all in memory
    end = clock()
    print('Saved \"{}\" graph, took {:.2f} seconds.'.format(colour,(end-start)))



#==============================================================================
# Plotting many graphs at once using a loop
# (2) real example
#==============================================================================
# another example
# e.g. suppose we want single line charts for the first 10 2-digit SIC industry.
# it's quite simple:

for col in df.columns[:10]:
    plt.plot(df[col])
    plt.title('Plot for industry {}'.format(col))
    plt.show()
    # make sure you put this at the end of the loop,
    # or it will put everything on one graph
    plt.close()
    
# What if you want a kind of "panel" graph, with different industries next
# to one another? you can use plt.subplots.
# let's do the biggest 5 industries in a horizontal panel.
top_5_industries = list(df.mean()\
                          .sort_values(ascending=False)\
                          .index[:5])

fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(20,4), sharex='col', sharey='row')
plot_number = 0
for ax, ind in zip(axes.flat, top_5_industries):
    ax.plot(df[ind])
    ax.set_title('Industry {}'.format(ind), fontsize=10)
    ax.grid()
    if plot_number == 0: # only put ylabel on first one.
        ax.set_ylabel('Output (£m)')
    plot_number +=1 
plt.suptitle('Output in largest five industries over time', fontsize=16)
plt.savefig('D:/test_python_charts/subplots_example.png', dpi=200)




# Couple more misc things: what if we want a unique chartname/filename when we save these things?
# this prevents us overwriting something that already exists

import getpass

getpass.getuser()

from time import strftime # 'string format time'

strftime('%Y-%m-%d %H-%M-%S')
strftime('%d%m%Y %H-%M-%S')

# For example:
plt.plot() # empty plot
plt.savefig('D:/test_python_charts/{} {}.png'.format(getpass.getuser(),strftime('%d%m%Y %H-%M-%S')))


# There is more to plotting than just matplotlib, though! e.g.:

# seaborn - recommended by Gareth
# seaborn.distplot is particularly nice for doing distributions

import seaborn as sns

