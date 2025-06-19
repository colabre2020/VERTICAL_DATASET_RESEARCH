import csv
import random
from faker import Faker

fake = Faker()

NUM_SUPPLIERS = 500
NUM_PRODUCTS = 3000
NUM_ORDERS = 8000
NUM_CUSTOMERS = 2000
NUM_SHIPMENTS = 6000

# Generate suppliers.csv
def generate_suppliers():
    with open('suppliers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['supplierID', 'name', 'contact', 'city', 'email', 'phone'])
        for i in range(1, NUM_SUPPLIERS+1):
            writer.writerow([
                f'S{i:04d}',
                fake.company(),
                fake.name(),
                fake.city(),
                fake.email(),
                fake.phone_number()
            ])

def generate_products():
    with open('products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['productID', 'supplierID', 'productName', 'category', 'unitPrice', 'unitsInStock', 'reorderLevel'])
        for i in range(1, NUM_PRODUCTS+1):
            supplier_id = f'S{random.randint(1, NUM_SUPPLIERS):04d}'
            writer.writerow([
                f'PR{i:05d}',
                supplier_id,
                fake.word().capitalize(),
                random.choice(['Electronics', 'Food', 'Clothing', 'Furniture', 'Automotive', 'Pharma']),
                round(random.uniform(5, 5000), 2),
                random.randint(0, 1000),
                random.randint(10, 100)
            ])

def generate_customers():
    with open('supply_customers.csv', 'w', newline='') as f:
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

def generate_orders():
    with open('orders.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['orderID', 'customerID', 'productID', 'orderDate', 'quantity', 'orderStatus'])
        for i in range(1, NUM_ORDERS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            product_id = f'PR{random.randint(1, NUM_PRODUCTS):05d}'
            writer.writerow([
                f'O{i+10000}',
                customer_id,
                product_id,
                fake.date_between(start_date='-3y', end_date='today'),
                random.randint(1, 100),
                random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'])
            ])

def generate_shipments():
    with open('shipments.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['shipmentID', 'orderID', 'shipDate', 'deliveryDate', 'carrier', 'status'])
        for i in range(1, NUM_SHIPMENTS+1):
            order_id = f'O{random.randint(10001, 10000+NUM_ORDERS)}'
            ship_date = fake.date_between(start_date='-2y', end_date='today')
            delivery_date = ship_date if random.random() < 0.8 else ''
            writer.writerow([
                f'SH{i+20000}',
                order_id,
                ship_date,
                delivery_date,
                fake.company(),
                random.choice(['In Transit', 'Delivered', 'Delayed', 'Lost'])
            ])

if __name__ == '__main__':
    generate_suppliers()
    generate_products()
    generate_customers()
    generate_orders()
    generate_shipments()
    print('Sample supply chain data generated!')
