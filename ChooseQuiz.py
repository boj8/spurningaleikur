from tkinter import *

class ChooseQuiz(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        Label(self, text='Veldu leik', font='Verdana 20 bold', bg='black', fg='white').place(x=140, y=30)

        Button(self, text='Njálssaga kaflar 1-5', font='Verdana 12 bold', bg='blue', fg='white').place(x=120, y=110, height=40, width=190)
        Button(self, text='Málfræði', font='Verdana 12 bold', bg='blue', fg='white', 
        command = lambda : [self.destroy(), controller.show_frame('FindingOpponent')]).place(x=120, y=170, height=40, width=190)
        Button(self, text='Grettissaga kafli 10', font='Verdana 12 bold', bg='blue', fg='white').place(x=120, y=230, height=40, width=190)
        Button(self, text='Stafsetning', font='Verdana 12 bold', bg='blue', fg='white').place(x=120, y=290, height=40, width=190)
        Button(self, text='Beygingar', font='Verdana 12 bold', bg='blue', fg='white').place(x=120, y=350, height=40, width=190)