import tkinter as tk
from tkinter import messagebox

def show_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Popup", "Hello, this is a popup window!")
    root.destroy()

print("Hello world")
show_popup()