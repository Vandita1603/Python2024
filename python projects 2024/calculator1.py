import tkinter
from tkinter import*

root=Tk()
root.title("Simple Calculator")
root.geometry('570x600+400+50') #(width , height , horizontal appearance position , vertical appearance position)
root.configure(bg="black")

equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation= ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation=""
    label_result.config(text=result)
base_frame=Frame(root,bd=4,relief=RIDGE,bg='#1d3849')
base_frame.place(x=0,y=0,width=570,height=600)

cal_frame=Frame(base_frame,bd=4,relief=RIDGE,bg='#1d3849')
cal_frame.place(x=0,y=100,width=563,height=490)

label_frame=Frame(base_frame,bd=4,relief=RIDGE,bg="#a2bbcf")
label_frame.place(x=0,y=0,width=560,height=100)

label_result = Label(label_frame,width=25,height=2,text="",font=("arial",30),bg="#a2bbcf",bd=2) 
label_result.pack()

Button(cal_frame,text="C",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#6b1313",command= lambda : clear()).place(x=2,y=5)
Button(cal_frame,text="%",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("%")).place(x=281,y=5)
Button(cal_frame,text="/",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("/")).place(x=141,y=5)
Button(cal_frame,text="*",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("*")).place(x=421,y=5)

Button(cal_frame,text="7",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("7")).place(x=2,y=98)
Button(cal_frame,text="8",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("8")).place(x=141,y=98)
Button(cal_frame,text="9",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("9")).place(x=281,y=98)
Button(cal_frame,text="-",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("-")).place(x=421,y=98)

Button(cal_frame,text="4",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("4")).place(x=2,y=198)
Button(cal_frame,text="5",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("5")).place(x=141,y=198)
Button(cal_frame,text="6",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("6")).place(x=281,y=198)
Button(cal_frame,text="+",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("+")).place(x=421,y=198)

Button(cal_frame,text="1",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("1")).place(x=2,y=298)
Button(cal_frame,text="2",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("2")).place(x=141,y=298)
Button(cal_frame,text="3",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("3")).place(x=281,y=298)
Button(cal_frame,text="=",width=5,height=3,font=("arial",30,"bold"),bd=3,fg="white", bg="#8c480f",command = lambda :calculate()).place(x=421,y=298)

Button(cal_frame,text="0",width=11,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show("0")).place(x=2,y=396)
Button(cal_frame,text=".",width=5,height=1,font=("arial",30,"bold"),bd=3,fg="white", bg="#142f44",command = lambda :show(".")).place(x=281,y=396)


root.mainloop()
