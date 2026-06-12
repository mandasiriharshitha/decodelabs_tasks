import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("\n" + "=" * 50)
print("        RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:

    try:

        length = int(input("\nEnter Password Length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        choice = input("\nGenerate Another Password? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank You For Using Random Password Generator!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")