from tkinter import *

'''

root=Tk()

def qwerty(event):
    print(F"you clicked on the button at {event.x} and {event.y}")

root.title("events")


widet=Button(root,text="click here")
widet.pack()

widet.bind("<Button-1>",qwerty)
widet.bind("<Double-1>",quit)

root.mainloop()

'''

'''
root=Tk()

root.title("events and keyboard")

root.geometry("400x400")

def qwerty(event):
    label=Label(root,text="hii how are you ")
    label.pack()

but=Button(root,text="click here")
but.bind("<Button-3>",qwerty)
but.pack(pady=20)

root.mainloop()

'''

root=Tk()

root.title("events and keyboard")

root.geometry("400x400")

def qwerty(event):
    label=Label(root,text="hii how are you ")
    label.pack()

but=Button(root,text="click here")
but.bind("<Return>",qwerty)
but.pack(pady=20)

root.mainloop()