import random

number = random.randint(1,100)
while True:
    guess_num = int(input("Guess a number:"))
    if(number < guess_num):
        print("Guess low number")
    elif(number > guess_num):
        print("Guess high number")
    elif(number == guess_num):
        print("Hurrah! You guess it right")
        break

