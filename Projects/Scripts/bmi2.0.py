
logo = """ 
 __         __                     
|__)|\/||  /   _ | _   | _ |_ _  _ 
|__)|  ||  \__(_||(_|_||(_||_(_)|                                   


"""

def calculate_bmi(height,weight):
	bmi = weight/height**2
	if bmi < 18.5:
	    print(f'BMI = {round(bmi,2)} are UNDERWEIGHT')
	elif bmi <= 25:
	    print(f'BMI = {round(bmi,2)} you have a normal weight')
	elif bmi <= 30:
	    print(f'BMI = {round(bmi,2)} you are slightly overweight')
	elif bmi <= 35:
	    print(f'BMI = {round(bmi,2)} you are obese')
	else:
	    print(f'BMI = {round(bmi,2)} you are clinically obese')


print(logo)

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
calculate_bmi(height,weight)




