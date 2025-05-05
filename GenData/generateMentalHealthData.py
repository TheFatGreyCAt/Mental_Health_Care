import csv
import random
from tqdm import tqdm

def generate_mental_health_row(row_id):
    return [
        row_id,
        random.choice(["Depression", "Anxiety", "Bipolar Disorder", "Schizophrenia", "PTSD", "OCD", "ADHD", "Autism Spectrum Disorder", "Substance Use Disorder", "Insomnia Disorder"]),
        random.choice(["Therapy", "Medication", "Combined", "None"]),
        random.randint(0, 15),
        random.choice(["Mild", "Moderate", "Severe"]),
        random.choice(["None", "Childhood Trauma", "Abuse", "Accident", "Multiple"]),
        random.choice(["Adherent", "Non-Adherent"]),
        random.choice(["Yes", "No"])
    ]

def generate_mental_health_data(file_name, a, b):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["MentalHealthRecordID", "MentalHealthDiagnosis", "TreatmentType", 
                        "TherapySessionsCount", "SeverityLevelOfDiagnosis", "TraumaHistory", "MedicationAdherence", "RelapseHistory"])
        for row_id in tqdm(range(a, b + 1), desc="Generating mental health data", unit="row"):
            writer.writerow(generate_mental_health_row(row_id))

if __name__ == "__main__":
    output_file = "mental_health_data.csv"
    generate_mental_health_data(output_file, 1, 50000000)