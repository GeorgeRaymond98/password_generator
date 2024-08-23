# import librairies 
import random
import string

def generate_password(length: int = 10):#  function generate_password compares the length and give it a default value of 10
    alphabet = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(alphabet) for i in range(length)) # Joins the password string to random char from ascii, digits, and punctuation for how many char that was set(10) and create a new strong call password
    return password

for i in range(2):# a for loop that creates 2 random passwords
    password = generate_password() # Set the new value of generate_password
    print(f"Generated Password: {password}", i) # print the new generate_password which is sent to password 