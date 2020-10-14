# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:47:38 2020

@author: xyz
"""

def main():
    celsius = int(input("What is the Celsius temp? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temp is",fahrenheit,"degrees fahrenheit.")
    if fahrenheit > 90:
        print("It's really hot out there, be careful!")
    if fahrenheit < 60:
        print("Brrrrr. Be sure to dress warmly!")

main()









