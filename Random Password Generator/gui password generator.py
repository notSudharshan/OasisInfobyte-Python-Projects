import tkinter as gui
from tkinter import messagebox
import random
import string
def generate_password():
    length = int(length_entry.get())
    thepass = ""
    if letters.get():
        thepass += string.ascii_letters
    if numbers.get():
        thepass += string.digits
    if symbols.get():
        thepass += string.punctuation
    password = ''.join(random.choice(thepass) for _ in range(length))
    output.set(password) 

root = gui.Tk()
root.title("Password Maker 2025")
root.geometry("400x300")
root.resizable(False, False)
gui.Label(root, text="Password Maker 2025", font=("Helvetica", 16, "bold")).pack(pady=10)
gui.Label(root, text="Password Length:").pack()
length_entry = gui.Entry(root, width=10, justify='center')
length_entry.pack()
letters= gui.BooleanVar()
numbers= gui.BooleanVar()
symbols = gui.BooleanVar()
gui.Checkbutton(root, text="Include Letters", variable=letters).pack()
gui.Checkbutton(root, text="Include Numbers", variable=numbers).pack()
gui.Checkbutton(root, text="Include Symbols", variable=symbols).pack()
output= gui.StringVar()
gui.Entry(root, textvariable=output, width=40, justify='center', state='readonly').pack(pady=10)
gui.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
gui.Button(root, text="Exit", command=root.destroy).pack(pady=5)
root.mainloop()
