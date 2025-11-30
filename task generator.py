import tkinter as tk
from tkinter import messagebox
import random
import string

# ------------------ Task Generator Function ------------------ #
def generate_task():
    chars = ''
    if letters_var.get():
        chars += string.ascii_letters
    if digits_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Warning", "Please select at least one option!")
        return

    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid positive number.")
        return

    task = ''.join(random.choice(chars) for _ in range(length))
    result_label.config(text=task)

# ------------------ UI Setup ------------------ #
root = tk.Tk()
root.title("Styled Task Generator")
root.geometry("500x400")
root.config(bg="#2e3f4f")

# ------------------ Styling ------------------ #
label_font = ("Segoe UI", 12)
entry_font = ("Segoe UI", 12)
button_font = ("Segoe UI", 12, "bold")

# ------------------ Title ------------------ #
tk.Label(root, text="Task Generator", font=("Segoe UI", 18, "bold"),
         fg="white", bg="#2e3f4f").pack(pady=15)

# ------------------ Length Entry ------------------ #
tk.Label(root, text="Enter Task Length:", font=label_font,
         fg="white", bg="#2e3f4f").pack()
length_entry = tk.Entry(root, font=entry_font, justify='center', width=10)
length_entry.insert(0, "10")
length_entry.pack(pady=5)

# ------------------ Checkboxes ------------------ #
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

check_frame = tk.Frame(root, bg="#2e3f4f")
check_frame.pack(pady=10)

tk.Checkbutton(check_frame, text="Letters", variable=letters_var, font=label_font,
               fg="white", bg="#2e3f4f", activebackground="#2e3f4f", activeforeground="white",
               selectcolor="#2e3f4f").grid(row=0, column=0, padx=10)
tk.Checkbutton(check_frame, text="Digits", variable=digits_var, font=label_font,
               fg="white", bg="#2e3f4f", activebackground="#2e3f4f", activeforeground="white",
               selectcolor="#2e3f4f").grid(row=0, column=1, padx=10)
tk.Checkbutton(check_frame, text="Symbols", variable=symbols_var, font=label_font,
               fg="white", bg="#2e3f4f", activebackground="#2e3f4f", activeforeground="white",
               selectcolor="#2e3f4f").grid(row=0, column=2, padx=10)

# ------------------ Generate Button ------------------ #
generate_btn = tk.Button(root, text="Generate Task", font=button_font,
                         bg="#00bfa5", fg="white", width=20, height=1,
                         activebackground="#00997a", relief="flat", bd=0,
                         command=generate_task)
generate_btn.pack(pady=15)

# ------------------ Result Display ------------------ #
result_label = tk.Label(root, text="", font=("Segoe UI", 14, "bold"),
                        fg="#ffffff", bg="#2e3f4f", wraplength=450, justify='center')
result_label.pack(pady=10)

# ------------------ Start ------------------ #
root.mainloop()
