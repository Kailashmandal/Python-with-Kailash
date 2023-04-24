
# label object different property
from tkinter import *
from tkinter import ttk

root= Tk()
eren = PhotoImage(file= "D:\logo.gif")

sampletxt="It is subjective to say which anime is the as it depends on personal taste and preferences. Some popular and critically acclaimed anime that have stood the test of time include"

lbl = ttk.Label(root, text=sampletxt,wraplength=150,justify=LEFT, foreground="grey",background="yellow"
, font=('Courier',18,'bold'))



lbl.config(image=eren,compound='left') # compound cammand will show both at a time use 'left' or 'right' command accordingly
lbl.pack()
# wrapping text inside lbl 150 in pixels

root.mainloop()
