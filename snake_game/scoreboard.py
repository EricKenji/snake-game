from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.write(f'Score: {self.score}', font=('Courier', 14, 'italic'), align='center')
        self.hideturtle()

    def point_scored(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', font=('Courier', 14, 'italic'), align='center')

    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write('GAME OVER', font=('Courier', 14, 'italic'), align='center')
