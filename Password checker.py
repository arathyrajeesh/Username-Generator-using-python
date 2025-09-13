#Design a Password Strength Checker that evaluates a given password.


import re
def password_checker(password):
    
    if not password:
        print('you must enter a password')
        
    length=0
    error=[]
    
    if len(password)>=5:
        length +=1
    else:
        error.append("Password must be at least 8 characters")
        
    if re.search(r"[A-Z]",password):
        length+=1
    else:
        error.append("Add at least one uppercase letter.")
        
    if re.search(r"[a-z]",password):
        length+=1
    else:
        error.append("Add at least one lowercase letter.")
        
    if re.search(r"\d", password):
        length += 1
    else:
        error.append("Add at least one digit.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        length += 1
    else:
        error.append("Add at least one special character.")
    
    if length == 5:
        return " Strong Password!"
    elif length >= 3:
        return " Medium Strength Password. Suggestions: " + ", ".join(error)
    else:
        return " Weak Password. Suggestions: " + ", ".join(error)


a = input("Enter a password: ")
print(password_checker(a))
