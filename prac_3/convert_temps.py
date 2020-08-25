"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

import random


def main():




    while choice != "Q":
          if choice == "C":
             celsius = float(input("Celsius: "))
             fahrenheit = converting_celsius_to_fahrenheit(celsius)
             print("Result: {:.2f} F".format(fahrenheit))
          elif choice == "F":
                fahrenheit = float(input("Fahrenheit: "))
                celsius = converting_fahrenheit_to_celsius(fahrenheit)
                print("Result: {:.2f} C".format(celsius))
          else:
                 print("Invalid option")
          print(MENU)
          choice = input(">>> ").upper()


    print("Thank you.")


def converting_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def converting_celsius_to_fahrenheit(celsius):
    """Converting celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32



main()


