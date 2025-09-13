import random

def generator(first_name, last_name):
    first_name = first_name.lower()[:3]   
    last_name = last_name.lower()

    username = f"{first_name}{last_name}"
    username += str(random.randint(10, 99))  
    username += random.choice(['@', '/', '$'])  

    return username

first = input('Enter first name: ')
last = input('Enter last name: ')
username = generator(first, last)
print(f"Username for {first} {last}: {username}")
