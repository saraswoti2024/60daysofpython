import random
import string
##FOR LOOP USING LIST
# fruits = ["apple","peach","pear"]

# for fruit in fruits:
#  print(fruit)
#  print(fruit+"pie")
 
#exercise-1 average height
# student_height = [180,124,144,145,160,200]
# total =0
# i=0
# for height in student_height:
#     total +=height
#     i+=1

# average = total/i
# print(f"the total average height is: {round(average,3)}")

#exercise-2 highest score

# student_score = [78,22,90,25,16,23]
# max = 0
# min = student_score[0]
# for score in student_score:  #to compare starting with index 1 student_score[1:]
#  if(score>max):
#   max = score
 
#  if(score<min):
#   min = score

# print(f"your maximum score : {max}")
# print(f"your minimum score: {min}")

#range in for loop

# for num in range(1,11,3):   #stepping by 3(1 paxi 3 oota number xoderw 4 ani 7 ani 10 and soon)
#     print(num)

# sum = 0
# for i in range(1,101):
#     sum +=i
# print(sum)

#exercise - adding even number
# sum = 0
# for i in range(1,101):
#     if(i%2==0):
#         sum +=i
# print(sum)

#or 

# sum = 0
# for i in range(0,101,2):
#         sum +=i
# print(sum)

#value = int(input("input number: "))
# for i in range(1,101):
#  if(i%5==0 and i%3==0):
#   print("FizzBuzz")
#  elif(i%3==0):
#    print("Fizz")
#  elif(i%5==0):
#   print("Buzz")
#  else:
#   print(i)

#project - pipassword Generator 

print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password? "))
symbol = int(input("How many symbols would you like? "))
number = int(input("How many numbers would you like? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # if(nsymbol<symbols):
    #  pass_symbol = random.choice(symbol)
    #  nsymbol += 1 
    # else:
    #    pass_other = random.choice(other)
    
    # if(nnum<numbers):
    #    pass_number = random.randint(1,100)
    #    nsymbol += 1 
    # else:
    #    pass_other = random.choice(other)

# print(f"your password is : {pass_symbol}+{pass_number}+{pass_other}")
password = []
for i in range(1,letter+1):
 password += (random.choice(letters))

for i in range(1,symbol+1):
 password += random.choice(symbols)

for i in range(1,number+1):
 password += random.choice(numbers)

random.shuffle(password)
print(password)

passwords = ""
for i in password:
 passwords += i

print(passwords)


