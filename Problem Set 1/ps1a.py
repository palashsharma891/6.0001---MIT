# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:07:22 2020

@author: Palash
"""

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12
portion_saved = float(
        input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

months = 0

while(current_savings < portion_down_payment):
    current_savings = current_savings + (current_savings * r / 12) + (
            portion_saved * monthly_salary)
    months += 1
    
print("Number of months: ", months)
    
