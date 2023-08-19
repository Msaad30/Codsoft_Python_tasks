from tkinter import *
root = Tk()
root.minsize(width=400,height=500)
#root.maxsize(width=400,height=500)
root.config(bg="black")

cal = Label(root,text="Calculator",font=("arial",28),width=15,height=2,fg="gold",bg="black")
cal.pack()

l = Label(root,font=("bold",20),width=22,height=2,borderwidth=1,relief="solid",bg="silver")
l.place(x=18,y=80)

    
equation = ""

def clear():
    global equation
    equation = ""
    l.config(text=equation,bg="silver",fg="black")

def show(val):
    global equation
    equation += val
    l.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
    l.config(text=result,fg="black",bg="silver")

    

Button(root,text="C",bg="blue",fg="white",font=("bold",15),height=2,width=7,command=lambda:clear()).place(x=20,y=160)
Button(root,text="/",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("/")).place(x=108,y=160)
Button(root,text="*",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("*")).place(x=196,y=160)
Button(root,text="-",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("-")).place(x=284,y=160)

Button(root,text="7",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("7")).place(x=20,y=224)
Button(root,text="8",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("8")).place(x=108,y=224)
Button(root,text="9",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("9")).place(x=196,y=224)
Button(root,text="+",bg="white",font=("bold",14),height=5,width=7,command=lambda:show("+")).place(x=284,y=224)

Button(root,text="4",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("4")).place(x=20,y=287)
Button(root,text="5",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("5")).place(x=108,y=287)
Button(root,text="6",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("6")).place(x=196,y=287)

Button(root,text="1",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("1")).place(x=20,y=350)
Button(root,text="2",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("2")).place(x=108,y=350)
Button(root,text="3",bg="white",font=("bold",15),height=2,width=7,command=lambda:show("3")).place(x=196,y=350)
Button(root,text="=",bg="orange",font=("bold",14),height=5,width=7,command=lambda:calculate()).place(x=284,y=350)

Button(root,text="0",bg="white",font=("bold",15),height=2,width=15,command=lambda:show("0")).place(x=20,y=413)
Button(root,text="del .",bg="white",font=("bold",15),height=2,width=7,command=lambda:show(".")).place(x=196,y=413)



root.mainloop()
