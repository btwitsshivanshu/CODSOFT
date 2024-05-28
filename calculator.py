import tkinter as tk

def button_click(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(item))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=button_clear)
clear_button.grid(row=4, column=1, columnspan=1)

root.mainloop()
