"""
Python exercises set 3.
These exercises go with "python_notes_part2.py".

Topic: Handling data with the pandas module.


For these exercises we will work with dummy data. For each question
run the code block at the top to create the dummy data. It will be saved
to your D:/ drive as "question_n.csv', where n is the question number.

If you don't want to save to your D: drive, change the savepath variable below:
"""
import pandas as pd
from numpy import random

savepath = 'D:/'


################################# Question 1 #################################

regions = ['england','wales','scotland','northern_ireland']
years = [y for y in range(2000,2018)]
df = pd.DataFrame(index=years, columns=regions)
nrows = df.shape[0]
for r in regions:
    for trend in range(nrows):
        df[r].iloc[trend] = 100 + trend*10 + random.normal(loc=10, scale=10)
df.to_csv(savepath+'question_1.csv')

"""
    Hint: every single one of these questions can be answered just by using 
    DataFrame methods :-)
  a.
     Read question_1.csv into a pandas DataFrame, and calculate the following:
      - sum of 'england' column
      - max of the 'northern ireland' column
      - mean value across countries 2010
  b.
     Round the values in the wales column to the nearest whole number, and 
     replace the original wales column with this.

  c.
     Create a new column called 'average', which contains the mean value
     of the four countries.
     
   d. 
     Create a column containing the percentage growth rate of the values for 
     england, year on year, then find the year with the highest growth rate.

"""

################################# Question 2 #################################

# For this question we'll read from an excel file instead of a csv file.
# We have two years of survey data, and we want to combine the reuslt into
# one file, keeping only people who appears in both years.

year_1 = pd.DataFrame({'Person_ID':[i for i in range(50)],
                       'Q1_response':random.choice(['a','b'],size=50),
                       'Q2_response':[abs(q) for q in random.normal(size=50)]})
year_2_ids = list(random.choice([i for i in range(50)], size=25, replace=False))\
             + [i for i in range(50,75)]
year_2 = pd.DataFrame({'Person_ID':year_2_ids,
                       'Q1_response':random.choice(['a','b'],size=50),
                       'Q2_response':[abs(q) for q in random.normal(size=50)]})
writer = pd.ExcelWriter(savepath+'question_2.xlsx')
year_1.to_excel(writer, sheet_name='year_1', index=None)
year_2.to_excel(writer, sheet_name='year_2', index=None)
writer.save()
    
"""
  a.
    This excel file has two sheets. Using the read_excel() function, open both
    sheets and store them in separate DataFrames.
  b. 
    Merge the two files into one DataFrame, using an outer join.
    
    Use the "suffixes" argument to distinguish between the responses in year_1
    and year_2.
  c.
    Generate a list of the Person_IDs who responded in year 1, but not in year 2.
  d.
    Reduce your data to only contain people who responded in both years, and
    whose respose to question 1 in year_1 was 'a'.
  e.
    Write the result out to a new csv file called "question_2_answer.csv".

"""

################################# Question 3 #################################

# Warning: this one is difficult, but it does highlight some common problems
# you'll encounter when trying to read in data and get it in a sensible format.

firms = ['Firm {}'.format(i) for i in range(40)]
turnover = ['£{:0.2f}'.format(t) for t in random.lognormal(size=40)]
sector = [s for s in random.choice(['agriculture ',
                                   'finance     ',
                                   'construction',
                                   'Construction'], size=40)]
messy_df = pd.DataFrame({'firm':firms,
                         'sector':sector,
                         'turnover, £m':turnover
                         })
messy_df.to_csv(savepath+'question_3.csv', header=False, index=None, sep='\t')

"""
This question will go through the process of reading a troublesome csv file.
It may be helpful to have this documentation open for reference: 
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html

  a.
    Try reading question_3.csv into pandas.
    
    You should get an error that looks something like this: "UnicodeDecodeError".
    
    Try to figure out why this error is occuring by copying and pasting the
    error message into google. It may also help to preface your search with
    "pandas".
    
    Hint: this page has a good answer:
    https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
    
    Now try changing one of the .read_csv() options to read the data correctly.
    
  b.
    You now have the correct encoding, but you should notice that your 
    DataFrame still doesn't look quite as expected.
    
    You need to change another setting to get it in a sensible format, see if
    you can work it out.
    
    Hint: the default value for the "sep" argument is comma separator: ','
  c.
    The data should now be in a reasonable shape, however, it looks like the
    the columns don't have names (headers).
    
    Adjust the settings in the .read_csv() call, to give your columns names.
    
    Hint: look at the "header" and "names" arguments.
    
  d.
    The data should now have been read in correctly, but some of the fields 
    needs adjusting before we can analyse it.
    
    First, convert the "turnover" column to float, and multiply it by 1 million.
    
    Hint: get rid of the pound sign before trying to convert the data type. To
    apply string methods to columns, remember you need to use this syntax:
    df[<col_name>].str.<method_name>
    
  e.
    Use a "groupby" to find the mean turnover for each sector.
    
    Is there something unexpected in the output? How would you fix it?
"""









"""
Python exercises set 3 - solutions

FYI: There is rarely a definitive "right" answer - there are usually multiple 
ways to do the same thing. Go for the simpler one if you have to choose.
"""

#==============================================================================
# Question 1
#==============================================================================
# a.
df = pd.read_csv(savepath+'question_1.csv')
df['england'].sum()
df['northern_ireland'].max()
# read_csv didn't automatically set year as the index, so I'll change the 
# read_csv call before finding the median for 2010. Alternatively, you could
# use set_index() on the year column.
df = pd.read_csv(savepath+'question_1.csv', index_col=0)
# so this uses the first row in the file as the index
df.loc[2010].mean()
# another alternative is to filter on the year column and then calculate the mean

# b.
df['wales'] = df['wales'].apply(round)

# Note: you may be tempted to do this:
df['wales'].astype(int)
# but converting a float to an integer always rounds down, so be careful!


# c.
df['average'] = df.mean(axis=1)

# d.
df['england_growth'] = df['england'].pct_change(periods=1)
# fastest growth year:
highest_growth_year = df['england_growth'].idxmax()

# or if you didn't know about this method, you can inspect it manually
# with .sort_values()

#==============================================================================
# Question 2
#==============================================================================
# a.
# When dealing with excel files with multiple sheets, you will need to read
# each sheet separately.
year_1 = pd.read_excel(savepath+'question_2.xlsx', sheetname='year_1')
year_2 = pd.read_excel(savepath+'question_2.xlsx', sheetname='year_2')

# b. 
df = year_1.merge(year_2,
                  how='outer',
                  on='Person_ID',
                  suffixes=['_year_1','_year_2'])

# c.
# There are many possible ways of doing this. 
# This way looks at nulls:
year_2_nulls = df[df['Q1_response_year_2'].isnull()]
ids = list(year_2_nulls['Person_ID'])

# d.
responded_in_both = df.dropna()
# or you do an inner join in part b
responded_in_both_with_a = responded_in_both[ responded_in_both['Q1_response_year_1'] == 'a']
# e.
responded_in_both_with_a.to_csv(savepath+'question_2_answer.csv', index=None)

#==============================================================================
# Question 3
#==============================================================================
# a.
# This error message arises because the default encoding (utf-8) doesn't
# recognise one of the characters in the data. In this case that's actually
# the pound sign (£).
# Changing the "encoding" setting in pd.read_csv would fix this:
# either
df = pd.read_csv(savepath+'question_3.csv', encoding='latin1')
# or
df = pd.read_csv(savepath+'question_3.csv', encoding='cp1252')
# trying either of these is usually a good bet to fixing that particular error.

# b.
# question_2.csv was tab separated, so you need to specify this when you read
# the file, i.e.:
df = pd.read_csv(savepath+'question_3.csv',
                 encoding='latin1',
                 sep='\t')
# Remember tabs are written as '\t' in python
# When you read the data in part a, you can tell that it's tab separated by
# inspecting the first few rows, e.g. with df.head(). You can clearly see
# that the fields are separated by tabs.

# c.
# Here's an example solution, there are many other ways of doing it:
df = pd.read_csv(savepath+'question_3.csv',
                 encoding='latin1',
                 sep='\t',
                 header=None,
                 names=['firm', 'sector', 'turnover'])

# Explanation:
# The default setting is to read the first row as the data header (column names)
# But these are real records, so we need to set header=None. We can also name
# the columns with the "names" option.

# d. Here's two possible ways of getting rid of the £ signs:
df['turnover'] = df['turnover'].str.replace('£', '') # replace £ symbols with empty string
# or you could do this:
df['turnover'] = df['turnover'].str[1:] # remove first character from each string

# Now convert the data type:
df['turnover'] = df['turnover'].astype(float)

# and multiply:
df['turnover'] = df['turnover'] * 10**6

# if you want, you can do this all in one line, although this isn't quite as 
# readable.
df['turnover'] = df['turnover'].str.replace('£','').astype(float) * 10**6

# e.
df.groupby('sector').mean()

# It looks like contsruction has been split into two groups by mistake, as some
# of the entries are capitalised.
# You can fix it using another string method:
df['sector'] = df['sector'].str.lower()
# now the groupby command will give a more sensible result.
# Or if you just wanted to change that particular instance, not the whole
# column, you could use the replace method:
df['sector'] = df['sector'].str.replace('Construction','construction')
