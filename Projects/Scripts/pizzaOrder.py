# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pay = 0
if size == 'S':
    pay += 15

elif size == 'M':
    pay += 20

elif size == 'L':
    pay += 25

if add_pepperoni == 'Y':
    if size == 'S':
        pay += 2
    else:
        pay += 3

if extra_cheese == 'Y':
    pay += 1


print(f'Price order is ${pay}')
