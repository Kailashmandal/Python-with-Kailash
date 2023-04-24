# pack geometry widget


# Grid geometry widget
# 1. Defines the row/column of two-demensional table in master
# 2. example: widget.grid(row =0, column =1 )


# Place Geometry Manager
# 1. Define relative or absolute x/y co-ordinate in master
# 2. Ex: widget.place(x= 200, y=150)

# Tip: use a single Geometry manager under a single master 
# ex:always use grid() for all object under the root window object.

# Event hadling is used to catch the keyboard/mouse user input
# Event loop handles the user event in sychronous way

# command property for button that run after clicking the button
# bind property and enter property for labels

from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self,master):
        
        self.label = ttk.Label( master, text="Hello, There!")
        self.label.grid(row=0,column=0,columnspan=2)

        ttk.Button(master,text="Texas",
        command=self.texas_hello).grid(row=1,column=0)

        ttk.Button(master=master , text="India",
        command=self.India_hello).grid(row=1,column=1)

    def texas_hello(self):
        self.label.config(text="Hello, Texas!")
    
    def India_hello(self):
        self.label.config(text="Hello, India!")


def main():

    root= Tk()
    app = HelloApp( root)
    root.mainloop()

if __name__=="__main__":
    main()