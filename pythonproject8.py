import tkinter as tk
from tkinter import messagebox

# Function to check the winner
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return buttons[row][0]['text']

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return buttons[0][col]['text']

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']

    return None

# Function to handle button clicks
def button_click(row, col):
    global game_over
    if buttons[row][col]['text'] == "" and not game_over:
        buttons[row][col]['text'] = current_player
        winner = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            game_over = True
        elif all(button['text'] != "" for row in buttons for button in row):
            messagebox.showinfo("Game Over", "It's a tie!")
            game_over = True
        else:
            switch_player()

# Function to switch between players
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    result_label.config(text=f"Player {current_player}'s turn")

# Function to reset the game
def reset_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#ffffff")
    result_label.config(text="Player X's turn")

# Set up the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("350x400")
root.configure(bg="#34495e")

# Initialize game variables
current_player = "X"
game_over = False

# Create the Tic-Tac-Toe board buttons
buttons = [[None, None, None] for _ in range(3)]

button_style = {
    "font": ("Arial", 24, "bold"),
    "width": 5,
    "height": 2,
    "bg": "#ecf0f1",
    "bd": 2,
    "relief": "raised",
    "activebackground": "#95a5a6",
    "activeforeground": "white",
    "highlightbackground": "#2c3e50"
}

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", **button_style, command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 14, "bold"), bg="#e74c3c", fg="white", command=reset_game, width=20)
reset_btn.grid(row=3, column=0, columnspan=3, pady=10)

# Game status label
result_label = tk.Label(root, text="Player X's turn", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Run the app
root.mainloop()
