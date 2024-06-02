import math 
import random


#dictionary: key|value

programming_dictionary = {

    "bug": "an error in program",
    "function": "easily call",
    "loop": "repeating over and over again",
    12:"twleve",
}
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
for i in programming_dictionary:
    print(i)  #gives only key
    print(programming_dictionary[i]) #gives only value
    print( str(i) + " : " + programming_dictionary[i])

#exercise- to grade the student marks in new dictonary without modifying previous dictionary
student_score = {
    "sara" : 80,
    "paru" : 92,
    "bimala" : 62,
    "sneha" : 59,
    "sita" : 90,
    "nir" : 52,
}
student_grades = {}
for key in student_score:
    if (student_score[key]>80):
     student_grades[key] = "Exceeds Expectation"
    elif (student_score[key]>90):
     student_grades[key] = "outstanding"
    elif (student_score[key]>70):
     student_grades[key]="Acceptable"
    elif (student_score[key]<70):
     student_grades[key] = "Fail"

print(student_score)
print(student_grades)


