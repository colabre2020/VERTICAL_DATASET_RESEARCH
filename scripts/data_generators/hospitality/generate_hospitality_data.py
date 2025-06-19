import csv
import random
from faker import Faker

fake = Faker()

NUM_HOTELS = 100
NUM_GUESTS = 2000
NUM_ROOMS = 1000
NUM_BOOKINGS = 4000
NUM_SERVICES = 3000

def generate_hotels():
    with open('hotels.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['hotelID', 'name', 'city', 'address', 'stars'])
        for i in range(1, NUM_HOTELS+1):
            writer.writerow([
                f'H{i:03d}',
                fake.company(),
                fake.city(),
                fake.address().replace('\n', ', '),
                random.randint(1, 5)
            ])

def generate_guests():
    with open('guests.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['guestID', 'name', 'email', 'phone', 'city'])
        for i in range(1, NUM_GUESTS+1):
            writer.writerow([
                f'G{i:05d}',
                fake.name(),
                fake.email(),
                fake.phone_number(),
                fake.city()
            ])

def generate_rooms():
    with open('rooms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['roomID', 'hotelID', 'roomType', 'price', 'status'])
        for i in range(1, NUM_ROOMS+1):
            hotel_id = f'H{random.randint(1, NUM_HOTELS):03d}'
            writer.writerow([
                f'R{i:04d}',
                hotel_id,
                random.choice(['Single', 'Double', 'Suite', 'Deluxe']),
                random.randint(50, 1000),
                random.choice(['Available', 'Occupied', 'Maintenance'])
            ])

def generate_bookings():
    with open('bookings.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['bookingID', 'guestID', 'roomID', 'checkIn', 'checkOut', 'status'])
        for i in range(1, NUM_BOOKINGS+1):
            guest_id = f'G{random.randint(1, NUM_GUESTS):05d}'
            room_id = f'R{random.randint(1, NUM_ROOMS):04d}'
            check_in = fake.date_between(start_date='-2y', end_date='today')
            check_out = check_in if random.random() < 0.8 else ''
            writer.writerow([
                f'B{i+10000}',
                guest_id,
                room_id,
                check_in,
                check_out,
                random.choice(['Confirmed', 'Checked In', 'Checked Out', 'Cancelled'])
            ])

def generate_services():
    with open('services.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['serviceID', 'bookingID', 'serviceType', 'amount', 'date'])
        for i in range(1, NUM_SERVICES+1):
            booking_id = f'B{random.randint(10001, 10000+NUM_BOOKINGS)}'
            writer.writerow([
                f'S{i+20000}',
                booking_id,
                random.choice(['Room Service', 'Spa', 'Laundry', 'Restaurant', 'Transport']),
                random.randint(10, 500),
                fake.date_between(start_date='-2y', end_date='today')
            ])

if __name__ == '__main__':
    generate_hotels()
    generate_guests()
    generate_rooms()
    generate_bookings()
    generate_services()
    print('Sample hospitality data generated!')
