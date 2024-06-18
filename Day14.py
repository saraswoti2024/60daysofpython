#Project-Higher lower game

import random 
from game_dataday14 import data
from logoday14 import logo
import os

def total(followera,followerb):
    if followera>followerb:
        return "a"
    else:
        return "b"
    
accountb = random.choice(data)
score = 0
isvalue = True
while isvalue:    
    accounta = accountb
    accountb = random.choice(data)

    while accounta==accountb:
        accountb=random.choice(data)

    namea = accounta["name"]
    passiona = accounta["description"]
    countrya = accounta["country"]

    nameb = accountb["name"]
    passionb = accountb["description"]
    countryb = accountb["country"]

    print(f"Compare A : {namea}, a {passiona}, from {countrya}")

    print(logo)

    print(f"Against B: {nameb},  a {passionb}, from {countryb}")

    guess = input("choose A or B : ").lower()

    followera = accounta["follower_count"]
    followerb = accountb["follower_count"]


    value = total(followera,followerb)
    if guess==value:
        score += 1
        print(f"You're right! current score is: {score}") 
        print("--------------------------------------")       
    else:
        print(f"\nYou're wrong! your score is : {score}")
        print("-----------------------------------------\n")
        playagain = input("Do you want to play again?: Type Y or N : ").lower()
        if(playagain=="y"):
            os.system("cls")
            score=0
            isvalue=True
        else:
            isvalue=False

    



