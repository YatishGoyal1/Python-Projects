import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":
    def check():
        global winner
        for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
                for i in combo:
                    buttons[i].config(bg="green")
                messagebox.showinfo("Game Over", f"Player {buttons[combo[0]]['text']} wins!")
                winner = True
                return

        if all(button["text"] != "" for button in buttons) and not winner:
            messagebox.showinfo("Game Over", "It's a draw!")
            winner = True

    def button_click(index):
        if buttons[index]["text"] == "" and not winner:
            buttons[index]["text"] = current_player
            check()
            if not winner:
                toggle_player()

    def toggle_player():
        global current_player
        current_player = "X" if current_player == "O" else "O"
        label.config(text=f"Player {current_player}'s turn ")

    def reset_game():
        global current_player, winner
        current_player = "X"
        winner = False
        label.config(text=f"Player {current_player}'s turn ")
        for button in buttons:
            button.config(text="", bg="SystemButtonFace")

    def quit_game():
        root.destroy()

    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                         command=lambda i=i: button_click(i)) for i in range(9)]
    for i, button in enumerate(buttons):
        button.grid(row=i // 3, column=i % 3)

    current_player = "X"
    winner = False

    label = tk.Label(root, text=f"Player {current_player}'s turn ", font=("normal", 16))
    label.grid(row=3, column=0, columnspan=3)

    reset_button = tk.Button(root, text="Reset Game", font=("normal", 14), command=reset_game)
    reset_button.grid(row=4, column=0, columnspan=1, pady=10)

    quit_button = tk.Button(root, text="Quit", font=("normal", 14), command=quit_game)
    quit_button.grid(row=4, column=2, columnspan=1, pady=10)

    root.mainloop()

