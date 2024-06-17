import os
import random

def visualize():

    def guessnumber(guess,attempt):

        if(guess==number):
         print(f"you won,{number} is the number")
         return 0
            
        elif abs(number-guess)<10:
         print("you're too close to winning")
         return attempt-1
        
        elif(guess>(number)):
         print("too high")
         return attempt-1

        elif(guess<(number)):
         print("Too low")
         return attempt-1

    def value(attempt):
        print(f"you have {attempt} attempts to guess the number!")
        guess= int(input("Make a guess: "))
        attempt = guessnumber(guess=guess,attempt=attempt)
        return attempt

    guess=0
    isvalue = True
    while isvalue: 
        print("Welcome to he Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100: ")
        number = (random.randint(1,101))
        print(f"correct answer is {number}")

        level = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()


        if(level == "easy"):
            attempt = 10
            while(guess!=number):
                if (attempt>0):
                 attempt= value(attempt)
                else:
                 break
                


        elif(level=="hard"):
            attempt = 5
            while(guess!=number):
                if(attempt>0):
                    attempt=value(attempt)
                else:
                 break



        print(f"correct answer is {number}")
        print("--------------------------")
        play = input("Do you want to play again: type 'y' or 'n': ")
        if play=='y':
            isvalue=True
            os.system("cls")
        else:
            isvalue=False
#visualize()



print("saraswoti")
