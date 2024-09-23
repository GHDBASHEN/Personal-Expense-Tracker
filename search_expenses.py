import sqlite3

# Function to search for expenses by keyword
def search_expenses(keyword):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    query = "SELECT * FROM expenses WHERE description LIKE ? OR category LIKE ?"
    cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
    results = cursor.fetchall()
    conn.close()

    return results

# Example usage
if __name__ == '__main__':
    keyword = input("Enter a keyword to search expenses: ")
    results = search_expenses(keyword)
    for row in results:
        print(row)
