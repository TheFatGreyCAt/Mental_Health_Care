import csv
import random
from tqdm import tqdm

def generate_digital_activity_row():
    return [
        random.choice(["Rarely", "Sometimes", "Often"]),
        random.choice(["Never", "Occasionally", "Regularly"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"])
    ]

def generate_digital_activity_data(file_name, a, b):

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["DigitalBehaviorRecordID", "VirtualCommunicationFrequency", "DigitalDetoxFrequency", "OnlineParticipation", "SocialMediaAddictionLevel"])
        for i in tqdm(range(a, b + 1), desc="Generating digital activity data", unit="row"):
            writer.writerow([i] + generate_digital_activity_row())

if __name__ == "__main__":
    output_file = "digital_activity_data.csv"
    generate_digital_activity_data(output_file, 1, 50000000)