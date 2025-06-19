import csv
import random
from faker import Faker

fake = Faker()

NUM_VEHICLES = 500
NUM_DRIVERS = 300
NUM_ROUTES = 200
NUM_SHIPMENTS = 4000
NUM_INCIDENTS = 500

def generate_vehicles():
    with open('vehicles.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['vehicleID', 'type', 'plateNumber', 'capacity', 'status'])
        for i in range(1, NUM_VEHICLES+1):
            writer.writerow([
                f'V{i:04d}',
                random.choice(['Truck', 'Van', 'Car', 'Bike', 'Bus']),
                fake.license_plate(),
                random.randint(1, 40),
                random.choice(['Active', 'Maintenance', 'Inactive'])
            ])

def generate_drivers():
    with open('drivers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['driverID', 'name', 'licenseNumber', 'hireDate', 'status'])
        for i in range(1, NUM_DRIVERS+1):
            writer.writerow([
                f'DR{i:04d}',
                fake.name(),
                fake.license_plate(),
                fake.date_between(start_date='-10y', end_date='today'),
                random.choice(['Active', 'Suspended', 'Retired'])
            ])

def generate_routes():
    with open('routes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['routeID', 'origin', 'destination', 'distance_km'])
        for i in range(1, NUM_ROUTES+1):
            writer.writerow([
                f'R{i:03d}',
                fake.city(),
                fake.city(),
                random.randint(10, 2000)
            ])

def generate_shipments():
    with open('shipments.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['shipmentID', 'vehicleID', 'driverID', 'routeID', 'date', 'status'])
        for i in range(1, NUM_SHIPMENTS+1):
            vehicle_id = f'V{random.randint(1, NUM_VEHICLES):04d}'
            driver_id = f'DR{random.randint(1, NUM_DRIVERS):04d}'
            route_id = f'R{random.randint(1, NUM_ROUTES):03d}'
            writer.writerow([
                f'SH{i+10000}',
                vehicle_id,
                driver_id,
                route_id,
                fake.date_between(start_date='-2y', end_date='today'),
                random.choice(['In Transit', 'Delivered', 'Delayed', 'Cancelled'])
            ])

def generate_incidents():
    with open('incidents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['incidentID', 'shipmentID', 'date', 'description', 'severity'])
        for i in range(1, NUM_INCIDENTS+1):
            shipment_id = f'SH{random.randint(10001, 10000+NUM_SHIPMENTS)}'
            writer.writerow([
                f'IN{i+20000}',
                shipment_id,
                fake.date_between(start_date='-2y', end_date='today'),
                fake.sentence(nb_words=6),
                random.choice(['Low', 'Medium', 'High'])
            ])

if __name__ == '__main__':
    generate_vehicles()
    generate_drivers()
    generate_routes()
    generate_shipments()
    generate_incidents()
    print('Sample transportation data generated!')
