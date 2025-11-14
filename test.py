#Creating a scientific calculator using Tkinter involves several steps. Below is a step-by-step guide to help you build a basic scientific calculator with a graphical user interface (GUI).
import tkinter as tk
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        print(e)
def clear():
    entry.delete(0, tk.END)
# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
# Create an entry widget for input and output
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) 
# Create buttons for digits and operations
buttons = [1,2,3,4,5,6,7,8,9,0,'+','-','*','/','(',')','.','sin','cos','tan','log','sqrt','^','C','=']
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
# Start the main event loop
root.mainloop()
# Note: This is a basic implementation. You can enhance it by adding more functions, improving the layout, and handling edge cases.
# For example, you can add functionality for the 'C' (clear) and '=' (calculate) buttons:
tk.Button(root, text='C', padx=20, pady=20, command=clear).grid(row=row_val, column=0)
tk.Button(root, text='=', padx=20, pady=20, command=calculate).grid(row=row_val, column=1)
# You can also map the '^' button to '**' for exponentiation in the calculate function.
def calculate():
    try:
        expression = entry.get().replace('^', '**')
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        print(e)
# This will allow users to use the '^' button for exponentiation.
# Remember to test your calculator thoroughly to ensure all functions work as expected!
#Make sure you have added the '=' button with the correct command to call the calculate function.
tk.Button(root, text='=', padx=20, pady=20, command=calculate).grid(row=row_val, column=1)
# Also, ensure that the calculate function is defined before you create the button.
def calculate():
    try:
        expression = entry.get().replace('^', '**')
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        print(e)
