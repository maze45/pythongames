import tkinter as tk

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.configure(bg="#1e1e1e")

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.FLAT, justify='right')
entry.pack(fill='both', padx=10, pady=10)

# Button frame
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(btn_frame, bg="#1e1e1e")
    row_frame.pack(fill='both', expand=True)
    for btn_text in row:
        if btn_text == 'C':
            btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), bg="#f87171", fg="white",
                            width=5, height=2, command=clear)
        elif btn_text == '=':
            btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), bg="#34d399", fg="white",
                            width=5, height=2, command=calculate)
        else:
            btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), bg="#4b5563", fg="white",
                            width=5, height=2)
            btn.bind("<Button-1>", click)
        btn.pack(side='left', padx=5, pady=5)

# Run the app
root.mainloop()
