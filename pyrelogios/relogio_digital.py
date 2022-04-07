import tkinter
from time import strftime

def timer():
    rel['text'] = strftime('%H:%M:%S')
    rel.after(1000, timer)

rel = tkinter.Label()
rel['font'] = 'Helvetica 120 bold'
rel.pack()
timer()
rel.mainloop()