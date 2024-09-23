import tkinter as tk
from tkinter import messagebox
import sqlite3

# Import database setup (run this once to create the database)
import database_setup

# Main window setup
root = tk.Tk()
root.title("Personal Expense Tracker")

# Widgets for input fields
label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
label_date.grid(row=0, column=0)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=1, column=0)
entry_category = tk.Entry(root)
entry_category.grid(row=1, column=1)

label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=2, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

label_description = tk.Label(root, text="Description:")
label_description.grid(row=3, column=0)
entry_description = tk.Entry(root)
entry_description.grid(row=3, column=1)

# Function to add expense
def add_expense():
    date = entry_date.get()
    category = entry_category.get()
    amount = entry_amount.get()
    description = entry_description.get()

    if date and category and amount:
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                       (date, category, amount, description))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Expense added successfully!")
        entry_date.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill all fields!")

# Add Expense Button
button_add = tk.Button(root, text="Add Expense", command=add_expense)
button_add.grid(row=4, column=1)

# Function to view expenses
def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    # Display expenses in a new window
    view_window = tk.Toplevel(root)
    view_window.title("View Expenses")
    
    for i, row in enumerate(rows):
        tk.Label(view_window, text=row).grid(row=i, column=0)

# Button to View Expenses
button_view = tk.Button(root, text="View Expenses", command=view_expenses)
button_view.grid(row=5, column=1)

root.mainloop()
