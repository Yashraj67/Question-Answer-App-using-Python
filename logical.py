import matplotlib.pyplot as plt
from tkinter import *

from tkinter import messagebox as mb

import json

class Quiz:

    def __init__(self):

        self.q_no = 0

        self.display_title()
        self.display_question()

        self.opt_selected = IntVar()

        self.opts = self.radio_buttons()

        self.display_options()

        self.buttons()

        self.data_size = len(question)

        self.correct = 0

    def display_result(self):

        wrong_count = self.data_size - self.correct
        return self.correct , wrong_count

    def check_ans(self, q_no):

        if self.opt_selected.get() == answer[q_no]:

            return True

    def next_btn(self):

        if self.check_ans(self.q_no):

            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            labels = 'Correct', 'Incorrect'
            sizes = [self.correct, 10-self.correct]

            colors = ("orange", "cyan")
            fig1, ax1 = plt.subplots()
            explode = (0, 0.1)
            ax1.pie(sizes, colors=colors, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)

            plt.show()
            gui.destroy()
        else:

            self.display_question()
            self.display_options()

    def buttons(self):

        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        next_button.place(x=350, y=380)


        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))


        quit_button.place(x=700, y=43)


    def display_options(self):
        val = 0


        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1


    def display_question(self):

        q_no = Label(gui, text=question[self.q_no], width=60, height=3,
                     font=('ariel', 16, 'bold'), anchor="w")

        q_no.place(x=80, y=80)

    def display_title(self):

        title = Label(gui, text="Logical Test",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        title.place(x=0, y=2)

    def radio_buttons(self):

        q_list = []

        y_pos = 150

        while len(q_list) < 4:

            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            q_list.append(radio_btn)

            radio_btn.place(x=100, y=y_pos)

            y_pos += 40

        return q_list


gui = Tk()

gui.geometry("800x450")

gui.title("PICAT")

with open('logical_data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answers'])

quiz = Quiz()

gui.mainloop()
