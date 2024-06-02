import math 
import random
import os
from art_day9 import logo


#dictionary: key|value

# programming_dictionary = {

#     "bug": "an error in program",
#     "function": "easily call",
#     "loop": "repeating over and over again",
#     12:"twleve",
# }
# print(programming_dictionary["bug"])
# print(programming_dictionary[12])
# print(type(programming_dictionary[12]))

# #adding new items
# programming_dictionary["coke"] ="very tasty"
# print(programming_dictionary)

# #empty dictionary
# empty_Dictionary = {}
# #programming_dictionary = {}  #wipes mathi ko data and will be empty

# #edit an item
# programming_dictionary["bug"] = "kira"
# print(programming_dictionary)

#loop in dictionary
# for i in programming_dictionary:
#     print(i)  #gives only key
#     print(programming_dictionary[i]) #gives only value
#     print( str(i) + " : " + programming_dictionary[i])

#exercise- to grade the student marks in new dictonary without modifying previous dictionary
# student_score = {
#     "sara" : 80,
#     "paru" : 92,
#     "bimala" : 62,
#     "sneha" : 59,
#     "sita" : 90,
#     "nir" : 52,
# }
# student_grades = {}
# for key in student_score:
#     if (student_score[key]>80):
#      student_grades[key] = "Exceeds Expectation"
#     elif (student_score[key]>90):
#      student_grades[key] = "outstanding"
#     elif (student_score[key]>70):
#      student_grades[key]="Acceptable"
#     elif (student_score[key]<70):
#      student_grades[key] = "Fail"

# print(student_score)
# print(student_grades)

############################################################################################
#NESTING

#nesting list in dictionary
# travels = {
#     "Nepal" : ["kathmandu","ramechhap","chitwan","sinduli"],
#     "France" : ["paris","lille","dijon"],
#     "India" : ["delhi","mumbai","chennai","pune"],
#      "capital" : {"capitals":["paris","Nepal","Kathmandu"],
#                   "total_visit":4,
#                   "popular":["nepal","india","france","greece"],
#                   },
# }
# print(travels)


###adding new country in the travel log without modifying it by calling function
# travel_log = [
#     {
#         "country" : "France",
#         "visits" : 12,
#         "cities" : ["paris","lille","Dijon"]
#     },
#     {
#         "country" : "Germany",
#         "visits" : 5,
#         "cities" : ["berlin","hamburg","stuttgart"]
#     },
# ]

# def add_new_country(countries,visities,citieses):
#     new_country={}
#     new_country["country"]= countries
#     new_country["visits"]=visities
#     new_country["cities"]=citieses
#     travel_log.append(new_country)
# li = input("add list: ")
# my_list = li.split()
# print(my_list)
# add_new_country("russia",2,citieses=my_list)
# print(travel_log)

#############project-secretauction################


# def auction(value):
    
def findbidder(bidding_record):
    highest=0
    winner = ""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest:
            highest=bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")


print(logo)
print("Welcome to the secret auction program")
bids={}
isvalue = True
while (isvalue):
    key = input("what is your name: ")
    value = int(input("what's your bid? : $"))
    bids[key] = value
    add = input("are there any other bidders? type yes or no: ").lower()
    if add=="no":
        findbidder(bids)
    elif add=="yes":
       os.system("cls")








