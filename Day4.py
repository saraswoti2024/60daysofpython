import random
import Day1

# random_integer = random.randint(1,100)          #generating random int number
# print(random_integer)
# print(Day1.a,Day1.b)                            #aarko file bata import gareko value
# random_float = random.random()                  #cannot write inside () error aauxa 0-1 samma value hunxa
# print(random_float)
# print(round((random_float*10),3))               #*10 garerw 0-10 samma ko random value generate garxa and soon 

# print(f"you and youre partner love score: {round((random.random()*100),2)}%")


# random_int = random.randint(1,2)
# if(random_int==1):
#  print("Head")
# elif(random_int==2):
#  print("Tail")

# states = ["kathmandu","pokhara","ramechapp","chitwan","nepaljung"]
# print(states[-1]) #counts from last
# print(states[0]) #beginning

# states[-1] = "Nepalland"
# states.append("dolakha")      #adding one value to the list
# states.extend(["illam","kanchanjunga"]) #adding multiple value to the list
# print(states)

#execerise-who will pay bill choosing randomly
# names_string = input("write your names and give comma: ")
# names = names_string.split(",")
# item_name = len(names)
# value = random.randint(0,item_name-1)
# #random = random.choice(names)
# print(f"person who will pay is {names[value]}")


#nested list
# fruits = ["strawberries","grapes","cherries","apple"]
# vegetables = ["spinach","tomatoes","potatoes","cabbage"]

# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)

##project1-overwrite "X" on selected row from 3rows
# row1=["👛","👛","👛"]
# row2=["👛","👛","👛"]
# row3=["👛","👛","👛"]
# map =[row1, row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = int(input("which one you to access?: "))

# if(position==00):
#     map[0][0]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==0o1):
#     map[0][1]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==(0o2)):
#     map[0][2]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==10):
#     map[1][0]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==11):
#     map[1][1]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==12):
#     map[1][2]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==20):
#     map[2][0]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==21):
#     map[2][1]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

# elif(position==22):
#     map[2][2]= 'X'
#     print(f"{row1}\n{row2}\n{row3}")

#project2-rock,paper,scissor
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
graphic = [rock,paper,scissors]

human_choice = int(input("what do you choose? Type 0 for Rock,1 for paper or 2 for scissor: "))
computer_choice = random.randint(0,2)

if(human_choice==0 and computer_choice==2 or human_choice==1 and computer_choice==0 or human_choice==2 and computer_choice==1):
 print(f"your choice:\n{graphic[human_choice]}")
 print(f"computer choice:\n{graphic[computer_choice]}")
 print("you won!😍😍")

elif(computer_choice==0 and human_choice==2 or computer_choice==1 and human_choice==0 or computer_choice==2 and human_choice==1):
 print(f"your choice:\n{graphic[human_choice]}")
 print(f"computer choice:\n{graphic[computer_choice]}")
 print("you lose!🫣🫣")

else:
 print(f"your choice:\n{graphic[human_choice]}")
 print(f"computer choice:\n{graphic[computer_choice]}")
 print("DRAW!!🥱🥱")