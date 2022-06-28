from tkinter import *
import json
import os
win1 = Tk()

win1.geometry("1000x450")

win1.title("PICAT")


with open('personality_data.json') as f:
    personality_data = json.load(f)

question = (personality_data['question'])
options = (personality_data['options'])
data_size = len(question)
fp = []
fp2=[]

class Personality:
    def __init__(self):
        self.data_size = len(question)
        self.q_no = 0
        self.opt_selected = IntVar()
        self.val = [2,1,0,-1,-2]
        self.score = 0
        self.score1 = 0
        self.s1 = []
        self.s2 = []
        self.no = 0
        self.display_title()
        self.questions()
        self.options()
        self.buttons()
    def questions(self):
        q_no = Label(win1, text=question[self.q_no], width=60,height = 3,
                     font=('ariel', 16, 'bold'),anchor="w")

        q_no.place(x=80, y=80)

    def options(self):
        y_pos = 150
        for i in range(0, 5):
            btn = Radiobutton(win1, text=f" {options[i]}", variable=self.opt_selected,
                                    value=self.val[i], font=("ariel", 14))
            btn.place(x=100, y=y_pos)
            y_pos += 40

    def buttons(self):
        next_button = Button(win1, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        next_button.place(x=350, y=380)

        quit_button = Button(win1, text="Quit", command=win1.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        quit_button.place(x=870, y=50)

    def check_ans(self):
        self.no += 1
        if self.no==6 or self.no==11 or self.no==16 or self.no==21:
            self.s1.append(self.score)
            self.s2.append(self.score1)
            self.score = 0
            self.score1 = 0

        if self.opt_selected.get() == 2:
            self.score += 20
        if self.opt_selected.get() == 1:
            self.score += 10
        if self.opt_selected.get() == 0:
            self.score += 10
            self.score1 += 10
        if self.opt_selected.get() == -1:
            self.score1 += 10
        if self.opt_selected.get() == -2:
            self.score1 += 20


    def next_btn(self):

        self.check_ans()
        self.q_no+=1
        if self.q_no == self.data_size:
            self.abc = Label(win1,text=f"Score = {self.s1}",bg="yellow",font=('ariel', 16, 'bold'), anchor='w').place(x=100,y=100)
            self.check_ans()

            win1.destroy()
        else:
            self.questions()
            self.options()



    def display_title(self):
            title = Label(win1, text="Personality Test",
                          width=60, bg="green", fg="white", font=("ariel", 20, "bold"))

            title.place(x=0, y=2)

    def run2(self):
        os.system('result.py')
    def get_values(self):
        return self.s1,self.s2

sas = Personality()
fp,fp2 = sas.get_values()
win1.mainloop()
