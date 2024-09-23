import tkinter as tk
from tkinter import messagebox
import sqlite3

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
    
    if rows:
        # Create headings for columns
        headings = ["ID", "Date", "Category", "Amount", "Description"]
        for col, heading in enumerate(headings):
            tk.Label(view_window, text=heading, font=('bold')).grid(row=0, column=col)

        # Populate rows with expense data
        for i, row in enumerate(rows, start=1):
            for j, value in enumerate(row):
                tk.Label(view_window, text=value).grid(row=i, column=j)
    else:
        tk.Label(view_window, text="No expenses found.").grid(row=0, column=0)

# Button to View Expenses
button_view = tk.Button(root, text="View Expenses", command=view_expenses)
button_view.grid(row=5, column=1)

# Function to delete expense by ID
def delete_expense():
    expense_id = entry_delete.get()

    if expense_id:
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()

        if cursor.rowcount == 0:
            messagebox.showerror("Error", "No expense found with that ID!")
        else:
            messagebox.showinfo("Success", "Expense deleted successfully!")
        entry_delete.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter an expense ID!")

# Delete Expense Section
label_delete = tk.Label(root, text="Delete Expense (Enter ID):")
label_delete.grid(row=6, column=0)
entry_delete = tk.Entry(root)
entry_delete.grid(row=6, column=1)

button_delete = tk.Button(root, text="Delete Expense", command=delete_expense)
button_delete.grid(row=7, column=1)

# Function to search expenses by category
def search_expense():
    category = entry_search.get()

    if category:
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
        rows = cursor.fetchall()
        conn.close()

        # Display search results in a new window
        search_window = tk.Toplevel(root)
        search_window.title(f"Search Results for '{category}'")
        
        if rows:
            # Create headings for columns
            headings = ["ID", "Date", "Category", "Amount", "Description"]
            for col, heading in enumerate(headings):
                tk.Label(search_window, text=heading, font=('bold')).grid(row=0, column=col)

            # Populate rows with search results
            for i, row in enumerate(rows, start=1):
                for j, value in enumerate(row):
                    tk.Label(search_window, text=value).grid(row=i, column=j)
        else:
            tk.Label(search_window, text="No matching expenses found.").grid(row=0, column=0)
    else:
        messagebox.showerror("Error", "Please enter a category to search!")

# Search Expense Section
label_search = tk.Label(root, text="Search by Category:")
label_search.grid(row=8, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=8, column=1)

button_search = tk.Button(root, text="Search Expense", command=search_expense)
button_search.grid(row=9, column=1)

root.mainloop()
