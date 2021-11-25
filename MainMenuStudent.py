from tkinter import *

class MainMenuStudent(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        Label(self, text='Spurningaleikur', font='Verdana 20 bold', bg='black', fg='white').place(x=100, y=30)

        Button(self, text='Spila ein/n', font='Verdana 12 bold', bg='blue', fg='white').place(x=140, y=110, height=40, width=165)
        Button(self, text='1 vs 1', font='Verdana 12 bold', bg='blue', fg='white', 
        command = lambda : [self.destroy(), controller.show_frame('ChooseSubject')]).place(x=140, y=170, height=40, width=165)
        Button(self, text='Bekkur vs Bekkur', font='Verdana 12 bold', bg='blue', fg='white').place(x=140, y=230, height=40, width=165)
        Button(self, text='Mót', font='Verdana 12 bold', bg='blue', fg='white').place(x=140, y=290, height=40, width=165)