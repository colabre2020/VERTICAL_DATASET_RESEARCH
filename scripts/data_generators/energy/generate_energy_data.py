import csv
import random
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 2500
NUM_METERS = 2500
NUM_USAGE = 10000
NUM_OUTAGES = 300
NUM_BILLS = 3000

def generate_customers():
    with open('energy_customers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['customerID', 'name', 'address', 'city', 'email', 'phone'])
        for i in range(1, NUM_CUSTOMERS+1):
            writer.writerow([
                f'C{i:04d}',
                fake.name(),
                fake.address().replace('\n', ', '),
                fake.city(),
                fake.email(),
                fake.phone_number()
            ])

def generate_meters():
    with open('meters.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['meterID', 'customerID', 'installDate', 'status'])
        for i in range(1, NUM_METERS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            writer.writerow([
                f'M{i:05d}',
                customer_id,
                fake.date_between(start_date='-10y', end_date='today'),
                random.choice(['Active', 'Inactive', 'Faulty'])
            ])

def generate_usage():
    with open('usage.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['usageID', 'meterID', 'date', 'kWh'])
        for i in range(1, NUM_USAGE+1):
            meter_id = f'M{random.randint(1, NUM_METERS):05d}'
            writer.writerow([
                f'U{i+10000}',
                meter_id,
                fake.date_between(start_date='-2y', end_date='today'),
                round(random.uniform(1, 100), 2)
            ])

def generate_outages():
    with open('outages.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['outageID', 'city', 'startDate', 'endDate', 'reason'])
        for i in range(1, NUM_OUTAGES+1):
            start_date = fake.date_between(start_date='-2y', end_date='today')
            end_date = start_date if random.random() < 0.7 else ''
            writer.writerow([
                f'O{i+20000}',
                fake.city(),
                start_date,
                end_date,
                fake.sentence(nb_words=5)
            ])

def generate_bills():
    with open('energy_bills.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['billID', 'customerID', 'amount', 'billDate', 'status'])
        for i in range(1, NUM_BILLS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            writer.writerow([
                f'B{i+30000}',
                customer_id,
                random.randint(50, 5000),
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['Paid', 'Unpaid', 'Pending'])
            ])

if __name__ == '__main__':
    generate_customers()
    generate_meters()
    generate_usage()
    generate_outages()
    generate_bills()
    print('Sample energy/utilities data generated!')
