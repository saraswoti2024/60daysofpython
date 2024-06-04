import random
import math
from art_day11 import logo
import os

#jack,king,queen - 10


yourcard = []
computercard = []

def humancard():
    for i in range(1,3):
        my_card = random.randint(1,11)
        yourcard.append(my_card)
        value2 = random.randint(1,11)
        computercard.append(value2)
    print(f" your cards : {yourcard}")
    print(f"computer's card: {computercard[0]}")

def result(human,computer):
 if(human>=21 or human<computer):
    return "computer"
 elif(computer<human):
    return "Human"
 elif (computer==human):
    return "draw"
 
def calculation(yourcard):
    total_human = sum(yourcard)
    total_computer = sum(computercard)
    if(total_computer<17):
       value2 = random.randint(1,11)
       computercard.append(value2)
    total_result = result(human=total_human,computer=total_computer)
    print(f"human card: {yourcard}")
    print(f"computer card: {computercard}")
    print(f"The winner is : {total_result} ")


print(logo)
print("WELCOME TO BLACKJACK GAME!")

def addition_card():
    humancard()
    if input("type y to continue or n to discontinue: ")=="y":
        my_card = random.randint(1,11)
        yourcard.append(my_card)
        calculation(yourcard=yourcard)

    else:
     calculation(yourcard)

addition_card()
isvalue=True
while isvalue:
    print("------------------------------------------------")
    if input("do you want to play again: type yes or no: ")=="yes":
        os.system("cls")
        yourcard.clear()
        computercard.clear()
        addition_card()
    else:
     isvalue=False