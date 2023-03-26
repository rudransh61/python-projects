import random

def generatePassword(n):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

    password = ""

    for i in range(n):
        password += random.choice(characters)

    return password

n = 12
password = generatePassword(n)
print("A randomly selected password is:", password)