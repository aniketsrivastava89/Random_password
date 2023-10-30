import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length should be greater than 0.")
            return

        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
