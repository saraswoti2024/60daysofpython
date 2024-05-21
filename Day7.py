#project hangman
# from replit import clear
import random
import os
import hangman_word07
# from hangman_word07 import word_list
from hangman_art07 import logo,stages

ranword = random.choice(hangman_word07.word_list).lower()
length = len(ranword)
lives = 6
end = False
print(logo)

print ("Welcome to HarryPotter Hangman game.")
print ("Guess the character of HarryPotter!")
display =[]

for j in range(len(ranword)):
    display += "_"
print(display)
print(f"There are total {len(display)} letter")
# for letter in store:
#     if(letter==guess):
#         print(letter)
#         i+=1
#         display[i] = letter
#         print(display)

while not end:
 guess = input("guess a word: ").lower()
#  os.system("cls")

 if guess in display:
   print(f"you've already guessed {guess}")
   continue
 
 for i in range(length):
  letter = ranword[i]
  if letter == guess:
   display[i] = letter
   print(display)

 if guess not in ranword:    #not in = (!=)
    print("you guessed " + guess +" which is incorrect. " "you have " + str(lives-1) + " guess left")
    print(stages[lives])
    lives -= 1
 if lives == 0:
        end = True
        print("you lose!")
        print(f"The correct answer is: {ranword}")
 if "_" not in display:
     end = True
     print("you win")       





