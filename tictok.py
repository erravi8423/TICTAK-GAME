#=============== My First tic tac toe game=====================
from tkinter import *

def callback(r,c):
    global player

    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].config(text = 'X', fg = 'blue',bg = 'white')
        states[r][c] = 'X'
        player = 'O'

    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].config(text = 'O', fg = 'orange',bg = 'black')
        states[r][c] = 'O'
        player = 'X'
        check_for_winner()

def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2]!=0:
            b[i][0].config(bg = 'gray')
            b[i][1].config(bg = 'gray')
            b[i][2].config(bg = 'gray')
            stop_game = True
    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i]!=0:
            b[0][i].config(bg = 'gray')
            b[1][i].config(bg = 'gray')
            b[2][i].config(bg = 'gray')
            stop_game = True

        if states[0][0] == states[1][1] == states[2][2]!=0:
            b[0][0].config(bg='gray')
            b[1][1].config(bg='gray')
            b[2][2].config(bg='gray')
            stop_game = True
        if states[2][0] == states[1][1] == states[0][2]!=0:
            b[2][0].config(bg='gray')
            b[1][1].config(bg='gray')
            b[0][2].config(bg='gray')
            stop_game = True




root = Tk()
root.title("TIC TAC TOE *RAVI TECHNICAL")

b = [[0,0,0],
     [0,0,0],
     [0,0,0]]
states = [[0,0,0],
          [0,0,0,],
          [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font = ("Arial", 60),width = 4, bg = 'powder blue',
                         command = lambda r = i, c = j: callback(r,c))
        b[i][j].grid(row = i,column = j)
player = 'X'
stop_game = False

mainloop()