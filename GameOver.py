from tkinter import *

class GameOver(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        Label(self, text='Þú vannst!', font='Verdana 20 bold', bg='black', fg='white').place(x=130, y=30)
        Label(self, text=controller.playerPoints, font='Verdana 18 bold', bg='blue', fg='white').place(x=150, y=100)
        Label(self, text=controller.opponentPoints, font='Verdana 18 bold', bg='red', fg='white').place(x=250, y=100)

        Button(self, text='Spila aftur', font='Verdana 12 bold', bg='blue', fg='white', 
        command = lambda : [self.destroy(), controller.show_frame('GameStart')]).place(x=130, y=170, height=40, width=165)
        Button(self, text='Nýr mótherji', font='Verdana 12 bold', bg='blue', fg='white', 
        command = lambda : [self.destroy(), controller.show_frame('FindingOpponent')]).place(x=130, y=230, height=40, width=165)
        Button(self, text='Skoða úrslit', font='Verdana 12 bold', bg='blue', fg='white').place(x=130, y=290, height=40, width=165)