import random

# 8. Generate random 4 digits number of 0s and 1s and convert the generated number to base 10
def generate_random_binary():
    binary_number = ''.join(random.choice('01') for _ in range(4))
    base_10_number = int(binary_number, 2)
    return binary_number, base_10_number

if __name__ == "__main__":
    binary_number, base_10_number = generate_random_binary()
    print(f"Generated binary number: {binary_number}")
    print(f"Converted to base 10: {base_10_number}")