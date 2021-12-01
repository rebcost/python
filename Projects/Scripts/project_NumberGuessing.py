logo = """ 


 _______           _______  _       _________ _______    _______  _______ _________ _______   
(  ___  )|\     /|(  ____ \( (    /|\__   __/(  ____ \  (  ____ \(  ____ )\__   __/(  ___  )  
| (   ) || )   ( || (    \/|  \  ( |   ) (   | (    \/  | (    \/| (    )|   ) (   | (   ) |  
| |   | || |   | || (__    |   \ | |   | |   | (__      | (__    | (____)|   | |   | |   | |  
| |   | || |   | ||  __)   | (\ \) |   | |   |  __)     |  __)   |     __)   | |   | |   | |  
| | /\| || |   | || (      | | \   |   | |   | (        | (      | (\ (      | |   | |   | |  
| (_\ \ || (___) || (____/\| )  \  |   | |   | (____/\  | )      | ) \ \_____) (___| (___) |  
(____\/_)(_______)(_______/|/    )_)   )_(   (_______/  |/       |/   \__/\_______/(_______)  
                                                                                              


"""

import random

def game(chance):
    print(f"You have {chance} attempts remaning to guess the number.")
    
    num_sorteado = random.randint(1, 20)
    num_escolhido = 0
    #print(f"Num sor = {num_sorteado}")
    while True: 
        num_escolhido = int(input("Make a guess: "))
        if num_sorteado != num_escolhido:
            print("Too high" if num_escolhido > num_sorteado else "Too Low")            
            chance -= 1            
            if chance == 0:
                print("You lose!")
                break
        else:
            print(f"You got it! The answer was {num_sorteado}")  
            break      

#Programa pricipal
print(logo)
print("Wellcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 20!")
dificuldade = ""
while True:
    dificuldade = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dificuldade == "easy" or dificuldade == "hard":
        break

if dificuldade == 'easy':
    chance = 10
else:   
    chance = 5

game(chance)
