import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


want_letter = input('Do you wanna have any letter in your password?\n').lower()
want_number = input('Do you wanna have any number in your password?\n').lower()
want_symbol = input('Do you wanna have any symbol in your password?\n').lower()

if want_letter == 'yes':
    how_many_letter = int(input('How many letter do you want in your password?\n'))
else:
    how_many_letter = 0
    

if want_number == 'yes':
    how_many_number = int(input('How many number do you want in your password?\n'))
else:
    how_many_number = 0
    

if want_symbol == 'yes':
    how_many_symbol = int(input('How many symbol do you want in your password?\n'))
else:
    how_many_symbol = 0
    
    
password = ''

for letter in range(how_many_letter):
    random_letter = random.choice(letters)
    password += random_letter
    
for number in range(how_many_number):
    random_number = random.choice(numbers)
    password += random_number
    
for symbol in range(how_many_symbol):
    random_symbol = random.choice(symbols)
    password += random_symbol
    

print(password)


mixed_password = list(password)

random.shuffle(mixed_password)

# mixed_password = str(mixed_password)

mixed_password = ''.join(mixed_password)

print(mixed_password)