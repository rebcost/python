import random
from time import sleep

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
jokenpo = [rock,paper,scissors]
user_choice = int(input('What do you choose. Type: \n 0 for Rock, \n 1 for Paper \n 2 for scissors\n'))
computer_choice = random.randint(0,2)

if user_choice > 2 or user_choice < 0:
    print('Error!!! Type another number!')    
    exit()
else: 
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO\n")
    sleep(1)

    print(f'You choose {jokenpo[user_choice]}')
    print(f'Computer choose {jokenpo[computer_choice]}')

    if user_choice == 0:
        if computer_choice == 2:
            print('You Win!')
        elif computer_choice == 0:
            print('Draw')
        else:
            print('You lose')

    if user_choice == 1:
        if computer_choice == 0:
            print('You Win!')
        elif computer_choice == 1:
            print('Draw')
        else:
            print('You Lose')

    if user_choice == 2:
        if computer_choice == 1:
            print('You Win!')
        elif computer_choice == 2:
            print('Draw')
        else:
            print('You lose')