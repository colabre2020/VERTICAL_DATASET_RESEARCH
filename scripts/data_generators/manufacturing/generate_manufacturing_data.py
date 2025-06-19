import csv
import random
from faker import Faker

fake = Faker()

NUM_PLANTS = 50
NUM_MACHINES = 300
NUM_WORKERS = 1000
NUM_ORDERS = 2000
NUM_MAINTENANCE = 800

def generate_plants():
    with open('plants.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['plantID', 'name', 'city', 'address'])
        for i in range(1, NUM_PLANTS+1):
            writer.writerow([
                f'PL{i:03d}',
                fake.company(),
                fake.city(),
                fake.address().replace('\n', ', ')
            ])

def generate_machines():
    with open('machines.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['machineID', 'plantID', 'type', 'installDate', 'status'])
        for i in range(1, NUM_MACHINES+1):
            plant_id = f'PL{random.randint(1, NUM_PLANTS):03d}'
            writer.writerow([
                f'M{i:04d}',
                plant_id,
                random.choice(['CNC', 'Lathe', 'Drill', 'Press', 'Robot']),
                fake.date_between(start_date='-10y', end_date='today'),
                random.choice(['Active', 'Maintenance', 'Inactive'])
            ])

def generate_workers():
    with open('workers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['workerID', 'name', 'plantID', 'hireDate', 'role'])
        for i in range(1, NUM_WORKERS+1):
            plant_id = f'PL{random.randint(1, NUM_PLANTS):03d}'
            writer.writerow([
                f'W{i:05d}',
                fake.name(),
                plant_id,
                fake.date_between(start_date='-10y', end_date='today'),
                random.choice(['Operator', 'Technician', 'Supervisor', 'Engineer'])
            ])

def generate_orders():
    with open('orders.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['orderID', 'plantID', 'product', 'quantity', 'orderDate', 'status'])
        for i in range(1, NUM_ORDERS+1):
            plant_id = f'PL{random.randint(1, NUM_PLANTS):03d}'
            writer.writerow([
                f'O{i+10000}',
                plant_id,
                fake.word().capitalize(),
                random.randint(1, 1000),
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['Pending', 'In Progress', 'Completed', 'Cancelled'])
            ])

def generate_maintenance():
    with open('maintenance.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['maintenanceID', 'machineID', 'date', 'description', 'status'])
        for i in range(1, NUM_MAINTENANCE+1):
            machine_id = f'M{random.randint(1, NUM_MACHINES):04d}'
            writer.writerow([
                f'MA{i+20000}',
                machine_id,
                fake.date_between(start_date='-2y', end_date='today'),
                fake.sentence(nb_words=6),
                random.choice(['Scheduled', 'Completed', 'Overdue'])
            ])

if __name__ == '__main__':
    generate_plants()
    generate_machines()
    generate_workers()
    generate_orders()
    generate_maintenance()
    print('Sample manufacturing data generated!')
