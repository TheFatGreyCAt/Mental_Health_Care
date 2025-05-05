import csv
import random
from tqdm import tqdm

def generate_random_name():
    first_names = [
    "John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura",
    "Daniel", "Olivia", "James", "Sophia", "Matthew", "Emma", "Andrew", "Isabella", "Ryan", "Ava",
    "Joshua", "Mia", "Justin", "Charlotte", "Brandon", "Amelia", "Kevin", "Abigail", "Brian", "Ella",
    "Thomas", "Madison", "Nathan", "Lily", "Samuel", "Grace", "Zachary", "Chloe", "Benjamin", "Hannah",
    "Nicholas", "Natalie", "Anthony", "Zoe", "Jason", "Victoria", "Aaron", "Samantha", "Jacob", "Leah"
    ]

    last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez",
    "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
    "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez"
    ]

    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_date_of_birth():
    year = random.randint(1965, 2007) 
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"

def generate_patient_row(patient_id):
    gender = "Female" if random.random() < 0.65 else "Male"
    return [
        patient_id,
        generate_random_name(),
        generate_random_date_of_birth(),
        gender,
        random.choice(["Single", "Married"]),
        random.choice(["High School", "Bachelor's", "Master's", "PhD"]),
        random.randint(0, 5),
        random.choice(["Nurse", "Social Worker", "Firefighter", "Police Officer", "Paramedic", "Teacher", "Doctor", "Mental Health Counselor", "Veterinarian", "Customer Service Representative", "Journalist", "Lawyer", "Construction Worker", "Restaurant Worker", "Delivery Driver", "Artist", "Flight Attendant", "Military Personnel", "Telemarketer", "IT Professional", "Retail Worker", "Executive Manager", "Call Center Operator", "Farm Worker", "Bus Driver"]),
        f"${random.randint(20000, 150000):,}",
        patient_id
    ]

def generate_patients_data(file_name, a, b):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["PatientID", "FullName", "DateOfBirth", "Gender", "MaritalStatus", "EducationLevel", "NumberOfChildren", "Occupation", "Income", "ContactID"])

        for patient_id in tqdm(range(a, b + 1), desc="Generating patients data", unit="row"):
            writer.writerow(generate_patient_row(patient_id))

if __name__ == "__main__":
    output_file = "patients_data.csv"
    generate_patients_data(output_file, 20000001, 50000000)