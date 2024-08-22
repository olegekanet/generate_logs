import time
import random
from faker import Faker

fake = Faker()

log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

def generate_log():
    timestamp = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    log_level = random.choice(log_levels)
    message = fake.sentence()
    return f"{timestamp} - {log_level} - {message}"

if __name__ == "__main__":
    while True:
        print(generate_log())
        time.sleep(random.uniform(0.5, 2))  # Случайная пауза между логами
