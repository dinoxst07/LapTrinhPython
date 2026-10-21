import tkinter as tk
from tkinter import messagebox

def on_click(char):
    
    current = entry_var.get()
    if current == ["SyntaxError", "<class 'SyntaxError'>"]:
        current = ""
        return
    entry_var.set(current + str(char))

def clear():
    entry_var.set("")

def calculate():
    
    try:
        expression = entry_var.get()
        result = eval(expression)
        entry_var.set(str(result))
    except Exception:
        entry_var.set("SyntaxError")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)
entry_var = tk.StringVar()

entry = tk.Entry(
    root, 
    textvariable=entry_var, 
    font=("Arial", 22), 
    justify="right", 
)
entry.pack(fill=tk.BOTH, padx=15, pady=15, ipady=10)
btns_frame = tk.Frame(root)
btns_frame.pack(padx=10, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(
        btns_frame, 
        text=text, 
        font=("Arial", 16, "bold"), 
        width=5, 
        height=2,
        command=lambda t=text: on_click(t)
    )
    btn.grid(row=row, column=col, padx=4, pady=4)

btn_clear = tk.Button(
    btns_frame, 
    text="C", 
    font=("Arial", 16, "bold"), 
    width=5, 
    height=2, 
    command=clear
)
btn_clear.grid(row=4, column=2, padx=4, pady=4)


btn_equal = tk.Button(
    btns_frame, 
    text="=", 
    font=("Arial", 16, "bold"), 
    width=11, 
    height=2, 
    command=calculate
)
btn_equal.grid(row=5, column=0, columnspan=2, padx=4, pady=4)

root.mainloop()