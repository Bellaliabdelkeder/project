import tkinter as tk
from tkinter import messagebox
from database import authenticate_user, add_user
from snake_game import start_game

def login():
    def try_login():
        username = entry_username.get()
        password = entry_password.get()
        if authenticate_user(username, password):
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            root.destroy()
            start_game()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def create_account():
        username = entry_username.get()
        password = entry_password.get()
        if username and password:
            try:
                add_user(username, password)
                messagebox.showinfo("Account Created", "Your account has been created successfully!")
            except ValueError as e:
                messagebox.showerror("Error", str(e))  # Show error if username exists
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password")

    root = tk.Tk()
    root.title("Snake Game Login")

    label_username = tk.Label(root, text="Username:")
    label_username.pack()

    entry_username = tk.Entry(root)
    entry_username.pack()

    label_password = tk.Label(root, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    login_button = tk.Button(root, text="Login", command=try_login)
    login_button.pack()

    create_button = tk.Button(root, text="Create Account", command=create_account)
    create_button.pack()

    root.mainloop()
