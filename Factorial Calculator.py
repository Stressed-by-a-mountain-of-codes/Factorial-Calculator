import tkinter as tk
from tkinter import messagebox
import math

def calculate_factorial():
    num = entry.get()
    if not num.isdigit():
        messagebox.showerror("Invalid Input", "Enter a non-negative integer.")
        return
    n = int(num)
    result = math.factorial(n)
    result_label.config(text=f"{n}! = {result}", fg="darkblue")
    root.after(3000, reset)

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Factorial Calculator")
root.geometry("360x220")
root.resizable(False, False)

tk.Label(root, text="Enter a number:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack()
entry.bind("<Return>", lambda e: calculate_factorial())

tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate_factorial).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 11), wraplength=330, justify="center")
result_label.pack(pady=10)

entry.focus()
root.mainloop()
