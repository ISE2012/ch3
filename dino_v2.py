# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:47:38 2020

@author: xyz
"""

def main():
    print("Welcome to the DinoCheck 2.0")
    print("Please answer '0' (no) or '1' (yes) for each question")
    isSharp =  int(input ("Does the dinosaur have sharp teeth? "))
    isWalled = int(input ("Is the dinosaur behind a large wall? "))
    isBiped =  int(input ("Is the dinosaur walking on two legs? "))
    isClawed = int(input ("Does the dinosaur have sharp claws? "))
    isBeaked = int(input ("Does the dinosaur have a beak? "))

    if isSharp:
        print("Be careful of a dinosaur with sharp teeth!")
    if isWalled:
        print("You are safe, the dinosaur is behind a big wall!")
    if isBiped:
        print("Be careful of a dinosaur who walks on two legs!")
    if isClawed and isBeaked:
        print("Be careful of a dinosaur with sharp claws and a beak!")
    print("Good luck!")

main()










