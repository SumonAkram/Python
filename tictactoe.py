from tkinter import *
import random

def NewGame():
    global player, button

    player = random.choice(players)

    label.config(text= player + "'s turn", font=("consolas", 30))

    # Clear the text on all buttons
    for row in range(3):
        for col in range(3):
            button[row][col].config(text="")

def next_turn(row, col):
    global player

    if button[row][col]["text"] == "" and not check_winner():
        button[row][col]["text"] = player

        if check_winner():
            label.config(text= player + " wins!")
        elif fillup():
            label.config(text= "Tie!")
        else:
            # Switch player
            player = players[(players.index(player) + 1) % 2]
            label.config(text= player + "'s turn")

def check_winner():
    for row in range(3):
        if button[row][0]["text"] == button[row][1]["text"] == button[row][2]["text"] != "":
            return True

    for col in range(3):
        if button[0][col]["text"] == button[1][col]["text"] == button[2][col]["text"] != "":
            return True

    # Diagonally check1
    if button[0][0]["text"] == button[1][1]["text"] == button[2][2]["text"] != "":
        return True

    # Diagonally check2
    if button[0][2]["text"] == button[1][1]["text"] == button[2][0]["text"] != "":
        return True

    return False

def fillup():
    for row in range(3):
        for col in range(3):
            if button[row][col]["text"] == "":
                return False
    return True

if __name__ == "__main__":
    screen = Tk()
    screen.title("Tic Tac Toe")
    players = ["X", "O"]
    player = random.choice(players)

    button = [[None]*3 for _ in range(3)]

    label = Label(text= player + "'s turn", font=("consolas", 30))
    label.pack(side="top")

    restartButton = Button(text="Restart Game", font=("consolas", 15), command=NewGame)
    restartButton.pack(side="top")

    frame = Frame(screen)
    frame.pack()

    for row in range(3):
        for col in range(3):
            button[row][col] = Button(frame, font=("consolas", 30), width=5, height=2,
                                       command=lambda row=row, col=col: next_turn(row, col))
            button[row][col].grid(row=row, column=col)

    screen.mainloop()
