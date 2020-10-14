# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:47:38 2020

@author: xyz
"""

def main():
    totalSales = float(input("Please enter your total sales: "))
    
    if totalSales >= 1000.00:
        iPhonesSold = int(input("Enter the number of iPhones sold: "))
        
        if iPhonesSold >= 3:
            bonus = totalSales * 0.03
        else:
            bonus = totalSales * 0.02

        print("Your bonus is $", bonus)

    else:
        print("Sorry, you do not get a bonus this time.")

main()


















