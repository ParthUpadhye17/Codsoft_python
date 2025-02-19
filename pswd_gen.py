import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),  
        random.choice(string.ascii_uppercase),  
        random.choice(string.digits),           
        random.choice(string.punctuation)       
    ]
    
    password += random.choices(all_characters, k=length-4)
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 8 characters): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    password = generate_password(length)
    print(f"generated password is: {password}")

if __name__ == "__main__":
    main()
