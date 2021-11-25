from tkinter import *
from CreateQuestions import getQuestions
from random import shuffle

class Game(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='black')

        self.controller = controller

        self.numberOfQuestions = 5
        self.currentQuestion = 1

        self.questions = getQuestions(5)
        self.questionText = self.questions[self.currentQuestion - 1]['question']
        
        self.playerPoints = Label(self, text=0, font='Verdana 12 bold', bg='blue', fg='white')
        self.playerPoints.place(x=10, y=20)

        self.opponentPoints = Label(self, text=0, font='Verdana 12 bold', bg='red', fg='white')
        self.opponentPoints.place(x=387, y=20)

        self.timer = Label(self, text=10, font='Verdana 20 bold', bg='black', fg='white')
        self.timer.place(x=195, y=15)

        self.question = Label(self, text=self.questionText, font='Verdana 20 bold', bg='white', fg='black', height=5, width=22, wraplength=450)
        self.question.place(x=0, y=60)

        self.answer1 = Button(self, text='Svar 1', font='Verdana 12 bold', bg='blue', fg='white', command = lambda: self.checkAnswer(self.answer1))
        self.answer1.place(x=120, y=250, height=40, width=190)
        self.answer2 = Button(self, text='Svar 2', font='Verdana 12 bold', bg='blue', fg='white', command = lambda: self.checkAnswer(self.answer2))
        self.answer2.place(x=120, y=310, height=40, width=190)
        self.answer3 = Button(self, text='Svar 3', font='Verdana 12 bold', bg='blue', fg='white', command = lambda: self.checkAnswer(self.answer3))
        self.answer3.place(x=120, y=370, height=40, width=190)
        self.answer4 = Button(self, text='Svar 4', font='Verdana 12 bold', bg='blue', fg='white', command = lambda: self.checkAnswer(self.answer4))
        self.answer4.place(x=120, y=430, height=40, width=190)

        self.assignAnswers()

    def updateGame(self, count):
        if count == -1:
            self.currentQuestion += 1
            self.updateQuestion()
        else:
            self.timer.configure(text=count)
    
    def updateQuestion(self):
        if self.currentQuestion > self.numberOfQuestions:
            self.controller.playerPoints = self.playerPoints['text']
            self.destroy()
            self.controller.show_frame('GameOver')
        else:
            self.question.configure(text=self.questions[self.currentQuestion - 1]['question'])
            self.assignAnswers()
            self.controller.updateGame(self, 10)
    
    def assignAnswers(self):
        buttons = [self.answer1, self.answer2, self.answer3, self.answer4]
        shuffle(buttons)
        correctAnswer = self.questions[self.currentQuestion-1]['rightAnswer']
        buttons[0].configure(text=correctAnswer)
        wrongAnswers = self.questions[self.currentQuestion-1]['wrongAnswers']
        shuffle(wrongAnswers)
        for i in range(1, 4):
            buttons[i].configure(text=wrongAnswers[i])
        for button in buttons:
            button.configure(state=NORMAL)
            button.configure(bg='blue')

    def checkAnswer(self, selectedButton):
        buttons = [self.answer1, self.answer2, self.answer3, self.answer4]
        if selectedButton['text'] == self.questions[self.currentQuestion-1]['rightAnswer']:
            selectedButton.configure(bg='green')
            self.playerPoints.configure(text = self.playerPoints['text'] + self.timer['text'])
        else:
            selectedButton.configure(bg='red')
        for button in buttons:
            button.configure(state=DISABLED)
