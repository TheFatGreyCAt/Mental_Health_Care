import csv
import random
from tqdm import tqdm

def generate_random_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_address():
    streets = ["Main St", "High St", "Park Ave", "Oak St", "Pine St", "Maple Ave", "Cedar St", "Elm St", "Washington Ave", "Lake St"]
    street_number = random.randint(1, 9999)
    return f"{street_number} {random.choice(streets)}"

def generate_random_city():
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
    return random.choice(cities)

def generate_contact_row(row_id):
    name = generate_random_name()
    countries = [
        "United States", "Australia", "United Kingdom", "Canada", "France", "South Korea", "Japan", "Brazil", "India", "China"
    ]
    return [
        row_id,
        f"+{random.randint(1, 99)} {random.randint(1000000, 9999999)}",
        f"{name.lower().replace(' ', '.')}@gmail.com",
        generate_random_address(),
        generate_random_city(),
        random.choice(countries)
    ]

def generate_contact_data(file_name, a, b):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ContactID", "PhoneNumber", "Email", "Address", "City", "Country"])
        for i in tqdm(range(a, b + 1), desc="Generating contact data", unit="row"):
            writer.writerow(generate_contact_row(i))

if __name__ == "__main__":
    output_file = "contacts_data.csv"
    # generate_contact_data(output_file, 1, 20000000)
    generate_contact_data(output_file, 1, 7)