import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Siv - Welcom")
root.geometry("1280x720")


def button_click():
    print("Button was clicked")



# définir la couleur de la fenêtre
root.configure(bg='white')

# Charger l'image
image = PhotoImage(file="./src/profil.png")


# Créer un canvas pour l'image
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill='both', expand=True)

# Dessiner l'image sur le canvas
canvas.create_image(0, 0, image=image, anchor='nw')


# ajouter une barre de menu
menu_bar = tk.Menu(root, bg='black', fg='white')
root.config(menu=menu_bar)

root.mainloop()
