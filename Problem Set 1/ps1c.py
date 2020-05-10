# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:47:33 2020

@author: Palash
"""

def calculate_savings_rate(annual_salary):
    """
    Calculate the best savings rate
    """
    


annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = ????

total_cost = 1000000.0
semi_annual_raise = .07
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

months = 0

while(months < 36):
    
    monthly_salary = annual_salary / 12
    
    current_savings = current_savings + (current_savings * r / 12) + (
            calculate_savings_rate(annual_salary) * monthly_salary)
    
    months += 1
    
    if (months % 6) == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    

print("Best savings rate: ", portion_saved)


    
