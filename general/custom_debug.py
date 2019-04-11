"""
Super hacky, but could be useful for debugging without a real debugger?

Instructions:
- Run the code below (lines 15-to-25. WARNING: this will add the "exit_word" 
  variable to your namespace)    
- Find some code you want to debug
- Enter this line at the point you want to start debugging:
>>> code.interact(local={**globals(), **locals()})
- Run code
- An interactive console will pop up, where you can view the state of variables
  at the point you entered. So you can see local vars, for example :)
"""

import code


def raise_sys_exit():
    raise SystemExit


# for some reason exit() doesn't work inside the code.InteractiveConsole
# so choose an exit word and use that instead
exit_word = 'let_me_out'
globals()[exit_word] = raise_sys_exit
# *disclaimer* modifying the globals dict is usally a bad idea...
    

# example:
def my_func():
    a = 1
    b = 2
    code.interact(local={**globals(), **locals()})
    c = 3
    print(a + b + c)
    
# run my_func() and try viewing the variables a, b and c.
# to exit the console, just call your exit word, e.g. let_me_out()

# unfortunately it seems that this doesn't work if input() built-in is not 
# supported