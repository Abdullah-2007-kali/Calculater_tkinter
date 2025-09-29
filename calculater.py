import tkinter as tk

root = tk.Tk()
# Set the window title
root.title("Calculator")

# Input field (Entry widget) to display operations and results
enter = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
enter.grid(row=0, column=0, columnspan=4, padx=6, pady=6)

# Function to process button clicks and perform operations
def ent(value):
    if value == "C":
        # Clear all text from the input field
        enter.delete(0, tk.END)
    elif value == "=":
        try:
            # Use eval() to calculate the mathematical expression
            result = eval(enter.get())
            enter.delete(0, tk.END)
            enter.insert(tk.END, str(result))
        except:
            # Show error if the expression is invalid
            enter.delete(0, tk.END)
            enter.insert(tk.END, "Error")
    else:
        # Append the pressed button's value to the input field
        enter.insert(tk.END, value) 

# List of button labels for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0
# Create each button from the list and place it in the grid layout
for but in buttons:
    button = tk.Button(
        root,
        text=but,
        width=5,
        height=2,
        font=("Arial", 14),
        command=lambda b=but: ent(b)   # Pass the correct button value to ent()
    )
    button.grid(row=row, column=col, padx=3, pady=3)
    col += 1
    if col > 3:   # Move to the next row after 4 columns
        col = 0
        row += 1

# Start the Tkinter main loop
root.mainloop()
