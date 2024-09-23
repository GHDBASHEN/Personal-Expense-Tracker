import sqlite3
import matplotlib.pyplot as plt

# Function to generate expense report
def generate_report():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    conn.close()

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    # Create a pie chart
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.show()

# Test report generation
if __name__ == '__main__':
    generate_report()
