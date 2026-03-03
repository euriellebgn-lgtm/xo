import tkinter as tk
from PIL import Image, ImageTk

import pygame

import tictactoe
import snake

# Initialiser pygame pour la musique
pygame.mixer.init()

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

def open_tic_tac_toe():
    stop_music()
    play_music("AdventureBegins.mp3")
    tictactoe.run_game(root)

def open_snake():
    stop_music()
    play_music("AdventureBegins.mp3")
    snake.run_game(root)

root = tk.Tk()
root.title("Menu")
root.geometry("400x400")

bg_img = Image.open("bgimg.jpg")
bg_img = bg_img.resize((400, 400))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Charger les icônes
ttt_img = Image.open("morpion_img.jpg")
ttt_img = ImageTk.PhotoImage(ttt_img.resize((50,50)))

snake_img = Image.open("snake_img.png")
snake_img = ImageTk.PhotoImage(snake_img.resize((70,45)))

# Boutons du menu
ttt_button = tk.Button(root, text="Tic-Tac-Toe", image=ttt_img, compound="left", command=open_tic_tac_toe)
ttt_button.pack(pady=40)

snake_button = tk.Button(root, text="Snake", image=snake_img, compound="left", command=open_snake)
snake_button.pack(pady=20)

root.mainloop()
