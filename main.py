from tkinter import *
import json
import os

gui = Tk()

gui.geometry("800x450")

gui.title("PICAT")

def run1():
    os.system('result.py')
def run2():
    os.system('logical.py')
def run3():
    os.system('eng_and_communication.py')

def run4():
    os.system('result.py')
    os.system('logical.py')
    os.system('eng_and_communication.py')

a  = Label(gui,text = "WELCOME TO PICAT",font=("ariel", 16, "bold"),bg="green",fg="white",padx=10,pady=10, width=30).place(x=200 , y=90)

b = Label(gui,text = "Choose your Test",font=("ariel", 16, "bold"),bg="deep sky blue",fg="white",padx=5,pady=7).place(x=310 , y=180)

f = Frame(bg = "grey" , height=140 , width=550).place(x=130,y=250)

b1 = Button(f,text="Personality",font=("ariel", 12, "bold"),bg = "lime green", padx=3,pady=3,command=run1).place(x=170,y=275)

b2 = Button(f,text="Logical Ability",font=("ariel", 12, "bold"),bg = "lime green", padx=3,pady=3,command=run2).place(x=330,y=275)

b3 = Button(f,text="Communication",font=("ariel", 12, "bold"),bg = "lime green", padx=3,pady=3,command=run3).place(x=510,y=275)

b4 = Button(f,text="ALL",font=("ariel", 12, "bold"),bg = "lime green", padx=3,pady=3,command=run4).place(x=360,y=340)

gui.mainloop()

