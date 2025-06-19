import csv
import random
from faker import Faker

fake = Faker()

NUM_PROPERTIES = 1000
NUM_AGENTS = 200
NUM_LISTINGS = 1200
NUM_VIEWINGS = 2500
NUM_TRANSACTIONS = 800

def generate_agents():
    with open('agents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['agentID', 'name', 'email', 'phone', 'agency'])
        for i in range(1, NUM_AGENTS+1):
            writer.writerow([
                f'A{i:04d}',
                fake.name(),
                fake.email(),
                fake.phone_number(),
                fake.company()
            ])

def generate_properties():
    with open('properties.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['propertyID', 'address', 'city', 'type', 'price', 'status'])
        for i in range(1, NUM_PROPERTIES+1):
            writer.writerow([
                f'P{i:05d}',
                fake.address().replace('\n', ', '),
                fake.city(),
                random.choice(['Apartment', 'House', 'Condo', 'Land']),
                random.randint(50000, 2000000),
                random.choice(['Available', 'Sold', 'Rented'])
            ])

def generate_listings():
    with open('listings.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['listingID', 'propertyID', 'agentID', 'listDate', 'status'])
        for i in range(1, NUM_LISTINGS+1):
            property_id = f'P{random.randint(1, NUM_PROPERTIES):05d}'
            agent_id = f'A{random.randint(1, NUM_AGENTS):04d}'
            writer.writerow([
                f'L{i+10000}',
                property_id,
                agent_id,
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['Active', 'Inactive', 'Closed'])
            ])

def generate_viewings():
    with open('viewings.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['viewingID', 'listingID', 'date', 'clientName'])
        for i in range(1, NUM_VIEWINGS+1):
            listing_id = f'L{random.randint(10001, 10000+NUM_LISTINGS)}'
            writer.writerow([
                f'V{i+20000}',
                listing_id,
                fake.date_between(start_date='-2y', end_date='today'),
                fake.name()
            ])

def generate_transactions():
    with open('transactions.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['transactionID', 'propertyID', 'agentID', 'date', 'amount', 'type'])
        for i in range(1, NUM_TRANSACTIONS+1):
            property_id = f'P{random.randint(1, NUM_PROPERTIES):05d}'
            agent_id = f'A{random.randint(1, NUM_AGENTS):04d}'
            writer.writerow([
                f'T{i+30000}',
                property_id,
                agent_id,
                fake.date_between(start_date='-2y', end_date='today'),
                random.randint(50000, 2000000),
                random.choice(['Sale', 'Rent'])
            ])

if __name__ == '__main__':
    generate_agents()
    generate_properties()
    generate_listings()
    generate_viewings()
    generate_transactions()
    print('Sample real estate data generated!')
