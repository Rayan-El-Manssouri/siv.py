import tkinter as tk

root = tk.Tk()
root.title("Siv - Welcom")
root.geometry("1280x720")


def button_click():
    print("Button was clicked")

GestionPersonne = tk.Button(root, text="Gestion personne", command=button_click)
GestionPersonne.pack()

GestionVehicule = tk.Button(root, text="Gestion véhicule!", command=button_click)
GestionVehicule.pack()

GestionOperation = tk.Button(root, text="Gestion opération", command=button_click)
GestionOperation.pack()

# définir la couleur de la fenêtre
root.configure(bg='white')

# ajouter une barre de menu
menu_bar = tk.Menu(root, bg='black', fg='white')
root.config(menu=menu_bar)




root.mainloop()
