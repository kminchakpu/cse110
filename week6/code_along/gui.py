import math
import tkinter as tk
from tkinter import ttk


def calculate_area():
    """Validates input, computes the area of a circle, and updates the GUI."""
    # Clear any previous error messages
    lbl_status.config(text="", foreground="black")

    try:
        # Retrieve and parse input string to a float
        input_text = ent_radius.get().strip()

        if not input_text:
            raise ValueError("Input is empty.")

        radius = float(input_text)

        if radius < 0:
            raise ValueError("Radius cannot be negative.")

        # Perform the calculation
        area = math.pi * (radius**2)

        # Display the result formatted to 2 decimal places
        lbl_result_value.config(text=f"{area:.2f}")

    except ValueError as ex:
        # Reset result display on error
        lbl_result_value.config(text="--")

        # Handle specific error messaging for the status bar
        if "empty" in str(ex):
            lbl_status.config(text="Error: Please enter a radius value.", foreground="red")
        elif "negative" in str(ex):
            lbl_status.config(text="Error: Radius cannot be a negative number.", foreground="red")
        else:
            lbl_status.config(text="Error: Invalid input. Please enter a valid number.", foreground="red")


def clear_fields():
    """Clears all input fields, output labels, and status bar messages."""
    ent_radius.delete(0, tk.END)
    lbl_result_value.config(text="--")
    lbl_status.config(text="", foreground="black")
    ent_radius.focus()


# --- GUI Setup ---

# Initialize the main window
root = tk.Tk()
root.title("Circle Area Calculator")
root.geometry("380x220")
root.resizable(False, False)

# Create a main frame with padding for layout structure
frame = ttk.Frame(root, padding="20 20 20 10")
frame.grid(row=0, column=0, sticky="nsew")

# Configure weights 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Input Row
lbl_radius = ttk.Label(frame, text="Enter Radius:")
lbl_radius.grid(row=0, column=0, padx=5, pady=10, sticky="W")

ent_radius = ttk.Entry(frame, width=15)
ent_radius.grid(row=0, column=1, padx=5, pady=10, sticky="W")
ent_radius.focus()  # Places cursor in the input box on launch

# Output Row
lbl_result_text = ttk.Label(frame, text="Calculated Area:")
lbl_result_text.grid(row=1, column=0, padx=5, pady=10, sticky="W")

lbl_result_value = ttk.Label(frame, text="--", font=("Arial", 10, "bold"))
lbl_result_value.grid(row=1, column=1, padx=5, pady=10, sticky="W")

# Action Buttons Row
btn_calculate = ttk.Button(frame, text="Calculate", command=calculate_area)
btn_calculate.grid(row=2, column=0, padx=5, pady=15, sticky="W")

btn_clear = ttk.Button(frame, text="Clear", command=clear_fields)
btn_clear.grid(row=2, column=1, padx=5, pady=15, sticky="W")

#Status Bar Enhancement
# Attached to 'root' directly at the bottom row to stretch across the entire window
lbl_status = ttk.Label(root, text="", relief=tk.SUNKEN, anchor="w", padding="5 2 5 2")
lbl_status.grid(row=1, column=0, sticky="we")

# Start the application loop
root.mainloop()