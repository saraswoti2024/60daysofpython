import random
import math

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

humancard()
if input("type y to continue or n to discontinue: ")=="y":
    humancard()
