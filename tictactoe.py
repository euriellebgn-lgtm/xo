import tkinter as tk
import random

def run_game():
    game = tk.Tk()
    game.title("Tic-Tac-Toe")

    players = ["X", "O"]
    player = random.choice(players)

    buttons = [[None for _ in range(3)] for _ in range(3)]

    label = tk.Label(game, text=player + " turn", font=("Helvetica", 20))
    label.pack()

    def check_winner():
        for row in range(3):
            if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
                for col in range(3):
                    buttons[row][col].config(bg="green", fg="white")
                return True

        for col in range(3):
            if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
                for row in range(3):
                    buttons[row][col].config(bg="green", fg="white")
                return True

        if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            for i in range(3):
                buttons[i][i].config(bg="green", fg="white")
            return True

        if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            buttons[0][2].config(bg="green", fg="white")
            buttons[1][1].config(bg="green", fg="white")
            buttons[2][0].config(bg="green", fg="white")
            return True

        empty = any(buttons[r][c]["text"] == "" for r in range(3) for c in range(3))
        if not empty:
            for r in range(3):
                for c in range(3):
                    buttons[r][c].config(bg="yellow")
            return "Tie"

        return False

    def next_turn(r, c):
        nonlocal player
        if buttons[r][c]["text"] == "" and not check_winner():
            buttons[r][c]["text"] = player

            result = check_winner()
            if result == "Tie":
                label.config(text="Tie!")
            elif result:
                label.config(text=player + " wins!")
            else:
                player = players[1] if player == players[0] else players[0]
                label.config(text=player + " turn")

    frame = tk.Frame(game)
    frame.pack()

    for r in range(3):
        for c in range(3):
            buttons[r][c] = tk.Button(
                frame,
                text="",
                font=("Consolas", 30),
                width=5,
                height=2,
                command=lambda r=r, c=c: next_turn(r, c)
            )
            buttons[r][c].grid(row=r, column=c)

    def restart():
        nonlocal player
        player = random.choice(players)
        label.config(text=player + " turn")
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(text="", bg="SystemButtonFace")

    tk.Button(game, text="Restart", command=restart).pack(pady=5)

    game.mainloop()


run_game()
