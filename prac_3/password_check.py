"""
Subject: CP1404

To create a program that error checks password
length to minimum length.

Student name: Matthew Ballarino
Student number: 13291475
"""

MINIMUM_LENGTH = 6

password_input = input("Enter password that at least has {0} characters:".format(MINIMUM_LENGTH))

while len(password_input) < MINIMUM_LENGTH:
    password_input = input("Please enter password that at least has {0} characters:".format(MINIMUM_LENGTH))
print('*' * len(password_input))



