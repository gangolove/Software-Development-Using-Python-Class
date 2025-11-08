"""
Name: Douglas Marshall
App Name: Student and GPA.py
Description: Program to accept student name and grade point average and print their accomplishments
"""

last_name = input('Please enter last name or "ZZZ" to quit! ')

if last_name != 'ZZZ':
    first_name = input('Please enter first name! ')
    print('Thank you, ', first_name, ' ', last_name, '. Now please tell me your GPA?')
    gpa = float(input())

    if gpa >= 3.5:
        print('Congrats! You have made the Dean\'s List!')
        
    elif gpa >= 3.25:
        print('Congrats! You have made the Honor Roll!')
    
    elif gpa >= 1.0:
        print('Congrats! You are passing!')
        
    else:
        print('Oh no! You are failing!')
