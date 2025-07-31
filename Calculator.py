# Import tkinter for GUI components
import tkinter as tk

# Define the click event handler
def click(event):
    # Get the current text from the display
    current = display.get()
    # Get the text of the clicked button
    button_text = event.widget["text"]

    # If the '=' button is clicked, evaluate the expression
    if button_text == "=":
        try:
            # Try to evaluate the expression using eval()
            result = eval(current)
            display.delete(0, tk.END)        # Clear the display
            display.insert(0, str(result))   # Insert the result
        except Exception as e:
            # If an error occurs (like division by zero), show 'Error'
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif button_text == "C":
        # If 'C' is clicked, clear the display
        display.delete(0, tk.END)
    else:
        # For any other button, append its text to the display
        display.insert(tk.END, button_text)

# Create the main application window
root = tk.Tk()
root.title("Calculator by Arnob Mustakim")         # Set window title
root.geometry("300x400")               # Set window size

# Create the entry widget for input/output display
display = tk.Entry(
    root,                   # Parent is root window
    font="Arial 20",        # Font style and size
    bd=10,                  # Border thickness
    relief=tk.RIDGE,        # 3D style border
    justify=tk.RIGHT        # Align text to the right
)
display.pack(              # Add to window with padding
    fill=tk.BOTH,
    padx=10, pady=10,
    ipadx=8, ipady=8
)

# Define calculator button texts in a grid-like structure
button_texts = [
    ["7", "8", "9", "/"],   # Row 1
    ["4", "5", "6", "*"],   # Row 2
    ["1", "2", "3", "-"],   # Row 3
    ["0", "C", "=", "+"]    # Row 4
]

# Create buttons using nested loops
for row in button_texts:
    frame = tk.Frame(root)     # Create a new frame for each row
    frame.pack(
        expand=True,           # Let it expand vertically
        fill="both"            # Fill both X and Y direction
    )
    for btn_text in row:
        button = tk.Button(
            frame,
            text=btn_text,         # Set button text
            font="Arial 18",       # Font size and style
            relief=tk.RAISED,      # Button style
            bd=4                   # Border thickness
        )
        button.pack(
            side=tk.LEFT,          # Arrange buttons horizontally
            expand=True,           # Allow button to grow
            fill="both"            # Fill entire cell
        )
        button.bind("<Button-1>", click)   # Bind left-click event to `click()` function

# Start the main event loop (keeps window open)
root.mainloop()