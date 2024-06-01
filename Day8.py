import math
import art_day08
# def greet(a):
#     print(f"hello {a}")
#     print(f" how are you {a}")

# greet("saraswoti")
# greet(123)

# #multiple arguments
# def greet(a,b):
#     print(f"hello i am {a}, age is {b}")

# greet("sara",21)

# #keyword arguments
# greet(b=21,a="sara")

# #exercise-area calculation

# def paint(height,width,coverage):
#     no_of_cans = (height*width) / coverage
#     print(f"the number of cans you need is: {math.ceil(no_of_cans)}")

# height = int(input("height: "))
# width = int(input("width: "))

# paint(height=height,width=width,coverage=5)

# #exercise-2 --prime number
# def prime(n):
#  i=2
#  isprime = True
 
#  for i in range(i,n):
#   if(n%i==0):
#     isprime = False
#     break
#   else:
#     isprime = True

#  if isprime:
#     print(f"{n} is a prime number")
#  else:
#     print(f"{n} is not a prime number")

# n=int(input("number to check: "))
# prime(n=n)
      
##project - caesar cipher
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caeser(plaintext,key,which):
    cipher=""
    for i in plaintext:
      if i in letter:
        position = letter.index(i)   #index of letter
        
        if which=="encrypt":
            new_position = position+key
            convert = letter[new_position]
            cipher+=convert
        elif which=="decrypt":
             new_position = position-key
             convert = letter[new_position]
             cipher+=convert
           
      else:
         print("not inside letter try again")
         break
    print(f"{which} is {cipher}")

print(art_day08.logo)

should_continue=True
while(should_continue):
    which = input("encrypt or decrypt: ").lower()
    plaintext = (input("enter your message:\n")).lower()
    key = int(input("key: "))
    key = key%26
    caeser(plaintext=plaintext,key=key,which=which)
    print("-------------------------")
    result=input("do you want to go again.type yes or no: ").lower()
    if(result=="no"):
     print("goodbye")
     should_continue=False
   
   
   



 









