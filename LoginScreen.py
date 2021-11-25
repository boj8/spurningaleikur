from tkinter import *

class LoginScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        Label(self, text='Skráðu þig inn', font='Verdana 20 bold', bg='black', fg='white').place(x=100, y=130)

        Label(self, text='Kennitala', font='Verdana 12 bold', bg='black', fg='white').place(x=80, y=210)
        kennitala = Entry(self, font='Verdana 12 bold')
        kennitala.place(x=200, y=212, height=20, width=130)

        Label(self, text='Lykilorð', font='Verdana 12 bold', bg='black', fg='white').place(x=80, y=260)
        lykilord = Entry(self, font='Verdana 12 bold', show='*')
        lykilord.place(x=200, y=262, height=20, width=130)

        Button(self, text='Skrá inn', font='Verdana 12 bold', bg='blue', fg='white', 
        command = lambda : [self.destroy(), controller.show_frame('MainMenuStudent')]).place(x=150, y=310)