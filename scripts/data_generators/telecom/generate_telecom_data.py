import csv
import random
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 3500
NUM_PLANS = 1000
NUM_CALLS = 12000
NUM_BILLS = 3000
NUM_COMPLAINTS = 800

def generate_customers():
    with open('telecom_customers.csv', 'w', newline='') as f:
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

def generate_plans():
    with open('telecom_plans.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['planID', 'planName', 'type', 'monthlyFee', 'dataLimitGB'])
        for i in range(1, NUM_PLANS+1):
            writer.writerow([
                f'PL{i:04d}',
                fake.word().capitalize(),
                random.choice(['Prepaid', 'Postpaid']),
                random.randint(100, 2000),
                random.randint(1, 200)
            ])

def generate_calls():
    with open('telecom_calls.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['callID', 'customerID', 'planID', 'callDate', 'durationMin', 'callType'])
        for i in range(1, NUM_CALLS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            plan_id = f'PL{random.randint(1, NUM_PLANS):04d}'
            writer.writerow([
                f'CA{i+10000}',
                customer_id,
                plan_id,
                fake.date_between(start_date='-2y', end_date='today'),
                random.randint(1, 60),
                random.choice(['Local', 'STD', 'ISD'])
            ])

def generate_bills():
    with open('telecom_bills.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['billID', 'customerID', 'amount', 'billDate', 'status'])
        for i in range(1, NUM_BILLS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            writer.writerow([
                f'B{i+20000}',
                customer_id,
                random.randint(100, 5000),
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['Paid', 'Unpaid', 'Pending'])
            ])

def generate_complaints():
    with open('telecom_complaints.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['complaintID', 'customerID', 'date', 'issue', 'status'])
        for i in range(1, NUM_COMPLAINTS+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            writer.writerow([
                f'CP{i+30000}',
                customer_id,
                fake.date_between(start_date='-1y', end_date='today'),
                fake.sentence(nb_words=5),
                random.choice(['Open', 'Closed', 'In Progress'])
            ])

if __name__ == '__main__':
    generate_customers()
    generate_plans()
    generate_calls()
    generate_bills()
    generate_complaints()
    print('Sample telecom data generated!')
