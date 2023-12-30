import tkinter
from tkinter import *

window=Tk()
window.title("simple calculator")
window.geometry("380x500+10+20")
window.resizable(False,False)
window.configure(background="black")

eqn=""
def show(value):
    global eqn
    eqn+=value
    label_result.config(text=eqn)

def clear():
    global eqn
    eqn=""
    label_result.config(text=eqn)

def calculate():
    global eqn
    result=""
    if eqn !="":
        try:
            result=eval(eqn)
        except:
            result="error"
            eqn=""
    label_result.config(text=result)
    
label_result=Label(window,width=15,height=2,text="",font=("arial",30))
label_result.pack()
Button(window,text="C",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="red",command=lambda: clear()).place(x=10,y=100)
Button(window,text="(",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="grey",command=lambda: show("(")).place(x=100,y=100)
Button(window,text=")",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="grey",command=lambda: show(")")).place(x=190,y=100)
Button(window,text="*",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="grey",command=lambda: show("*")).place(x=280,y=100)


Button(window,text="7",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("7")).place(x=10,y=180)
Button(window,text="8",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("8")).place(x=100,y=180)
Button(window,text="9",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("9")).place(x=190,y=180)
Button(window,text="-",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="grey",command=lambda: show("-")).place(x=280,y=180)

Button(window,text="4",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("4")).place(x=10,y=260)
Button(window,text="5",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("5")).place(x=100,y=260)
Button(window,text="6",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("6")).place(x=190,y=260)
Button(window,text="+",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="grey",command=lambda: show("+")).place(x=280,y=260)

Button(window,text="1",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("1")).place(x=10,y=340)
Button(window,text="2",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("2")).place(x=100,y=340)
Button(window,text="3",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("3")).place(x=190,y=340)

Button(window,text="0",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="orange",command=lambda: show("0")).place(x=10,y=420)
Button(window,text=".",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="grey",command=lambda: show(".")).place(x=100,y=420)


Button(window,text="/",width=4,height=1,font=("arial",20,"bold"),bd=1,foreground="white",background="grey",command=lambda: show("/")).place(x=190,y=420)
Button(window,text="=",width=4,height=3,font=("arial",20,"bold"),bd=1,foreground="white",background="sky blue",command=lambda: calculate()).place(x=280,y=340)

window.mainloop()


    
