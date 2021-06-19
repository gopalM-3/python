'''
    Application name: InteracLive
    Author: Gopal Matcha
    Date started working on: 23/04/2021
'''

import datetime
x = datetime.datetime.now()
print("Hey there! I'm !nteracLive")
name = input("Your name please?\n")
print("Nice to meet you,", name + "!")
yearob = int(input("Could you please tell me your year of birth?\n"))
print("Ohh! So, you're", x.year - yearob, "years old then... Nice!")
height = float(input("Give me your height in meters: "))
if height > 1.75:
    print("Damn! You're pretty tall ;-)")
weight = float(input("Please give me your weight in kilograms as well: "))
print("You're height and weight are", height, "metres and", weight, "kg respectively.")
BMI = (weight/(height*height))
print("Your Body Mass Index (BMI) is", BMI, "kg/m^2.")
if BMI < 18:
    print("You seem to be underweight, consider eating protein rich food and focus on strength training :-)")
elif BMI > 24:
    print("You seem to be overweight, consider avoiding fatty food and focus on cardio training :-)")
else:
    print("You seem to have a healthy lifestyle, focus on working out and continue the good work :-)")
country = input("Which country are you from?\n")
print(country, "seems like a pretty good place, you sure must be proud of your country.")
