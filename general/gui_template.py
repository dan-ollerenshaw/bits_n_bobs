# Make a simple GUI.

# Read a csv specified by the user, then save the "head"
# of the csv in the D:/ drive

# Successfully converted this to .exe on linux and windows using pyinstaller :)


from tkinter import Button, Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import pandas as pd


class MyGui():
    """
    """
    def __init__(self, master):
        self.master = master # aka root
        master.title("Welcome to Dan's program!")
        master.geometry('350x200')

        # initialise data to export:
        self.data = pd.DataFrame(None)
        
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
