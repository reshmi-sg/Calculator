import tkinter as tk
import tkinter.messagebox

# Create Main Window
win = tk.Tk()
win.title('Calculator')
win_width = 300
win_height =460

# Center the window
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width // 2) - (win_width // 2)
y = (screen_height // 2) - (win_height // 2)
win.geometry(f"{win_width}x{win_height}+{x}+{y}")
win.configure(bg="#121212")
win.resizable(False, False)

# Entry Field
entry = tk.Entry(win, font=("Arial", 20), bd=0, bg="#1e1e1e", fg="white", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Function to handle button click
def click(val):
    if val == 'AC':
        entry.delete(0, tk.END)
    elif val == '⌫':
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    elif val == '=':
        try:
            expr = entry.get().replace('×', '*').replace('÷', '/').replace('−', '-')
            result = eval(expr)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            tk.messagebox.showerror("Error", "Invalid Expression")
    else:
        entry.insert(tk.END, val)

buttons = [
    ['(', ')', '%', 'AC'],
    ['⌫', '7', '8', '9'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '−'],
    ['0', '.', '=', '+']
]

# Frame for buttons
btn_frame = tk.Frame(win, bg="#121212")
btn_frame.pack()

# Create buttons
def create_button(txt, r, c):
    bg = "#1f1f1f"
    fg = "white"
    if txt == '=':
        bg = "#4d90fe"
    elif txt in ['+', '−', '×', '÷']:
        fg = "#4d90fe"
    elif txt == 'AC':
        fg = "#ff4d4d"
    elif txt == '⌫':
        fg = "#ffa500"

    btn = tk.Button(
        btn_frame, text=txt, font=("Arial", 14),
        bg=bg, fg=fg, width=5, height=2,
        relief="flat", activebackground="#333",
        command=lambda t=txt: click(t)
    )
    btn.grid(row=r, column=c, padx=4, pady=4)

# Place buttons in grid
for i, row in enumerate(buttons):
    for j, txt in enumerate(row):
        create_button(txt, i, j)

# Run the app
#win.mainloop()
