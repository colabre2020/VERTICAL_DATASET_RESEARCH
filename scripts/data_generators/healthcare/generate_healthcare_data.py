import csv
import random
from faker import Faker

fake = Faker()

NUM_PATIENTS = 3000
NUM_DOCTORS = 300
NUM_APPOINTMENTS = 6000
NUM_PRESCRIPTIONS = 4000
NUM_BILLS = 2000

def generate_doctors():
    with open('doctors.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['doctorID', 'name', 'specialty', 'email', 'phone'])
        for i in range(1, NUM_DOCTORS+1):
            writer.writerow([
                f'DR{i:04d}',
                fake.name(),
                random.choice(['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'General']),
                fake.email(),
                fake.phone_number()
            ])

def generate_patients():
    with open('patients.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['patientID', 'name', 'age', 'gender', 'city', 'email', 'phone'])
        for i in range(1, NUM_PATIENTS+1):
            writer.writerow([
                f'PT{i:04d}',
                fake.name(),
                random.randint(0, 100),
                random.choice(['M', 'F']),
                fake.city(),
                fake.email(),
                fake.phone_number()
            ])

def generate_appointments():
    with open('appointments.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['appointmentID', 'patientID', 'doctorID', 'date', 'status'])
        for i in range(1, NUM_APPOINTMENTS+1):
            patient_id = f'PT{random.randint(1, NUM_PATIENTS):04d}'
            doctor_id = f'DR{random.randint(1, NUM_DOCTORS):04d}'
            writer.writerow([
                f'AP{i+10000}',
                patient_id,
                doctor_id,
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['Scheduled', 'Completed', 'Cancelled'])
            ])

def generate_prescriptions():
    with open('prescriptions.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['prescriptionID', 'appointmentID', 'medicine', 'dosage', 'duration'])
        for i in range(1, NUM_PRESCRIPTIONS+1):
            appointment_id = f'AP{random.randint(10001, 10000+NUM_APPOINTMENTS)}'
            writer.writerow([
                f'PR{i+20000}',
                appointment_id,
                fake.word().capitalize(),
                f"{random.randint(1,3)} tablets/day",
                f"{random.randint(3,30)} days"
            ])

def generate_bills():
    with open('bills.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['billID', 'patientID', 'amount', 'date', 'status'])
        for i in range(1, NUM_BILLS+1):
            patient_id = f'PT{random.randint(1, NUM_PATIENTS):04d}'
            writer.writerow([
                f'BL{i+30000}',
                patient_id,
                random.randint(100, 10000),
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['Paid', 'Unpaid', 'Pending'])
            ])

if __name__ == '__main__':
    generate_doctors()
    generate_patients()
    generate_appointments()
    generate_prescriptions()
    generate_bills()
    print('Sample healthcare data generated!')
