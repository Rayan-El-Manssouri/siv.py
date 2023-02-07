import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Siv - 1.0.0")
root.geometry("1280x720")

def button_click():
    print("Button was clicked")

# définir la couleur de la fenêtre
root.configure(bg='white')

# Charger l'image
image = PhotoImage(file="./src/profil.png")

# Redimensionner l'image de profil
new_width = 120
new_height = 120
image = image.subsample(image.width() // new_width, image.height() // new_height)

# Créer un canvas pour l'image
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill='both', expand=True)

# Dessiner l'image sur le canvas
canvas.create_image(1250, 10, image=image, anchor='ne')


# ajouter une barre de menu
menu_bar = tk.Menu(root, bg='black', fg='white')
root.config(menu=menu_bar)

root.mainloop()