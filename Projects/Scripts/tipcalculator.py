
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print('Welcome to tip calculator!')
total = float(input('Whats was the total bill? $ '))
per = int(input('What percentage tip would you like to give 10, 12 or 15?\n'))
peoples = int(input('How many people to split the bill? \n'))

total_give = (1+per/100)*total
pay = total_give/peoples

print(f'Each peason should pay ${round(pay,2)}')