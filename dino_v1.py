# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:47:38 2020

@author: xyz
"""

def main():
    print("Welcome to the DinoCheck 1.0")
    print("Please answer 'True' or 'False' for each question")
    isSharp = input("Does the dinosaur have sharp teeth? ")
    isWalled = input("Is the dinosaur behind a large wall? ")
    isBiped = input("Is the dinosaur walking on two legs? ")
    isClawed = input("Does the dinosaur have sharp claws? ")
    isBeaked = input("Does the dinosaur have a beak? ")

    if isSharp == "True":
        print("Be careful of a dinosaur with sharp teeth!")
    if isWalled == "True":
        print("You are safe, the dinosaur is behind a big wall!")
    if isBiped == "True":
        print("Be careful of a dinosaur who walks on two legs!")
    if (isClawed  == "True") and (isBeaked == "True"):
        print("Be careful of a dinosaur with sharp claws and a beak!")
    print("Good luck!")

main()







