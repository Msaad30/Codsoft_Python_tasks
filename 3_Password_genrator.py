#importing needed pakages
from tkinter import *
from tkinter import messagebox
import random 

#creating frame
root = Tk()
root.minsize(width=800,height=600)
root.title("Password Generator")
root.config(bg="lightblue")

head = Label(root,text="Password Genrator",font=("arial",40,"bold"),width=15,height=2,fg="black",bg="lightblue")
head.pack()

#Name lable and text field
name = Label(root,text="Name : ",font=("arial",25,"bold"),width=15,height=2,fg="black",bg="lightblue")
name.place(x=5,y=100)

n = StringVar()
e_name = Entry(root,font=("arial",25),width=25,textvariable=n)
e_name.place(x=250,y=120)

#Eamil lable and text field
Email = Label(root,text="Email : ",font=("arial",25,"bold"),width=15,height=2,fg="black",bg="lightblue")
Email.place(x=5,y=170)

e = StringVar()
e_mail = Entry(root,font=("arial",25),width=25,textvariable=e)
e_mail.place(x=250,y=190)

#mobile number lable and text field
Mob = Label(root,text="Mobile no: ",font=("arial",25,"bold"),width=15,height=2,fg="black",bg="lightblue")
Mob.place(x=5,y=240)

m = StringVar()
e_mob = Entry(root,font=("arial",25),width=25,textvariable=m)
e_mob.place(x=250,y=260)

#length lable and text field
len = Label(root,text="Set length : ",font=("arial",25,"bold"),width=15,height=2,fg="black",bg="lightblue")
len.place(x=5,y=310)

l = IntVar()
e_len = Entry(root,font=("arial",25),width=5,textvariable=l)
e_len.place(x=250,y=330)

#button for generating password

def genarate(): #creating fun for generation password
    Name = n.get()
    Email = e.get()
    Mob = m.get()
    Length = l.get()

    all = Name + Email + Mob
    
    Password = "".join(random.sample(all,Length))
    password.config(text = Password)

generate = Button(root,text="Generate",bg="brown",fg="white",font=("arial",20,"bold"),height=1,width=19,command=genarate)
generate.place(x=370,y=325)

#label for showing password
password = Label(root,text="password",font=("arial",20,"bold"),width=46,height=2,fg="gold",bg="black")
password.place(x=5,y=400)

#button for regenerating password
re_gen = Button(root,text="Re - Generate",bg="Green",fg="white",font=("arial",20,"bold"),height=1,width=14,command=genarate)
re_gen.place(x=5,y=490)

#creating for coping text
def copy():
    messagebox.showinfo("Successful","Message Copied")

copy = Button(root,text="Copy",bg="red",fg="white",font=("arial",20,"bold"),height=1,
width=14,command=copy)
copy.place(x=270,y=490)

#creating button for clearing all field

def clear():
    e_name.delete(0,END)
    e_mail.delete(0,END)
    e_mob.delete(0,END)
    e_len.delete(0,END)
    password.config(text="")
    
clear = Button(root,text="Clear",bg="blue",fg="white",font=("arial",20,"bold"),height=1,width=14,command=clear)
clear.place(x=540,y=490)

root.mainloop()

