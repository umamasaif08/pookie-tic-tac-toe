from tkinter import *
import random

def next_turn(row, coloum):
    global player

    if buttons[row][coloum]["text"] == "" and check_winner() is False:
        buttons[row][coloum]["text"] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn 💕"))
        elif check_winner() is True:
            label.config(text=(player + " wins! ✨🎉"))
        elif check_winner() == "Tie":
            label.config(text=" It’s a tie cutie! 💖")

def check_winner():
    # rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            for col in range(3):
                buttons[row][col].config(bg="#CCFFCC")  # mint green highlight
            return True

    # cols
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            for row in range(3):
                buttons[row][col].config(bg="#CCFFCC")
            return True

    # diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        for i in range(3):
            buttons[i][i].config(bg="#CCFFCC")
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="#CCFFCC")
        buttons[1][1].config(bg="#CCFFCC")
        buttons[2][0].config(bg="#CCFFCC")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="#FFF5CC")  # soft yellow for tie
        return "Tie"
    else:
        return False

def empty_spaces():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn 💕")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#EBD6FF")

# window setup
window = Tk()
window.title("Pookie  Tic Tac Toe 🎀🧸")
window.configure(bg="#FFD6E8")  # pastel pink bg

players = ["🧸", "🎀"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn 💕", font=('Comic Sans MS', 28), fg="deeppink", bg="#FFD6E8")
label.pack(side="top")

reset_button = Button(text="New Game 🌸", font=('Comic Sans MS', 20), bg="hotpink", fg="white", command=new_game)
reset_button.pack(side="top")

frame = Frame(window, bg="#FFD6E8")
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, text="", font=('Comic Sans MS', 30), width=5, height=2,
                                bg="#EBD6FF", fg="deeppink",
                                command=lambda row=i, col=j: next_turn(row, col))
        buttons[i][j].grid(row=i, column=j)

window.mainloop()
