from tkinter import *

class ChooseSubject(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        Label(self, text='Veldu fag', font='Verdana 20 bold', bg='black', fg='white').place(x=150, y=30)

        Button(self, text='Saga', font='Verdana 12 bold', bg='blue', fg='white').place(x=140, y=110, height=40, width=165)
        Button(self, text='Íslenska', font='Verdana 12 bold', bg='blue', fg='white', 
        command = lambda : [self.destroy(), controller.show_frame('ChooseQuiz')]).place(x=140, y=170, height=40, width=165)
        Button(self, text='Stærðfræði', font='Verdana 12 bold', bg='blue', fg='white').place(x=140, y=230, height=40, width=165)
        Button(self, text='Danska', font='Verdana 12 bold', bg='blue', fg='white').place(x=140, y=290, height=40, width=165)