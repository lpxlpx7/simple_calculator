import tkinter as tk
from tkinter import ttk
import math

def button_click(symbol):
    if symbol == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == 'C':
        entry.delete(0, tk.END)
    elif symbol == '⌫':
        entry.delete(0, tk.END)
    elif symbol == '^':
        entry.insert(tk.END, '**')
    elif symbol == '√':
        entry.insert(tk.END, 'math.sqrt(')
    elif symbol in ('sin', 'cos', 'tan'):
        entry.insert(tk.END, 'math.' + symbol + '(')
    else:
        entry.insert(tk.END, symbol)

def create_button(symbol, row, column, columnspan=1):
    button = ttk.Button(root, text=symbol, width=6, command=lambda: button_click(symbol))
    button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5, sticky="nsew")

root = tk.Tk()
root.title("计算机")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16), relief="flat", background="#d3d3d3")
style.map("TButton", background=[("active", "#b0b0b0")])

entry = tk.Entry(root, width=30, borderwidth=5, font=("Helvetica", 18))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0, 2), ('.', 4, 2), ('+', 4, 3), ('=', 4, 4),
    ('C', 1, 4), ('⌫', 1, 3), ('%', 2, 4), ('(', 3, 0), (')', 3, 1), ('^', 3, 4),
    ('sin', 1, 5), ('cos', 2, 5), ('tan', 3, 5), ('√', 4, 5)
]

for button in buttons:
    create_button(*button)


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
