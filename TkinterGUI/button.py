from tkinter import *
from tkinter import ttk
root= Tk()

def callback():
    print("clicked!")

btn = ttk.Button(root, text="Click Me")
btn.config(command= callback) # setting the function that will run after clicking the button

# btn.invoke() # to invoke the btn command anywhere

# we can set the button state according to the condition by using the state property of buttons "normal", "active", "disabled"

btn.state(['active'])

btn.pack()
root.mainloop()  