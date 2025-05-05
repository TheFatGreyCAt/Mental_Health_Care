import csv
import random
from tqdm import tqdm

def generate_health_habits_row():
    return [
        random.choice(["Non-Smoker", "Occasional Smoker", "Regular Smoker"]),
        random.choice(["Sedentary", "Moderately Active", "Very Active"]),
        random.choice(["None", "Moderate", "High"]),
        random.choice(["Healthy", "Unhealthy", "Vegetarian", "IrregularMeals"]),
        random.choice(["Regular", "Irregular", "Insufficient", "Oversleeping"]),
        random.choice(["Light", "Moderate", "Heavy", "Addicted"]),
        random.randint(0, 16),
        random.choice(["Rarely", "Sometimes", "Often"])
    ]

def generate_health_habits_data(file_name, a, b):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["HealthHabitsRecordID", "SmokingStatus", "PhysicalActivityLevel", 
                        "AlcoholConsumption", "DietaryHabits", "SleepPatterns", "SocialMediaUsage", "WorkingHours", "GamingFrequency"])
        for i in tqdm(range(a, b + 1), desc="Generating health habits data"):
            writer.writerow([i] + generate_health_habits_row())

if __name__ == "__main__":
    output_file = "health_habits_data1.csv"
    generate_health_habits_data(output_file, 1, 5)