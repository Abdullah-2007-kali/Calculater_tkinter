1. Create the main window

Every Tkinter program starts with a root window.

import tkinter as tk

root = tk.Tk()       # Create the main window
root.title("My First App")  # Set the title
root.geometry("300x200")    # Set size (width x height)

2. Add Widgets (buttons, labels, entries, etc.)

Widgets are the building blocks of Tkinter GUIs.

# Label (text on screen)
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))

# Entry (text input field)
entry = tk.Entry(root, width=20)

# Button (clickable button)
button = tk.Button(root, text="Click Me")

3. Place Widgets

You need to position widgets inside the window.
There are 3 main layout managers:

pack() – simple top-down arrangement.

grid() – place in rows and columns (like a table).

place() – absolute positioning (x, y).

Example with grid():

label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=1, column=0, padx=10, pady=10)
button.grid(row=2, column=0, padx=10, pady=10)

4. Add Functionality (event handling)

Widgets can do actions when clicked.
For example, making a button show text from an entry:

def on_click():
    user_text = entry.get()
    label.config(text=f"You typed: {user_text}")

button.config(command=on_click)

5. Run the Application

Finally, start Tkinter’s event loop:

root.mainloop()

✅ Full Example: Simple Input & Button
import tkinter as tk

# Create window
root = tk.Tk()
root.title("Basic Tkinter Example")
root.geometry("300x200")

# Widgets
label = tk.Label(root, text="Type something:", font=("Arial", 12))
entry = tk.Entry(root, width=20)
button = tk.Button(root, text="Show")

# Function for button
def on_click():
    text = entry.get()
    label.config(text=f"You typed: {text}")

button.config(command=on_click)

# Layout
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=1, column=0, padx=10, pady=10)
button.grid(row=2, column=0, padx=10, pady=10)

# Run
root.mainloop()
