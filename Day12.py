import math
import random
import string
import os

# def scope(new):
#     # print(f"{test}")
#     val=12
#     if(val>10):
#         new = 12
#     # print(val)

# scope(5)
# print(new)

#modifing global scope
# PI = 3.14 
# sara = 15
# PI = sara
# print(PI)

##project--------number guessing game
#easy-10attempts
#hard-5attempts
#solution
#1.random number
#for loop <11 for easy, <5 for hard
#if guess>hamronumber,too high..g<hamronumber,too low,if g==hamronumber+1,-1 too close,
#if out of chances , run again play again

def guessnumber(guess):

    if(guess==number):
     return f"you won,{number} is the number"
    
    elif abs(number-guess)<10:
     return "you're too close to winning"
    
    elif(guess>(number)):
     return "too high"

    elif(guess<(number)):
     return "Too low"


isvalue = True
while isvalue: 
    print("Welcome to he Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100: ")
    number = (random.randint(1,101))
    print(f"correct answer is {number}")

    level = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    if(level == "easy"):
        attempt = 10
        print(f"you have 10 attempts to guess the number!")
        while(attempt>0):
            guess= int(input("Make a guess: "))
            final = guessnumber(guess)
            print(f"you have {attempt} attempts to guess the number!")
            print(f"{final}")
            if final == f"you won,{number} is the number":
             break
            attempt= attempt-1
            

    elif(level=="hard"):
        attempt = 5
        print(f"you only have 5 attempts to guess the number")
        print(f"you have 10 attempts to guess the number!")
        while(attempt>0):
                guess= int(input("Make a guess: "))
                final = guessnumber(guess)
                
                print(f"you have {attempt} attempts to guess the number!")
                print(f"{final}")
                attempt= attempt-1

    print(f"correct answer is {number}")
    os.system("cls")
    play = input("Do you want to play again: type 'y' or 'n': ")
    if play=='y':
       isvalue=True
       os.system("cls")
    else:
       isvalue=False




