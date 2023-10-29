import tkinter as tk
import secrets
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    result_display.config(text=password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and configure the Length label
length_label = tk.Label(app, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

# Create and configure the Length entry field
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and configure the Generate button
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and configure the Result label
result_display = tk.Label(app, text="", font=('Arial', 16))
result_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
app.mainloop()
