import csv
import random
from tqdm import tqdm

def generate_medical_history_row(row_id):
    return [
        row_id,
        random.choice([0, 1]),
        random.choice([0, 1]),
        random.choice(["None", "Diabetes", "Hypertension", "Cardiovascular", "Asthma", "Multiple"]),
        random.choice(["None", "Food", "Medication", "Environmental", "Multiple"]),
        random.randint(0, 10),
        random.choice(["None", "Epilepsy", "Parkinson's", "MultipleSclerosis", "Migraines", "Other"]),
    ]

def generate_medical_history_data(file_name, a, b):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["MedicalHistoryRecordID", "FamilyHistoryOfDepression", "HistoryOfSubstanceAbuse", 
                        "ChronicDiseases", "Allergies", "PsychiatricHospitalizations", "NeurologicalDisorders"])
        for row_id in tqdm(range(a, b + 1), desc="Generating medical history data", unit="row"):
            writer.writerow(generate_medical_history_row(row_id))

if __name__ == "__main__":
    output_file = "medical_history_data.csv"
    generate_medical_history_data(output_file, 1, 50000000)