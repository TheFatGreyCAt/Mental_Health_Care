import csv
import random
from datetime import datetime
from tqdm import tqdm


notes_options = [
    "Advised medication.",
    "Follow-up scheduled.",
    "Referred to specialist.",
    "Check-up completed.",
    "Prescribed meds."
]

def random_date():
    year = random.randint(2000, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime(year, month, day)

def generate_hospital_visit_row(visit_id):
    visit_date = random_date()
    year = visit_date.year
    return [
        *[visit_id] * 8,
        visit_date.strftime("%Y-%m-%d"),
        random.choice(["Good", "Fair", "Poor"]),
        random.choice(notes_options),
        year
    ]

def generate_hospital_visit_data(file_name, start_id, end_id):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["VisitRecordID", "PatientID", "HealthHabitRecordID", "MentalAssessmentRecordID", "MentalHealthRecordID", "DigitalBehaviorRecordID", "EnvironmentSocialRecordID", "MedicalHistoryRecordID", "VisitDate", "GeneralHealthStatus", "Notes", "Year"])

        for i in tqdm(range(start_id, end_id + 1), desc="Generating hospital visit records"):
            writer.writerow(generate_hospital_visit_row(i))

if __name__ == "__main__":
    output_files = "hospital_visit_records_data3.csv"
    visit_id_s = 1 + 20000000 + 20000000
    visit_id_e = 20000000 + 20000000 + 10000000
    generate_hospital_visit_data(output_files, visit_id_s, visit_id_e)
    

