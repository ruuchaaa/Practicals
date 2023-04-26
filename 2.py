#Write a program based on GUI, window with a label and two buttons
import tkinter as tk

window = tk.Tk()
window.title("The Person App")
window.geometry("400x300")
label = tk.Label(window, text="Is Rucha a kind homosapien?")
label.pack()

button1 = tk.Button(window, text="YES")
button1.pack()

button2 = tk.Button(window, text="NO")
button2.pack()

window.mainloop()