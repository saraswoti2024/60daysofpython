import random
import math
from art_day10 import logo
import os
#print(logo)

#function with output

# def function(fname,lname,dname):
 
#  """three quoted 
#    multi
#    line act as comment if no variable is assigned"""
#  if fname == "" or lname=="":
#   return
#  ffname = fname.title()
#  flname = lname.title()
#  f2name = dname
#  return f"{fname} {flname} {f2name}"
# print(function(input("enter your first name: "),"khadka",123))

# def result(n1,op,n2):
# n1 = input("what's the first number: ")
# print("+\n-\n*\n/\n")
# op = input("pick an operator: ")
# n2 = input("what's the second number: ")
# result(n1=n1,op=op,n2=n2)


# def add(n1, n2):
#   return n1 + n2

# def subtract(n1, n2):
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# def calculator():
#   print(logo)

#   num1 = float(input("first number: "))
#   for symbol in operations:
#     print(symbol)
#   should_continue = True
 
#   while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = answer
#     else:
#       should_continue = False
#       os.system("cls")

#       calculator()

# calculator()


##-------calculator-----------

def add(n1,n2):
 return n1+n2

def sub(n1,n2):
 return n1-n2

def div(n1,n2):
 return n1/n2

def mul(n1,n2):
 return n1*n2

def rem(n1,n2):
 return n1%n2

print(logo)
dictionary = {
 "+" : add,
 "-" : sub,
 "*" : mul,
 "/" : div,
 "%" : rem,
}

n1 = float(input("first number: "))
for i in dictionary:
 print(i)
isvalue=True
while isvalue:

  op = input("op: ")
  n2 = float(input("Second number: "))
  operation = dictionary[op]
  answer = operation(n1=n1,n2=n2)
  print(f" {n1} {op} {n2} = {round(answer,3)}")

  ask = input("do you want to continue y or n?")
  if (ask=="y"):
   n1 = answer    

  elif (ask=="n"):
    isvalue=False
  










 


