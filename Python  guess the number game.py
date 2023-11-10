#Guess the number
import random

max_num=30
random_num=random.randint(1, max_num)
guess=0
while guess!=random_num:
    guess= int(input(f"Guess a number between 1 & {max_num}: "))
    if guess< random_num:
        print("Wrong! Go higher")
    elif guess> random_num:
        print("Wrong! Go lower")
    else:
        print("Purrrrrrfect! The random number is", random_num)