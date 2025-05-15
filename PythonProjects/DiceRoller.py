print("Are you exited to guess the dice roll num:")

import random
num = random.randint(1,6)
while True:
    guess = int(input("Guess the dice roll number from 1 to 6:"))
    if(guess > num):
        print("Guess low number!")
    if(guess < num):
        print("Guess high number")
    if(guess == num):
        print("hurrah! you guess it correctly")
    
