import csv
import random
from faker import Faker

fake = Faker()

NUM_STUDENTS = 3000
NUM_TEACHERS = 200
NUM_COURSES = 100
NUM_ENROLLMENTS = 6000
NUM_GRADES = 6000

def generate_teachers():
    with open('teachers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['teacherID', 'name', 'department', 'email', 'hireDate'])
        for i in range(1, NUM_TEACHERS+1):
            writer.writerow([
                f'T{i:04d}',
                fake.name(),
                random.choice(['Math', 'Science', 'History', 'English', 'Art', 'PE', 'Computer Science']),
                fake.email(),
                fake.date_between(start_date='-15y', end_date='today')
            ])

def generate_students():
    with open('students.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['studentID', 'name', 'age', 'gender', 'email', 'enrollDate'])
        for i in range(1, NUM_STUDENTS+1):
            writer.writerow([
                f'S{i:05d}',
                fake.name(),
                random.randint(16, 25),
                random.choice(['M', 'F']),
                fake.email(),
                fake.date_between(start_date='-5y', end_date='today')
            ])

def generate_courses():
    with open('courses.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['courseID', 'courseName', 'department', 'teacherID'])
        for i in range(1, NUM_COURSES+1):
            teacher_id = f'T{random.randint(1, NUM_TEACHERS):04d}'
            writer.writerow([
                f'C{i:03d}',
                fake.word().capitalize() + ' ' + random.choice(['101', '201', '301', 'Lab', 'Seminar']),
                random.choice(['Math', 'Science', 'History', 'English', 'Art', 'PE', 'Computer Science']),
                teacher_id
            ])

def generate_enrollments():
    with open('enrollments.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['enrollmentID', 'studentID', 'courseID', 'enrollDate'])
        for i in range(1, NUM_ENROLLMENTS+1):
            student_id = f'S{random.randint(1, NUM_STUDENTS):05d}'
            course_id = f'C{random.randint(1, NUM_COURSES):03d}'
            writer.writerow([
                f'E{i+10000}',
                student_id,
                course_id,
                fake.date_between(start_date='-5y', end_date='today')
            ])

def generate_grades():
    with open('grades.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['gradeID', 'enrollmentID', 'grade', 'gradeDate'])
        for i in range(1, NUM_GRADES+1):
            enrollment_id = f'E{random.randint(10001, 10000+NUM_ENROLLMENTS)}'
            writer.writerow([
                f'G{i+20000}',
                enrollment_id,
                random.choice(['A', 'B', 'C', 'D', 'F']),
                fake.date_between(start_date='-5y', end_date='today')
            ])

if __name__ == '__main__':
    generate_teachers()
    generate_students()
    generate_courses()
    generate_enrollments()
    generate_grades()
    print('Sample education data generated!')
