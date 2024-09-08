import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length=12, options="upper"):
    """Generate a random password with specified options."""
    if options == "upper":
        characters = string.ascii_uppercase
    elif options == "lower":
        characters = string.ascii_lowercase
    elif options == "numbers":
        characters = string.digits
    elif options == "all":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_uppercase  
    
    return ''.join(random.choice(characters) for _ in range(length))

def show_password():
    """Generate and display the password in the entry field."""
    length = 12 
    option = option_var.get()
    global generated_password
    generated_password = generate_password(length=length, options=option)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

def confirm_password():
    """Check if the entered password matches the generated password."""
    user_input = guess_entry.get()
    if user_input == generated_password:
        messagebox.showinfo("Success", "Password matches!")
    else:
        messagebox.showerror("Error", "Password does not match.")

def copy_password():
    """Copy the generated password to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.configure(bg="lightpink")


generated_password = ""


option_var = tk.StringVar(value="upper")

options_frame = tk.Frame(root,bg="lightpink")
options_frame.pack(pady=10)

tk.Radiobutton(options_frame, text="Include Uppercase Letters",bg="lightpink", variable=option_var, value="upper").pack(anchor="w")
tk.Radiobutton(options_frame, text="Include Lowercase Letters",bg="lightpink", variable=option_var, value="lower").pack(anchor="w")
tk.Radiobutton(options_frame, text="Include Numbers",bg="lightpink", variable=option_var, value="numbers").pack(anchor="w")
tk.Radiobutton(options_frame, text="Include Uppercase, Lowercase, and Numbers",bg="lightpink", variable=option_var, value="all").pack(anchor="w")


password_label = tk.Label(root,bg="#99c9dd", text="Generated Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password",bg="#99c9dd", command=show_password)
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password",bg="red", command=copy_password)
copy_button.pack(pady=10)


guess_label = tk.Label(root, text="Enter Password to Confirm:",bg="#99c9dd")
guess_label.pack(pady=10)

guess_entry = tk.Entry(root, width=50)
guess_entry.pack(pady=5)

confirm_button = tk.Button(root, text="Confirm Password",bg="lightgreen", command=confirm_password)
confirm_button.pack(pady=10)


root.mainloop()
