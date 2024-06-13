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
'''
root=Tk()

root.title("events and keyboard")

root.geometry("400x400")

def qwerty(event):
    label=Label(root,text="hii how are you ")
    label.pack()

but=Button(root,text="click here")
but.bind("<Enter>",qwerty)
but.pack(pady=20)

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
but.bind("<Return>",qwerty)
but.pack(pady=20)

root.mainloop()
'''


'''
root = Tk()

C = Canvas(root, bg="yellow",
		height=250, width=300)

line = C.create_line(108, 120,
					320, 40,
					fill="green")

arc = C.create_arc(180, 150, 80,
				210, start=0,
				extent=220,
				fill="red")

oval = C.create_oval(80, 30, 140,
					150,
					fill="blue")

C.pack()
mainloop()
'''

'''
root = Tk()
canvas = Canvas(root, width=400, height=300, bg="blue")
canvas.pack()
root.mainloop()
'''

root=Tk()
root.title("checkbox")
root.geometry("400x400")

def show():
    w=Label(root,text=a.get()).pack() 

a=IntVar()
c=Checkbutton(root,text="male",variable=a)
c.pack()

but=Button(root,text="show",command=show).pack()

root.mainloop()