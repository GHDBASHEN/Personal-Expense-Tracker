import sqlite3
from tkinter import messagebox

# Function to delete an expense by ID
def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Expense deleted successfully!")

# Example usage
if __name__ == '__main__':
    expense_id = input("Enter the expense ID to delete: ")
    delete_expense(expense_id)
