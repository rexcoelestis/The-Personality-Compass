from questions import *
from personality_types import *
import numpy

answers = []
questions_seen = 0
name = "Friend"
ready = False
description = "\nThe description will be here."
instructions = "\nThe instructions will be here."
leave = False
question_set = "'a' or 'b'.  "

def calculate_As(list):
    return list.count("a")

def calculate_Bs(list):
    return list.count("b")

def calculate_Cs(list):
    return list.count("c")

def calculate_Ds(list):
    return list.count("d")

print("\nWelcome to The Personality Compass \n Python Edition \n {} \n {}  ".format(description, instructions))

name = input("\nWhat is your name?  \n\n")

while ready == False:
    step1 = input("\nHello {}, What would you like to do? \nJust type: \n D - to read the description of the quiz again. \n I - to read the instructions again. \n B - to begin the quiz. \n Q - to exit the quiz. \n\n".format(name))
    if step1 == "B":
        ready = True
    elif step1 == "Q":
        leave = True
        break
    elif step1 == "I":
        print(instructions)
    elif step1 == "D":
        print(description)

for question in questions:
    if leave == True:
        exit()
    questions_seen += 1
    if questions_seen > 30:
        question_set = "'c' or 'd'. You can always also choose 'q' to quit.  "
    answer = input(question)
    try:
        answer = answer.lower()
        if questions_seen <= 30:
            if answer != "a" or answer != "b" or answer != "q":
                raise ValueError("Did not choose {} ".format(question_set))
        else:
            if answer != "a" or answer != "b" or answer != "q":
                raise ValueError("Did not choose {} ".format(question_set))
    except ValueError as err:
        print("Please be sure to select the correct option.  Error: {}".format(err))
    else:
        if answer == "q":
            exit
        else:
            answers.append(answer)

print("Thank you for your answers!  ")
print("Please wait while we calculate your result...  ")

acount = calculate_As(answers)
bcount = calculate_Bs(answers)
ccount = calculate_Cs(answers)
dcount = calculate_Ds(answers)

if acount >= bcount:
    ns_type = "A"
else:
    ns_type = "B"

if ccount >= dcount:
    ew_type = "C"
else:
    ew_type = "D"

p_type_key = ns_type + ew_type
personality_type = p_types.get(p_type_key)
type_description = p_type_descr.get(p_type_key)

print("Your personality type is {}.".format(personality_type))
print(type_description)
print("Thank you for participating!  Have a good one!")

exit()
