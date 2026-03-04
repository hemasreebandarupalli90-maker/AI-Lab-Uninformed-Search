import random
import string

def generate_captcha(length=6):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

def run_captcha():
    captcha = generate_captcha()
    print("CAPTCHA:", captcha)

    user_input = input("Enter CAPTCHA: ")

    if user_input == captcha:
        print("Access Granted")
    else:
        print("Access Denied")

if __name__ == "__main__":
    run_captcha()
