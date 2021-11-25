from tkinter import *
from time import sleep

class FindingOpponent(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        Label(self, text='Vinsamlegast bíðið...', font='Verdana 20 bold', bg='black', fg='white').place(x=60, y=80)
        Label(self, text='Finn mótherja', font='Verdana 20 bold', bg='black', fg='white').place(x=100, y=140)

        img = PhotoImage(file='loading.gif')
        mynd = Label(self, image=img, bg='black')
        mynd.image = img
        mynd.place(x=50, y=250)

    def opponentFound(self, controller):
        self.destroy()
        controller.show_frame('GameStart')