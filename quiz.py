from questions import questions
from types import types
from types import type_descr
import numpy

answers = []
questions_seen = 0
name = ""
ready = false
description = "The description will be here."
instructions = "The instructions will be here."
leave = false
question_set = "'a' or 'b'.  "

def calculate_As(list):
    return list.count("a")

def calculate_Bs(list):
    return list.count("b")

def calculate_Cs(list):
    return list.count("c")

def calculate_Ds(list):
    return list.count("d")

print("Welcome to The Personality Compass \n Python Edition \n\n {} \n\n {}  ".format(description, instructions))

name = input("What is your name?  ")

while ready == false:
    step1 = input("Hello {}, What would you like to do? \n type: \n D - to read the description of the quiz again. \n I - to read the instructions again. \n B - to begin the quiz. \n Q - to exit the quiz.".format(name))
    if step1 == "B":
        ready = true
    elif step1 == "Q":
        leave = true
        break
    elif step1 == "I":
        print(instructions)
    elif step1 == "D":
        print(description)

while leave == false:
    for question in questions:
        questions_seen += 1
        if questions_seen > 30:
            question_set = "'c' or 'd'.  "
        answer = input(question)
        try:
            answer = answer.lower()
            if answer != "a" or answer != "b" or answer != "c" or answer != "d":
                raise ValueError("Did not choose 'a', 'b', 'c', or 'd'. ")
        except ValueError as err:
                print("Please be sure to select either {}".format(question_set))
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
    personality_type = types.get(p_type_key)
    type_description = type_descr.get(p_type_key)

    print("Your personality type is {}.".format(personality_type))
    print(type_description)
    print("Thank you for participating!  Have a good one!")
    leave == true
exit()
