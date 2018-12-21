"""
Python exercises set 2.
These exercises go with "python_notes_part1.py".

Topic: "Pure" Python


################################# Question 1 #################################
  a. 
    Write a function that asks the user how old they are.
    Use the input to decide (and print) whether that person is eligible to
    vote.
    HINT: use int() to convert response to a number
  b.
    Extend the function to estimate how many years they must live with
    the outcome of their vote (assuming average life expectancy is constant
    at 85). Print this information.

################################# Question 2 #################################
  a. 
    Write a function which asks for an input. If this input is not the letter
    'L' then it will ask again until it receives the correct input and then it
    prints out 'arigatou gozaimasu' before quitting.
    HINT: use a while loop.

    bonus: allow the function to accept upper or lower case without using
           an 'or' clause.

################################# Question 3 #################################
  a. 
    For the entire 18th century, print to the screen all the years which are
    leap years.
    18th century leap years: starts in 1700, 1704, 1708, etc.

################################# Question 4 #################################
  For this question we'll use the os module. Import it like so:
  import os

  a.
    Use the os module to create a new folder somewhere on your computer. Call
    it "python_test".
    The function you should use is "os.mkdir".
    
    Once it's created, change directory to your new folder using "os.chdir".
  b.
    Run the following code block, which will create some dummy files in your
    new folder (assuming you changed directory to it! you can verify with
    "os.getcwd()"):
    
    # START OF CODE BLOCK
    import datetime as dt
    import json
    import getpass
    import platform
    
    user = getpass.getuser()
    for file in range(5):
        with open('file_{}.txt'.format(file), 'w') as f:
            f.write('Hello {}! this file was written at {}'.format(user,
                                                                   dt.datetime.now()))
    data = {user:platform.system()}
    with open('dummy_info.json', 'w') as f:
        json.dump(data, f)
    # END OF CODE BLOCK  

    Using the os.listdir() function, store the names of all the files in your
    directory have the extension ".txt".
    Hint: there is a useful string method called .endswith()
    
  c. Using the os.rename() function, rename all the text files to something else!
     Try to do this in a loop rather than one at a time.
     
     Hint 1: the fiddly bit here is that os.rename requires you to specify the 
     filepath as well as the filename...
     Hint 2: when typing out filepaths in python, make sure to use forward 
     slashes (/), not backslashes (\). Annoyingly, if you copy and paste from 
     the windows explorer, you will get backslashes.
"""




"""
Python exercises set 2 - solutions

FYI: There is rarely a definitive "right" answer - there are usually multiple 
ways to do the same thing. Go for the simpler one if you have to choose.
"""

#==============================================================================
# Question 1
#==============================================================================
# a.
def age_asker():
    age = input('How old are you? ')
    age = int(age) # convert the response to a number
    if age >= 18:
        print('You are old enough to vote!')
    else:
        print('You are too young to vote!')
        
# b.       
def age_asker2(life_expectancy=85):
    age = input('How old are you? ')
    age = int(age) # convert the response to a number
    if age >= 18:
        print('You are old enough to vote!')
    else:
        print('You are too young to vote!')
    # print how long you must live with your vote
    years_to_live_with_vote = life_expectancy - age
    print('You must live with your vote for {} years!'.format(years_to_live_with_vote))
    
#==============================================================================
# Question 2
#==============================================================================
# a.
def letter_asker():
    letter = 'not l' # doesn't matter what it's initialised to, so long as it's not l!
    while letter.lower() != 'l':
        letter = input('Enter a letter: ')
    print('arigatou gozaimasu')

#==============================================================================
# Question 3
#==============================================================================
# a.
for year in range(1700,1800, 4):
    print('{} is a leap year.'.format(year))
    
#==============================================================================
# Question 4
#==============================================================================
# a.
# I'll start this example assuming you're starting in the D:/ drive, but it
# doesn't matter where you start
import os
os.mkdir('D:/python_test')
# note that if you try to create a folder that already exists, you'll
# get an error (mkdir won't overwrite an existing folder)
os.chdir('D:/python_test')


# b.

import datetime as dt
import json
import getpass
import platform

user = getpass.getuser()
for file in range(5):
    with open('file_{}.txt'.format(file), 'w') as f:
        f.write('Hello {}! this file was written at {}'.format(user,
                                                               dt.datetime.now()))
data = {user:platform.system()}
with open('dummy_info.json', 'w') as f:
    json.dump(data, f)

# list files in directory that end in .txt:
txt_files = [f for f in os.listdir() if f.endswith('txt')]

# N.B. If you're curious about what this code block does...
# (1) import a bunch of modules
# (2) obtain your username
# (3) open 5 text files, recording your username and the time the file was written
# (4) write a JavaScript Object Notation file containing your username and the 
# type of operating system you're using (presumably windows)
# JSON is another way of storing data, much like a csv

# c.
directory = 'D:/python_test/'
for file in txt_files:
    new_name = file.replace('file','renamed') # you can rename however you like
    os.rename(directory + file, directory + new_name)
    
# You may also see people using "os.path.join" for similar purposes, which
# is more robust (in the sense that it works for any operating system)
