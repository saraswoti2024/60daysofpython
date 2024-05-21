#project hangman

import random
chosen_word = ["apple","banana","pineapple"]
ranword = random.choice(chosen_word).lower()
length = len(ranword)
print(ranword)
val = str(length)
print(length)

# store =[]
# for i in range(0,length):
#     store+=ranword[i]
# print(store)

display =[]
# for j in range(len(ranword)):
#     display += "_"
# print(display)

# for letter in store:
#     if(letter==guess):
#         print(letter)
#         i+=1
#         display[i] = letter
#         print(display)
guess = input("guess a word: ").lower()
end = False
while not False:
 guess = input("guess a word: ").lower()
 for i in range(length):
    letter = ranword[i]
    if letter == guess:
        display[i] = letter
        print(display[i])
 
 
print(display)
if "_" not in display:
end = True
print("you win")
else:
print("you lost")