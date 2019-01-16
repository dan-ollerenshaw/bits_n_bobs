# Make a simple GUI that transforms some data.

#TODO: find a program to successfully convert this to exe
#(no luck with pyinstaller)

from tkinter import Button, Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import pandas as pd


class MyGui():
    """
    """
    def __init__(self, master): # what is master?
        self.master = master
        master.title('test') # not doing anything
                
        # initialise data to export:
        self.data = pd.DataFrame(None)
        print(self.data)
        
        self.loader = Button(master,
                             text='Load a dataset',
                             command=self.launch)
        self.loader.grid(row=1, padx=5)
        
        self.func = Button(master,
                           text='Apply the function',
                           command=self.take_head)
        self.func.grid(row=2, padx=5)
        
        self.saver = Button(master,
                            text='Save the data',
                            command=self.save)
        self.saver.grid(row=3,padx=5)
        
        self.quitter = Button(master,
                              text='Quit program',
                              command=master.quit)
        self.quitter.grid(row=4)
    
    
    def take_head(self):
        """ Dummy function
        """
        self.data = self.data.head()

    
    def launch(self):
        file = askopenfilename(defaultextension='.csv',
                               initialdir='D:/')
        self.data = pd.read_csv(file)
    
    
    def save(self):
        outpath = asksaveasfilename(defaultextension='.csv')
        self.data.to_csv(outpath)
        print('Saved data!')

def main():
    root = Tk()
    MyGui(root)
    root.mainloop()
    root.destroy()


if __name__ == '__main__':
    main()
