import csv
import random
from tqdm import tqdm

def generate_mental_assessment_row():
    return [
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"])
    ]

def generate_mental_assessment_data(file_name, a, b):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["MentalAssessmentRecordID", "AnxietyLevel", "BurnoutLevel",
                        "DepressionLevel", "StressLevel", "SelfEsteemLevel"])
        for i in tqdm(range(a, b + 1), desc="Generating mental assessment data", unit="row"):
            writer.writerow([i] + generate_mental_assessment_row())

if __name__ == "__main__":
    output_file = "mental_assessment_data.csv"
    generate_mental_assessment_data(output_file, 1, 50000000)