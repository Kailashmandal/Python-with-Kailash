from tkinter import *
from tkinter import ttk

root = Tk()
# creating the root top level Tk window object 

button = ttk.Button( root , text="Click Me") 

#just creating the button will not make it visible we have pack it inside a container
button.pack()
# an unique identifier is created and get assosiated with the root window

print(button.config()) # return the all configuration setting related to a object

print( str( button))

lbl = ttk.Label(root, text="Hello, Tkinter!").pack()

print( str(lbl))
root.mainloop()
