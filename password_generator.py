import tkinter as tk
import string
import secrets
import pyperclip

# ------------------ Functions ------------------ #
def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)

# ------------------ GUI Setup ------------------ #
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="🔐 Automatic Password Generator", font=("Helvetica", 14, "bold"))
heading.pack(pady=10)

# Password Length Entry
length_frame = tk.Frame(root)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5)
length_entry.insert(0, "12")
length_entry.pack(side=tk.LEFT)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white")
generate_btn.pack(pady=10)

# Password Entry Display
password_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
password_entry.pack(pady=10)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white")
copy_btn.pack(pady=5)

# Start the GUI
root.mainloop()
