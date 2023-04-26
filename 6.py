import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x400")
root.title("DIALOG BOX")
def mesbo():
    messagebox.showinfo("title box","this is a message box")

button1 = tk.Button(root,text="click me",command=mesbo)
button1.pack()

root.mainloop()