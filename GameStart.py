from tkinter import *

class GameStart(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        Label(self, text='Málfræði', font='Verdana 20 bold', bg='black', fg='white').place(x=140, y=30)

        Label(self, text='Þú', font='Verdana 25 bold', bg='blue', fg='white').place(x=110, y=170)
        Label(self, text='VS', font='Verdana 20 bold', bg='black', fg='white').place(x=190, y=170)
        Label(self, text='Jón', font='Verdana 25 bold', bg='red', fg='white').place(x=270, y=170)

        self.timer = Label(self, text=3, font='Verdana 30 bold', bg='black', fg='white')
        self.timer.place(x=205, y=350)

    
    def countdown(self, controller, count):
        if count == -1:
            self.destroy()
            controller.show_frame('Game')
        else:
            self.timer.configure(text=count)