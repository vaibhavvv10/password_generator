import string 
import random


def generate_password(len_min,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters=letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    pwd=""
    meets_criteria= False
    has_numbers = False
    has_special = False
    
    while not meets_criteria or len(pwd)<len_min:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria=has_numbers
        if special_characters:
            meets_criteria=has_special and meets_criteria
            
    
    return pwd


len_pwd = int(input("enter the length of the password: "))
has_number = input("Do u want no in password(y/n) :").lower() == "y"
has_special = input("Do u want special characters in password(y/n)? :").lower() == "y"
password= generate_password(len_pwd,has_number,has_special)
print(password)
