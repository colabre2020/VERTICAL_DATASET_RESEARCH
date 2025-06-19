import csv
import random
from faker import Faker

fake = Faker()

NUM_USERS = 3000
NUM_PRODUCTS = 1500
NUM_CARTS = 2000
NUM_ORDERS = 4000
NUM_REVIEWS = 2500

def generate_users():
    with open('users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['userID', 'name', 'email', 'phone', 'city'])
        for i in range(1, NUM_USERS+1):
            writer.writerow([
                f'U{i:05d}',
                fake.name(),
                fake.email(),
                fake.phone_number(),
                fake.city()
            ])

def generate_products():
    with open('products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['productID', 'productName', 'category', 'price', 'stock'])
        for i in range(1, NUM_PRODUCTS+1):
            writer.writerow([
                f'P{i:05d}',
                fake.word().capitalize(),
                random.choice(['Electronics', 'Clothing', 'Home', 'Toys', 'Books', 'Beauty']),
                round(random.uniform(5, 2000), 2),
                random.randint(0, 500)
            ])

def generate_carts():
    with open('carts.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cartID', 'userID', 'productID', 'quantity', 'addedDate'])
        for i in range(1, NUM_CARTS+1):
            user_id = f'U{random.randint(1, NUM_USERS):05d}'
            product_id = f'P{random.randint(1, NUM_PRODUCTS):05d}'
            writer.writerow([
                f'C{i+10000}',
                user_id,
                product_id,
                random.randint(1, 5),
                fake.date_between(start_date='-1y', end_date='today')
            ])

def generate_orders():
    with open('orders.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['orderID', 'userID', 'productID', 'orderDate', 'quantity', 'status'])
        for i in range(1, NUM_ORDERS+1):
            user_id = f'U{random.randint(1, NUM_USERS):05d}'
            product_id = f'P{random.randint(1, NUM_PRODUCTS):05d}'
            writer.writerow([
                f'O{i+20000}',
                user_id,
                product_id,
                fake.date_between(start_date='-2y', end_date='today'),
                random.randint(1, 5),
                random.choice(['Placed', 'Shipped', 'Delivered', 'Cancelled'])
            ])

def generate_reviews():
    with open('reviews.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['reviewID', 'userID', 'productID', 'rating', 'review', 'date'])
        for i in range(1, NUM_REVIEWS+1):
            user_id = f'U{random.randint(1, NUM_USERS):05d}'
            product_id = f'P{random.randint(1, NUM_PRODUCTS):05d}'
            writer.writerow([
                f'R{i+30000}',
                user_id,
                product_id,
                random.randint(1, 5),
                fake.sentence(nb_words=8),
                fake.date_between(start_date='-2y', end_date='today')
            ])

if __name__ == '__main__':
    generate_users()
    generate_products()
    generate_carts()
    generate_orders()
    generate_reviews()
    print('Sample e-commerce data generated!')
