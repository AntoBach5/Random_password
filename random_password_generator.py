import time, random

numbers = "0123456789"
lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%&*()_+-=~\\:;\"<>,.?/"


def generate_password(complexity=1):
    print("\n\033[90mGenerating password...\033[0m")
    
    password = random.choice(numbers) + random.choice(lower_letters) + random.choice(upper_letters) + random.choice(symbols)
    password += ''.join(random.choices(numbers + lower_letters + upper_letters + symbols, k=8))
    
    if complexity >= 2:
        for i in range(complexity):
            password += ''.join(random.choices(numbers + lower_letters + upper_letters + symbols, k=8))
            time.sleep(0.75)
            
    print(f"\033[92mYour generated password is: {password}\033[0m\n")

while True:
    selection = input("\n\033[90mSelect complexity of the password (1-5): \033[0m")
    start = input("\033[90mPress enter to generate a random password \033[0m")
    if start == "":
        generate_password(int(selection))