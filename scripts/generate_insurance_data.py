import csv
import random
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 5000
NUM_POLICIES = 8000
NUM_CLAIMS = 5000
NUM_AGENTS = 500
NUM_PAYMENTS = 2000

# Generate agents.csv
def generate_agents():
    with open('agents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['agentID', 'name', 'region', 'hireDate', 'email'])
        for i in range(1, NUM_AGENTS+1):
            writer.writerow([
                f'A{i:03d}',
                fake.name(),
                fake.city(),
                fake.date_between(start_date='-10y', end_date='today'),
                fake.email()
            ])

def generate_customers():
    with open('customers.csv', 'w', newline='') as f:
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

def generate_policies():
    with open('policies.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['policyID', 'customerID', 'policyType', 'premium', 'issueDate', 'status', 'coverageAmount', 'agentID'])
        for i in range(1, NUM_POLICIES+1):
            customer_id = f'C{random.randint(1, NUM_CUSTOMERS):04d}'
            agent_id = f'A{random.randint(1, NUM_AGENTS):03d}'
            writer.writerow([
                f'P{i+10000}',
                customer_id,
                random.choice(['Life', 'Health', 'Auto', 'Home', 'Travel']),
                random.randint(300, 5000),
                fake.date_between(start_date='-5y', end_date='today'),
                random.choice(['Active', 'Lapsed', 'Expired']),
                random.randint(10000, 500000),
                agent_id
            ])

def generate_claims():
    with open('claims.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['claimID', 'policyID', 'claimAmount', 'claimDate', 'claimStatus', 'description', 'payoutDate'])
        for i in range(1, NUM_CLAIMS+1):
            policy_id = f'P{random.randint(10001, 10000+NUM_POLICIES)}'
            status = random.choice(['Open', 'Closed', 'Rejected'])
            payout_date = fake.date_between(start_date='-2y', end_date='today') if status == 'Closed' else ''
            writer.writerow([
                f'CL{i+20000}',
                policy_id,
                random.randint(500, 20000),
                fake.date_between(start_date='-3y', end_date='today'),
                status,
                fake.sentence(nb_words=4),
                payout_date
            ])

def generate_payments():
    with open('payments.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['paymentID', 'policyID', 'amount', 'paymentDate', 'method', 'status'])
        for i in range(1, NUM_PAYMENTS+1):
            policy_id = f'P{random.randint(10001, 10000+NUM_POLICIES)}'
            writer.writerow([
                f'PAY{i+30000}',
                policy_id,
                random.randint(300, 5000),
                fake.date_between(start_date='-5y', end_date='today'),
                random.choice(['Credit', 'Debit', 'Bank Transfer']),
                random.choice(['Success', 'Failed'])
            ])

if __name__ == '__main__':
    generate_agents()
    generate_customers()
    generate_policies()
    generate_claims()
    generate_payments()
    print('Sample insurance company data generated!')
