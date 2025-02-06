import tkinter as tk
from tkinter import messagebox
import math

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry_var.set("")
    elif button_text == "√":
        try:
            result = math.sqrt(float(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "^":
        entry_var.set(entry_var.get() + "**")
    else:
        entry_var.set(entry_var.get() + button_text)

# Create main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("390x500")

# Create Entry Widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
    (".", "^", "√", "(") ,
    (")", "sin", "cos", "tan")
]

def scientific_function(func):
    try:
        result = getattr(math, func)(math.radians(float(entry_var.get())))
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

for r, row in enumerate(buttons):
    for c, button_text in enumerate(row):
        if button_text in ["sin", "cos", "tan"]:
            btn = tk.Button(root, text=button_text, font=("Arial", 18), padx=20, pady=20,
                             command=lambda text=button_text: scientific_function(text))
        else:
            btn = tk.Button(root, text=button_text, font=("Arial", 18), padx=20, pady=20,
                             command=lambda text=button_text: on_click(text))
        btn.grid(row=r+1, column=c, sticky="nsew")

# Run the application
root.mainloop()
