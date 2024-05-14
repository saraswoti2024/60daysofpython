# water_level = 50

# if (water_level>80):
#     print("Drain water")

# else:
#     print("keep filling")

# height = int(input("what is your height?"))


# if height>=120:
#     print("you're eligible for roller coaster")
#     age = int(input("What is your age?"))
#     if age>12:
#          print("please pay $7.")

#     elif age<=18:
#         print("pay $7")

#     else:
#         print("please pay $12")

# else:
#     print("sorry,youre not eligible")


#odd or even
# num = int(input("type num:"))

# if num%2==0:
#     print("even")

# else:
#     print("odd")

#exercise-BMI calculator

# height = float(input("Enter your height in ft:"))
# weight = float(input("Enter your weight in kg:"))

# BMI = round(weight/(height**2),3)

# if(BMI<=18.5):
#     print(f"you're underweight,your BMI is {BMI}")
# elif BMI<=25:
#     print(f"you're normal weight,your BMI is {BMI}")
# elif BMI<=30:
#     print(f"you're overweight,your BMI is {BMI}")
# elif BMI<=35:
#     print(f"you're obese,your BMI is {BMI}")
# else:
#     print(f"you're clinically obese,your BMI is {BMI}")

#exercise-leapyear
# year = int(input("year:"))

# if(year%4==0):
#     if(year%100==0):
#         if(year%400==0):
#             print(f"{year} is a leap year!")
        
#         else:
#              print(f"{year} is not a leap year!")
#     else:
#         print(f"{year} is a leap year!")
# else:
#     print(f"{year} is not a leap year!")

#exercise-pizza order program

# print("Welcome to python pizza Deliviries!")
# size = input("what size of pizza do you wnat?S,M or L: ")
# add_pepporani = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese?Y or N: ")


# p= 0

# echeese = 1

# if size=="S": 
#     p +=15

# elif size=="M":
#     p +=20
# elif size =="L":
#     p +=25

# if add_pepporani=="Y":
#    if size == "S":
#        p+=2
#    else:
#        p+=3

# if extra_cheese=="Y":
#     p+=1

# print(f"your total is {p}")

#logical operators- and,or,not

#exercise- love calculator
print("Welcome to love calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter your lover's name: ")
combined = name1+name2
lowercase = combined.lower()

t= lowercase.count("t")
r= lowercase.count("r")
u= lowercase.count("u")
e= lowercase.count("e")

true = t+r+u+e

l= lowercase.count("l")
o= lowercase.count("o")
v= lowercase.count("v")
e= lowercase.count("e")

love = l+o+v+e

score = str(true+love)
print(f"your total love percentage is: {score}%")
score = int(score)
if (score<10) or (score>90):
    print("you go together like coke and mentos")
elif (score>=40) and (score<=50):
    print("you are alright together")

#exercise-treasure island

# print("Welcome to Treasure island.Your mission is to find treasure!")
# a = input("youre at a cross road where do you want to go?Type left or right")
# if(a=="left"):
#     b = input("you came to a lake.wait or swim?")
#     if b=="wait":
#      c = input("choose one door :red,blue or yellow")
#      if(c=="blue"):
#       print("you lose")
#      else:
#       print("stop")

#     else: 
#      c = input("you swim, blue,red or yellow?")  
#      if c=="blue" or c=="red":
#       print("You ")     

# elif a=="right":
#     b = input("red,blue or green door?")   
#     if(b=="red" or b =="blue"):
#      print("exit!")
#     else:
#      print("won!")

#practice-saraswoti's horror house game
# print("Welcome to saraswoti's horror house")

# choice1 = input("choose which house you want to go\nspider,dance,suprise: ")

# if(choice1=="spider"):
#  choice2 = input("wow!nice choice.you're so close to winning!!\nthere are three doors, choose one blue,red,black: ")
#  if(choice2=="blue" or choice2=="red"):
#   print("muahahahaha, you're out heehehehe")
#  elif choice2=="black":
#   print("CONGRAGULATIONS, YOU WON!!!")

# elif choice1 == "dance":
#  choice2 = input("you like dancing huh?!, i will show you how to dance.paparapapaprapap\nchose one dance hiphop,classical,belly: " )
#  if(choice2=="hiphop"):
#   print("go outside doing hiphop .youre out!")
#  elif(choice2=="classical"):
#   print("you won my horror house,but not the main prize dumbass .try again!")
#  else:
#   print("YOU WON!!!SHAKE YOUR HIP NOW HAHAHA")

# elif choice1=="suprise":
#  print("you're eliminated,you idiot!!")