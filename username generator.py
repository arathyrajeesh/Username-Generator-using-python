#Make a Username Generator from first and last names.

import random
def generator(first_name,last_name):
    
    first_name=first_name.lower()
    last_name=last_name.lower()
    
    first_name=first_name[:3]
    
    username = f"{first_name}{last_name}"
    username+=str(random.randint(10,99))
    
    return username

first=str(input('Enter first name: '))
last=str(input('Enter last name: '))
username=generator(first,last)
print(f" username for {first} {last}: {username}")
