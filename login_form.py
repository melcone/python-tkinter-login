import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Mel's Login Form")
root.geometry("500x500")
root.configure(bg="#111111")

title_label = tk.Label(
    root,
    text="Login",
    font=("Arial", 20, "bold"),
    bg="#111111",
    fg="white"
)
title_label.pack(pady=5)

username_label = tk.Label(
    root,
    text="Username",
    anchor="w",
    font=("Arial", 11),
    bg="#111111",
    fg="white"
)
username_label.pack(pady=(20, 5), padx=135, fill=tk.X)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
username_entry.pack(pady=5)

password_label = tk.Label(
    root,
    text="Password",
    anchor="w",
    font=("Arial", 12),
    bg="#111111",
    fg="white"
)
password_label.pack(pady=(20, 5), padx=135, fill=tk.X)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    show="*"
)
password_entry.pack(pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username or Password!"
        )

login_button = tk.Button(
    root,
    text="Log In",
    font=("Arial", 12, "bold"),
    bg="#3DAAFF",
    fg="white",
    width=10,
    command=login
)
login_button.pack(pady=20)

root.mainloop()