import random
import time

def generate_random_number():
    while True:
        num = random.randint(1, 20)
        print(f"Generated number: {num}")
        time.sleep(10)  # Sleep for 10 seconds
        yield num

# This part is to ensure that when this script is run directly, it starts generating numbers.
if __name__ == "__main__":
    for number in generate_random_number():
        continue
