from questions import *
from personality_types import *
import numpy

answers = []
questions_seen = 0
questions_remaining = 60
name = "Friend"
ready = False
description = "\nThe Personality Compass is a ground-breaking exploration of the main personality types which form the basis of societies the world over.  Tried and tested with astonishingly accurate results.  The Personality Compass shows how these differed temperaments correspond with the governing points of the compass, sharing the special characteristics that are assosciated with each direction."
instructions = "\nQUICK TEST FOR TYPE\n\nThis is an adaptation of Turner and Greco's Quick-Test for Type.  You will be presented with 60 pairs of words.  For each pair, read the choices and choose the word that describes you more often than the other (even though you may have both characteristics).  For the first 30 pairs you will make your selection by choosing either 'a' or 'b'.  For the second group of 30 pairs, you must make your selection by choosing either 'c' or 'd'.  You may also select 'q' at anytime to exit the program."
leave = False
question_set = "'a' or 'b'.  You can always also choose 'q' to quit.  "
opt1 = "a"
opt2 = "b"

def calculate_As(list):
    return list.count("a")

def calculate_Bs(list):
    return list.count("b")

def calculate_Cs(list):
    return list.count("c")

def calculate_Ds(list):
    return list.count("d")

print("\nWelcome to The Personality Compass \nPython Edition \n {} \n {}  ".format(description, instructions))

name = input("\nWhat is your name?  \n\n")

while ready == False:
    step1 = input("\nHello {}, What would you like to do? \nJust type: \n D - to read the description of the quiz again. \n I - to read the instructions again. \n B - to begin the quiz. \n Q - to exit the quiz. \n\n".format(name))
    if step1.lower() == "b":
        ready = True
    elif step1.lower() == "q":
        exit()
    elif step1.lower() == "i":
        print(instructions)
    elif step1.lower() == "d":
        print(description)

print("\nExcellent!  Let's get started!!  \n(You may select 'q' at anytime to exit)")

for question in questions:
    if leave == True:
        exit()
    questions_seen += 1
    if questions_seen > 30:
        question_set = "'c' or 'd'. You can always also choose 'q' to quit.  "
        opt1 = "c"
        opt2 = "d"
    print("\nQUESTION {} ({} remaining):".format(questions_seen, questions_remaining))
    answer = input(question)
    try:
        answer = answer.lower()
        while answer not in {opt1, opt2, "q"}:
            raise ValueError("Did not choose {} ".format(question_set))
    except ValueError as err:
        print("Please be sure to select the correct option.  Error: {}".format(err))
    else:
        if answer == "q":
            leave = True
        else:
            answers.append(answer)
            questions_remaining -= 1

print("Thank you for your answers!  \n")
print("Please wait while we calculate your result...  \n")
print("...")
print("...")
print("...")

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

print("\nYour personality type is {}. \n".format(personality_type))
print(type_description)
print("\nFor more information about your type and what it means to you, please check out 'The Personality Compass: A New Way to Understand People' by Diane Turner & Thelma Greco.")
print("\nThank you for participating!  Have a good one!")

exit()
