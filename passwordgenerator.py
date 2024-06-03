import random

def generate_password(length):
    if length < 1:
        raise ValueError("Password length should be at least 1")

    
    letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    characters = letters_upper + letters_lower + digits + punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":
    
    desired_length = int(input("Enter the desired password length: "))
    password = generate_password(desired_length)
    print(f"Generated password: {password}")
