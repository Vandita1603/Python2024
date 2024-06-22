import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe")
buttons = []

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", bg="pink", fg="black", bd=3, font=('Arial', 20), width=6, height=3,
                           command=lambda i=i, j=j: button_click(i, j))
        button.grid(row=i, column=j, sticky="nsew")
        row.append(button)
    buttons.append(row)

def button_click(row, col):
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = "X"  # Assuming player 1 is X
        # Check if player X wins
        if check_winner("X"):
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            reset_board()
        # Check for a tie
        elif check_tie():
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_board()
        else:
            # Simulate computer's move (assuming computer is O)
            computer_move()
def check_winner(player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(buttons[i][j]["text"] == player for j in range(3)) or \
                all(buttons[j][i]["text"] == player for j in range(3)):
            return True
    if buttons[0][0]["text"] == player and buttons[1][1]["text"] == player and buttons[2][2]["text"] == player:
        return True
    if buttons[0][2]["text"] == player and buttons[1][1]["text"] == player and buttons[2][0]["text"] == player:
        return True
    return False

def check_tie():
    # Check if all buttons are filled
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True
import random

def computer_move():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if buttons[row][col]["text"] == "":
            buttons[row][col]["text"] = "O"  # Assuming computer is O
            # Check if computer wins
            if check_winner("O"):
                messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                reset_board()
            # Check for a tie
            elif check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                reset_board()
            break
def reset_board():
    for row in buttons:
        for button in row:
            button["text"] = ""
root.mainloop()