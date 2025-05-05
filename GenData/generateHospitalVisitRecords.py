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

def generate_hospital_visit_row(patient_id, visit_id, record_count):
    visit_date = random_date()
    year = visit_date.year
    return [
        visit_id,
        patient_id,
        *[visit_id] * 6,
        visit_date.strftime("%Y-%m-%d"),
        random.choice(["Good", "Fair", "Poor"]),
        random.choice(notes_options),
        year
    ]

def generate_hospital_visit_data(file_name, start_patient_id, end_patient_id, start_visit_id):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["VisitRecordID", "PatientID", "HealthHabitRecordID", "MentalAssessmentRecordID", "MentalHealthRecordID", "DigitalBehaviorRecordID", "EnvironmentSocialRecordID", "MedicalHistoryRecordID", "VisitDate", "GeneralHealthStatus", "Notes", "Year"])

        patient_id = start_patient_id
        visit_id = start_visit_id

        for _ in tqdm(range(start_patient_id, end_patient_id + 1), desc="Generating hospital visit records"):
            record_count = random.randint(1, 5)

            for _ in range(record_count):
                writer.writerow(generate_hospital_visit_row(patient_id, visit_id, record_count))
                visit_id += 1

            patient_id += 1

    return visit_id

if __name__ == "__main__":
    output_files = [
        f"hospital_visit_records_data{i}.csv" for i in range(1, 5)
    ]

    # patient_ranges = [
    #     (1, 5000000),
    #     (5000001, 10000000),
    #     (10000001, 15000000),
    #     (15000001, 20000000)
    # ]

    patient_ranges = [ (1,5) ]

    last_visit_id = 1
    for output_file, (start_patient_id, end_patient_id) in zip(output_files, patient_ranges):
        last_visit_id = generate_hospital_visit_data(output_file, start_patient_id, end_patient_id, last_visit_id)

