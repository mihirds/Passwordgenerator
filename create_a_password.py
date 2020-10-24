import random

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?'

number = int(input('number of passwords wanted: '))
length = int(input('Password length? '))

for i in range(number):
    password = ''
    for j in range(length):
        password += random.choice(characters)
    print(password)
    
