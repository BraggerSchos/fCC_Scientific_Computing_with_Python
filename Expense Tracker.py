import smtplib
from email.mime.text import MIMEText

# Function to add a new expense to the list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Function to print all expenses
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate the total sum of all expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter the expenses list by a specific category
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# Function to generate the content of the email
def generate_email_content(expenses):
    if not expenses:
        return "No expenses recorded."

    content = "Here is your list of expenses:\n\n"
    for expense in expenses:
        content += f"- Amount: {expense['amount']} Lei, Category: {expense['category']}\n"
    content += f"\nTotal Expenses: {total_expenses(expenses)} Lei"
    return content

# Function to send an email with the expense report
def send_email(expenses):
    sender = ''  # Your email
    app_password = ''  # Your app password
    recipient = ''  # Recipient's email
    subject = 'Your Expense Tracker Report'
    email_content = generate_email_content(expenses)

    msg = MIMEText(email_content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, app_password)
            smtp.sendmail(sender, recipient, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function to manage the Expense Tracker program
def main():
    expenses = []  # Initialize the list to store expenses

    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Send expense report via email')
        print('6. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':  # Add a new expense
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':  # Display all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':  # Show the total amount of expenses
            print('\nTotal Expenses:', total_expenses(expenses))

        elif choice == '4':  # Filter and display expenses by category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            filtered_expenses = filter_expenses_by_category(expenses, category)
            print_expenses(filtered_expenses)

        elif choice == '5':  # Send expense report via email
            send_email(expenses)

        elif choice == '6':  # Exit the program
            print('Exiting the program.')
            break

# Run the program
main()