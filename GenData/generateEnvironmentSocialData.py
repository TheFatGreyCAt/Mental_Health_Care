import csv
import random
from tqdm import tqdm

def generate_environment_social_row():
    return [
        random.choice(["Poor", "Average", "Good"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Poor", "Average", "Good"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"]),
        random.choice(["Low", "Medium", "High"])
    ]

def generate_environment_social_data(file_name, a, b):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["EnvironmentSocialRecordID", "LivingConditions", "CommunityEngagement",
                        "PeerPressureLevel", "WorkLifeBalance", "ExposureToNews", "FamilySupportLevel", "WorkplaceStressLevel"])
        for i in tqdm(range(a, b + 1), desc="Generating environment social data", unit="row"):
            writer.writerow([i] + generate_environment_social_row())

if __name__ == "__main__":
    output_file = "environment_social_data.csv"
    generate_environment_social_data(output_file, 1, 50000000)