#importing needed pakages
from tkinter import *
from tkinter import messagebox
import random 

#creating frame
root = Tk()
root.minsize(width=700,height=500)
root.title("Password Generator")
root.config(bg="white")

Question = [
    "Q. Who is the father of C language?",
    "Q. Which of the following is not a valid C variable name?",
    "Q. When was C programming developed?",
    "Q. What was C programming adapted from?",
    "Q. What are float variables?",
    "Q. Which of the following is not related to c programming?",
]
answers_choice = [
    ["a) Steve Jobs","b) James Gosling","c) Dennis Ritchie","d) Rasmus Lerdorf"],
    ["a) int number;","b) float rate;","c) int variable_count;","d) int $main;"],
    ["a) The 1950s","b) The 1960s","c) The 1980s","d) The 1970s"],
    ["a) C++","b) Combined programming language","c) python","d) All of the above"],
    ["a) Integer value","b) unknown value","c) Decimal value","d) All of the above" ],
    ["a) conio.h","b) getch()","c) console.log","d) All of the above"],
]

answer = [2,3,3,1,2,2]

user_ans = []

pass1 = PhotoImage(file="img/pass1.png")
fail1 = PhotoImage(file="img/fail1.png")

def show_result():
    global score
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    
    show = "Your Score {} is out of 30"    
    lblQuestion.config(text=show.format(score))

    if score >= 15:    
        photo1 = Label(root,image=pass1,height=300,width=400,bg="white")
        photo1.place(x=180,y=140)
    else:
        photo2 = Label(root,image=fail1,height=300,width=400,bg="white")
        photo2.place(x=180,y=140)


    

def cal():
    global answer, answers_choice, indexes, score
    x = 0
    score = 0
    for i in indexes:
        
        if user_ans[i] == answer[i]:
            score = score + 5
        x += 1

    if user_ans[i] <= 6:
        show_result()



indexes = []

x = 0

def gen():
    global x, indexes
    while(len(indexes) < 6):
        indexes.append(x)
        x = x + 1
ques = 1

def selected():
    global radio_var, user_ans, ques
    global lblQuestion,r1,r2,r3,r4

    val = radio_var.get()
    user_ans.append(val)
    radio_var.set(-1)
    gen()  
    if ques < 6:
        lblQuestion['text'] = Question[indexes[ques]]
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
    else:
        cal()

    ques += 1

def start_quiz():
    gen()
    
    global lblQuestion,r1,r2,r3,r4

    lblQuestion = Label(root,text=Question[indexes[0]],
    font=("arial",25),width=30,height=5,bg="white",fg="black",justify="center",wraplength=500)
    lblQuestion.pack()

    global radio_var
    radio_var = IntVar()
    radio_var.set(-1)

    r1 = Radiobutton(root,text=answers_choice[indexes[0]][0],font=("arial",20),justify="center",command=selected,wraplength=300,value=0,variable=radio_var,bg="white",fg="black")
    r1.place(x=60,y=200)

    r2 = Radiobutton(root,text=answers_choice[indexes[0]][1],font=("arial",20),justify="center",command=selected,wraplength=300,value=1,variable=radio_var,bg="white",fg="black")
    r2.place(x=350,y=200)

    r3 = Radiobutton(root,text=answers_choice[indexes[0]][2],font=("arial",20),justify="center",command=selected,wraplength=300,value=2,variable=radio_var,bg="white",fg="black")
    r3.place(x=60,y=300)


    r4 = Radiobutton(root,text=answers_choice[indexes[0]][3],font=("arial",20),justify="center",command=selected,wraplength=300,value=3,variable=radio_var,bg="white",fg="black")
    r4.place(x=350,y=300)


pic = PhotoImage(file="img/quiz1.png")
photo = Label(root,image=pic,height=300,width=300,bg="white")
photo.place(x=190,y=20)

head1 = Label(root,text="Test your Knowledge",font=("arial",30,"bold"),width=25,height=2,bg="white",fg="black")
head1.place(x=30,y=300)

head = Label(root,text="C Programming",font=("arial",20,"bold"),width=25,height=2,bg="white",fg="black")
head.place(x=110,y=365)


def start():
    head1.destroy()
    head.destroy()
    photo.destroy()
    start_quiz()
    root.config(bg="white")
    start_btn.destroy()

start_btn = Button(root,text="Start Quiz",bg="green",fg="white",font=("arial",10,"bold"),height=1,width=19,command=start)
start_btn.place(x=250,y=450)


root.mainloop()

