import csv
import random
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 4000
NUM_PRODUCTS = 2000
NUM_ORDERS = 7000
NUM_PAYMENTS = 3000
NUM_RETURNS = 1000

def generate_customers():
    with open('retail_customers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['customerID', 'name', 'city', 'email', 'phone'])
        for i in range(1, NUM_CUSTOMERS+1):
            writer.writerow([
                f'C{i:04d}',
                fake.name(),
                fake.city(),
                fake.email(),
                fake.phone_number()
            ])

def generate_products():
    with open('retail_products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['productID', 'productName', 'category', 'unitPrice', 'unitsInStock'])
        for i in range(1, NUM_PRODUCTS+1):
            writer.writerow([
                f'P{i:05d}',
                fake.word().capitalize(),
                random.choice(['Electronics', 'Clothing', 'Grocery', 'Home', 'Toys', 'Books']),
                round(random.uniform(5, 2000), 2),
                random.randint(0, 500)
            ])

def generate_orders():
    with open('retail_orders.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['orderID', 'customerID', 'productID', 'orderDate', 'quantity', 'orderStatus'])
        for i in range(1, NUM_ORDERS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            product_id = f'P{random.randint(1, NUM_PRODUCTS):05d}'
            writer.writerow([
                f'O{i+10000}',
                customer_id,
                product_id,
                fake.date_between(start_date='-2y', end_date='today'),
                random.randint(1, 10),
                random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'])
            ])

def generate_payments():
    with open('retail_payments.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['paymentID', 'orderID', 'amount', 'paymentDate', 'method', 'status'])
        for i in range(1, NUM_PAYMENTS+1):
            order_id = f'O{random.randint(10001, 10000+NUM_ORDERS)}'
            writer.writerow([
                f'PAY{i+20000}',
                order_id,
                random.randint(10, 2000),
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['Credit', 'Debit', 'UPI', 'Wallet']),
                random.choice(['Success', 'Failed'])
            ])

def generate_returns():
    with open('retail_returns.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['returnID', 'orderID', 'returnDate', 'reason', 'status'])
        for i in range(1, NUM_RETURNS+1):
            order_id = f'O{random.randint(10001, 10000+NUM_ORDERS)}'
            writer.writerow([
                f'R{i+30000}',
                order_id,
                fake.date_between(start_date='-1y', end_date='today'),
                fake.sentence(nb_words=4),
                random.choice(['Approved', 'Rejected', 'Pending'])
            ])

if __name__ == '__main__':
    generate_customers()
    generate_products()
    generate_orders()
    generate_payments()
    generate_returns()
    print('Sample retail data generated!')
