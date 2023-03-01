#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Taking inputs from the User
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total=nr_letters+nr_numbers+nr_symbols

# Taking random character from the list letters and make a string
nletter=""
for l in range(0,nr_letters):
    naletter=random.choice(letters)
    nletter+=naletter

# Taking random numbers from the list numbers and make a string
nnumber=""
for n in range(0,nr_numbers):
    nanumber=random.choice(numbers)
    nnumber+=nanumber

# Taking random symbols from the list of sybols and make a string.
nsymbols=""
for s in range(0,nr_symbols):
    nasymbol=random.choice(symbols)
    nsymbols+=nasymbol
    
# Cancatinate all the string and make a list 
password=nletter+nnumber+nsymbols
password1=[]
for i in password:
    password1.append(i)

# Shuffle the list passord
random.shuffle(password1)

# Cancantenate all the items of the list in the string and generate password
password3=""
for i in password1:
    password3+=i
print("Your securely generated Password is ",password3)