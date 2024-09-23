
# Personal Expense Tracker

This is a simple **Personal Expense Tracker** application built using **Python** and **Tkinter**. The application allows users to add, view, search, and delete expenses. It also stores the data using an **SQLite** database.

## Features

- **Add Expense**: Add expenses by providing the date, category, amount, and description.
- **View Expenses**: View all expenses in a table format.
- **Search Expense**: Search expenses based on category or date.
- **Delete Expense**: Delete a specific expense by ID.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GHDBASHEN/Personal-Expense-Tracker.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the database setup script (if not already set up):
    ```bash
    python database_setup.py
    ```

4. Start the application:
    ```bash
    python main.py
    ```

## Database

The application uses an **SQLite** database (`expenses.db`) to store the following fields:
- `ID`: A unique identifier for each expense.
- `Date`: Date of the expense.
- `Category`: The category of the expense (e.g., food, transportation).
- `Amount`: The amount spent.
- `Description`: A short description of the expense.

## How to Use

1. **Add Expense**: Fill in the form with the date, category, amount, and description, then click "Add Expense".
2. **View Expenses**: Click the "View Expenses" button to see all the recorded expenses.
3. **Search Expense**: Enter a category or date to filter expenses and click "Search".
4. **Delete Expense**: Enter the ID of the expense you want to delete, then click "Delete Expense".

## Future Enhancements

- Add data visualization for expense trends.
- Export expenses to CSV or Excel format.
- Add expense editing functionality.

## License

This project is licensed under the MIT License.
"""

# Save the content to a README.md file.
with open("/mnt/data/README.md", "w") as file:
    file.write(readme_content)

"/mnt/data/README.md"  # Returning the file path for download.
