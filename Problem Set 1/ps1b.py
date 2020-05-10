# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:21:38 2020

@author: Palash
"""

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(
        input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

months = 0

while(current_savings < portion_down_payment):
    
    print(annual_salary)
    
    monthly_salary = annual_salary / 12
    
    current_savings = current_savings + (current_savings * r / 12) + (
            portion_saved * monthly_salary)
    
    months += 1
    
    if (months % 6) == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    

print("Number of months: ", months)
    
