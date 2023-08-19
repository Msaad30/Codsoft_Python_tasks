from tkinter import *  # or you can : import tkinter 
root = Tk()
root.title("TO DO LIST")
root.minsize(height=500,width=400)
root.config(bg="cyan")

Label(root,text="TO DO LIST", font=("arial",30,"bold"),bg="cyan").pack()

def insert():
    lb.insert(END,x.get())
    e2.delete(0,END)

x = StringVar()
e2 = Entry(root,font=("fantasy",25),width=16,textvariable = x)
e2.place(x=10,y=70)

lb = Listbox(root,height=8,font=("fantasy",20),width=25)
lb.place(x=10,y=130)

b2 = Button(root,text="ADD",font=("arial",10,"bold"),height=2,width=8,bg="green",fg="white",command=insert)
b2.place(x=310,y=69)

def remove():
    lb.delete(ANCHOR)

b3 = Button(root,text="DELETE",font=("bold",10),height=2,width=13,bg="red",fg="white",command=remove)
b3.place(x=130,y=420)

root.mainloop()    # use to set windows active always set in last 