#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

logo = """ 


______     ______                                   _   _____                           _             
| ___ \    | ___ \                                 | | |  __ \                         | |            
| |_/ /   _| |_/ /_ _ ___ _____      _____  _ __ __| | | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ | | |  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |  | |_| | | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_|   \__, \_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
       __/ |                                                                                          
      |___/                                                                                           
 

"""

print(logo)
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password: ")) 
nr_symbols = int(input(f"How many symbols would you like: "))
nr_numbers = int(input(f"How many numbers would you like: "))

password_list = []
for letter in range(0,nr_letters):
    password_list.append(random.choice(letters)) 
   
for symbol in range(0,nr_symbols):
    password_list += random.choice(symbols)
    
for number in range(0,nr_numbers):
    password_list += random.choice(numbers)
    

random.shuffle(password_list)


password = ""
for char in password_list:
    password += char

print(f'Your password is - {password}')

print('\n')



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
