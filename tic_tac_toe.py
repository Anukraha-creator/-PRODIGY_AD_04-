import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_buttons()
        self.create_reset_button()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 15), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.check_winner() is None:
            self.buttons[row][col]["text"] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
            elif self.is_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return self.buttons[i][0]["text"]
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return self.buttons[0][i]["text"]

        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return self.buttons[0][0]["text"]
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return self.buttons[0][2]["text"]

        return None

    def is_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def reset_game(self):
        self.player = "X"
        for row in self.buttons:
            for button in row:
                button["text"] = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
