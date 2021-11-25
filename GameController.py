from tkinter import *
from LoginScreen import LoginScreen
from MainMenuStudent import MainMenuStudent
from FindingOpponent import FindingOpponent
from ChooseSubject import ChooseSubject
from ChooseQuiz import ChooseQuiz
from Game import Game
from GameStart import GameStart
from GameOver import GameOver

class GameController(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        self.geometry('412x732')
        self.title('Spurningaleikur')
        self.configure(bg='black')

        self.playerPoints = 0
        self.opponentPoints = 0

        self.frames = {
            'LoginScreen' : LoginScreen,
            'MainMenuStudent' : MainMenuStudent,
            'FindingOpponent' : FindingOpponent,
            'ChooseSubject' : ChooseSubject,
            'ChooseQuiz' : ChooseQuiz,
            'Game' : Game,
            'GameStart' : GameStart,
            'GameOver' : GameOver
        }
            
        self.show_frame('LoginScreen')
        
    def show_frame(self, cont):
        frame = self.frames[cont](self, self)
        frame.pack(fill=BOTH, expand=1)
        if cont == 'FindingOpponent':
            self.after(3000, self.opponentFound, frame)
        elif cont == 'GameStart':
            self.after(1000, self.gameStartCountdown, frame, 2)
        elif cont == 'Game':
            self.after(1000, self.updateGame, frame, 9)
    
    def opponentFound(self, frame):
        frame.opponentFound(self)
    
    def gameStartCountdown(self, frame, count):
        frame.countdown(self, count)
        if count > -1:
            self.after(1000, self.gameStartCountdown, frame, count - 1)
    
    def updateGame(self, frame, count):
        frame.updateGame(count)
        if count > -1:
            self.after(1000, self.updateGame, frame, count - 1)

app = GameController()
app.mainloop()
