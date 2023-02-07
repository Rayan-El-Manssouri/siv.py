import tkinter as tk

root = tk.Tk()
root.title("Clean GUI")
root.iconbitmap("logo.png")

def button_click():
    print("Button was clicked")

button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

root.mainloop()