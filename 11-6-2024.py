#tkinter 

# python tkiner is the fastest way and easiest way to create gui applications 

# python should be installed in your computer it is mandatory

# at staring we can import everything from tkinter like 

from tkinter import *

# in tkinter everything is a widget 
'''
root=Tk()

w=Label(root,text="aditya!")

w.pack()

root.mainloop()
'''

'''
root=Tk()

w=Label(root,text="aditya!")

w1=Label(root,text="is not married")

w.grid(row=0,column=0)
w1.grid(row=1,column=0)

root.mainloop()

'''

'''
root=Tk()

def qwerty():
    qwe=Label(root,text="hi my self aditya")
    qwe.pack()

mybutton=Button(root,text="click",command=qwerty)
mybutton.pack()

root.mainloop()
'''

'''
from tkinter import *

master = Tk()

Label(master, text='First Name').grid(row=0)

Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
'''

'''
from tkinter import *

master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()
'''

'''
from tkinter import *

root = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()

'''

'''
root=Tk()

root.title("enter your name")

e=Entry(root,width=35,borderwidth=5)

def qwerty():

    name =e.get()
    w=Label(root,text=f"{name}")
    w.pack()


mybutton=Button(root,text="click",command=qwerty)
mybutton.pack()

root.mainloop()
'''

'''
top = Tk()  
  
top.geometry("200x100")  
  
b = Button(top,text = "Simple")  
  
b.pack()  

top.mainloop()

'''

