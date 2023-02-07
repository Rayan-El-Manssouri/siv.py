import tkinter as tk
from tkinter import PhotoImage

def button_click():
    print("Button was clicked")

root = tk.Tk()
root.title("Clean GUI")
root.geometry("400x200")

icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)
root.wm_iconbitmap("logo.png")

button = tk.Button(root, text="Click Me!", command=button_click, bg="lightblue", fg="white", font=("Helvetica", 16))
button.pack(pady=10)

root.mainloop()