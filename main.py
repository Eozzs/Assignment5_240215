import sqlite3

connection = sqlite3.connect("personal_finance.db")
cursor = connection.cursor()

# cursor.execute('CREATE TABLE finances (id integer PRIMARY KEY, type string, category string, amount integer)')

insert_query = 'INSERT INTO finances (type, category, amount) VALUES(?,?,?)'

category_query = 'SELECT * FROM finances WHERE category = ?'

def enter_incomes():
    with connection:
        i_category = input("Enter income category - salary/project/bonus: ")
        i_amount = input("Enter income amount: ")
        cursor.execute(insert_query, ("Income", i_category, i_amount))
    print(f'Your income added. ')
def enter_expenses():
    with connection:
        e_category = input("Enter expense category - rent/food/car/family/fun: ")
        e_amount = input("Enter expense amount: ")
        cursor.execute(insert_query, ("Expense", e_category, e_amount))
    print(f'Your expense added. ')
def get_all_incomes():
    with connection:
       cursor.execute('SELECT * FROM finances WHERE type = "Income"')
       all_i = cursor.fetchall()
       for i in all_i:
           print(f'ID {i[0]} - {i[1]},  category: {i[2]}, amount: {i[3]}')
def get_all_expenses():
    with connection:
       cursor.execute('SELECT * FROM finances WHERE type = "Expense"')
       all_e = cursor.fetchall()
       for e in all_e:
           print(f'ID {e[0]} - {e[1]}, category: {e[2]}, amount: {e[3]}')
def get_balance():
    with connection:
       cursor.execute('SELECT SUM(amount) FROM finances WHERE type = "Income"')
       i_sum = cursor.fetchone()
       cursor.execute('SELECT SUM(amount) FROM finances WHERE type = "Expense"')
       e_sum = cursor.fetchone()
       balance = i_sum[0] - e_sum[0]
       if balance >= 0:
            print(f'Your balance is: {balance} ')
       else:
            print(f'Your balance is negative: {balance} ... It seems you are in trouble ! ')
def delete_entry():
    with connection:
        cursor.execute('SELECT * FROM finances')
        all_entries= cursor.fetchall()
        print("List of income and expense entries: ")
        for entry in all_entries:
            print(f'ID {entry[0]} - {entry[1]}, category: {entry[2]}, amount: {entry[3]}')
        delete_id = input('Enter ID to delete entry: ')
        cursor.execute('DELETE FROM finances WHERE id = ?', (delete_id,))
        print(f'Deleted successfully.')

def update_entry():
    with connection:
        cursor.execute('SELECT * FROM finances')
        all_entries = cursor.fetchall()
        print("List of income and expense entries: ")
        for entry in all_entries:
            print(f' ID {entry[0]} -{entry[1]}, category: {entry[2]}, amount: {entry[3]}')
        update_id = input('Enter ID to update entry: ')
        type = input('Enter type: ')
        category = input('Enter category: ')
        amount = input('Enter amount: ')
        cursor.execute('UPDATE finances SET type = ?, category = ?, amount = ? WHERE id =?',
                       (type, category, amount, update_id))
        print(f'Updated successfully.')


while True:
    choice = input('Enter income - 1; Enter expense - 2; See all incomes - 3; See all expenses - 4; Get '
                   'balance - 5; Delete entry - 6; Update entry - 7; Quit - q :  ')
    if choice == '1':
        enter_incomes()
    elif choice == '2':
        enter_expenses()
    elif choice == '3':
        get_all_incomes()
    elif choice == '4':
        get_all_expenses()
    elif choice == '5':
        get_balance()
    elif choice == '6':
        delete_entry()
    elif choice == '7':
        update_entry()
    elif choice == 'q':
        exit()
    else:
        print('No input? Try again ;)')