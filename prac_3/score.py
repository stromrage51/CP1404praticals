"""
Subject: CP1404

The purpose of these program is to Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt.

Student name: Matthew Ballarino
Student number: 13291475
"""

import random


"""Creating a random score"""
# amount_of_grades = int(input("Please how grades their are: "))


# print(grade_statement(score, amount_of_grades))
def main ():
    """Finds out the score and giving a grade"""
    score = 0

    work = int(input("How many grades are their: "))
    LIST_RANDOM = grade_maker(score, work)
    # LIST_RANDOM = 0
    print(grade_maker(score, work))
    print(grade_maker(LIST_RANDOM, work))
    print("The score was {0} and grade was {1}".format(grade_maker(LIST_RANDOM, work), grade_maker(score, work), sep=''))

def grade_maker(score, work):
    for k in range(work):
        LIST_RANDOM = random.randrange(0, 100, 10)
        score = LIST_RANDOM

    if score <= 0:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"

        elif score >= 50:
            return "Passable"

        else:
            return "Bad"


main()


