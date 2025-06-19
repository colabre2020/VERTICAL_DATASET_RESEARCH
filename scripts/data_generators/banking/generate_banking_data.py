import csv
import random
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 5000
NUM_ACCOUNTS = 8000
NUM_TRANSACTIONS = 10000
NUM_BRANCHES = 200
NUM_EMPLOYEES = 500

def generate_branches():
    with open('branches.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['branchID', 'name', 'city', 'address', 'managerID'])
        for i in range(1, NUM_BRANCHES+1):
            manager_id = f'E{random.randint(1, NUM_EMPLOYEES):04d}'
            writer.writerow([
                f'B{i:03d}',
                fake.company(),
                fake.city(),
                fake.address().replace('\n', ', '),
                manager_id
            ])

def generate_employees():
    with open('employees.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['employeeID', 'name', 'position', 'hireDate', 'branchID', 'email'])
        for i in range(1, NUM_EMPLOYEES+1):
            branch_id = f'B{random.randint(1, NUM_BRANCHES):03d}'
            writer.writerow([
                f'E{i:04d}',
                fake.name(),
                random.choice(['Manager', 'Teller', 'Advisor', 'Clerk']),
                fake.date_between(start_date='-10y', end_date='today'),
                branch_id,
                fake.email()
            ])

def generate_customers():
    with open('bank_customers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['customerID', 'name', 'age', 'gender', 'city', 'email', 'phone', 'joinDate'])
        for i in range(1, NUM_CUSTOMERS+1):
            writer.writerow([
                f'C{i:04d}',
                fake.name(),
                random.randint(18, 80),
                random.choice(['M', 'F']),
                fake.city(),
                fake.email(),
                fake.phone_number(),
                fake.date_between(start_date='-10y', end_date='today')
            ])

def generate_accounts():
    with open('accounts.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['accountID', 'customerID', 'branchID', 'accountType', 'balance', 'openDate', 'status'])
        for i in range(1, NUM_ACCOUNTS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            branch_id = f'B{random.randint(1, NUM_BRANCHES):03d}'
            writer.writerow([
                f'A{i+10000}',
                customer_id,
                branch_id,
                random.choice(['Savings', 'Checking', 'Loan', 'Credit']),
                round(random.uniform(100, 100000), 2),
                fake.date_between(start_date='-10y', end_date='today'),
                random.choice(['Active', 'Dormant', 'Closed'])
            ])

def generate_transactions():
    with open('transactions.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['transactionID', 'accountID', 'amount', 'transactionDate', 'type', 'description'])
        for i in range(1, NUM_TRANSACTIONS+1):
            account_id = f'A{random.randint(10001, 10000+NUM_ACCOUNTS)}'
            writer.writerow([
                f'TX{i+20000}',
                account_id,
                round(random.uniform(-5000, 20000), 2),
                fake.date_between(start_date='-5y', end_date='today'),
                random.choice(['Deposit', 'Withdrawal', 'Transfer', 'Payment']),
                fake.sentence(nb_words=4)
            ])

if __name__ == '__main__':
    generate_branches()
    generate_employees()
    generate_customers()
    generate_accounts()
    generate_transactions()
    print('Sample banking data generated!')
