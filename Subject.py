import random

def pick_a_subject():
    Subjects = ['ME-103','PHY-102','CY-101','CY-103','MA-102']
    Subject_of_the_day = random.choice(Subjects)
    
    print("Today\'s Subject is:", Subject_of_the_day)
    pick_a_subject()
