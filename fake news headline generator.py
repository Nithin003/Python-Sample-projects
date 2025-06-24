
# A fake news headline generator mini project
# import "random" module.

import random

# Declare the subjects, actions and places for the headline using list

subjects = [
    "Prabhas","NTR","Virat Kohli","Modi","Tesla","Brahmi"
]

actions = [
    "dances and sings",
    "parked his car",
    "plays badminton",
    "throws a stone",
    "eats pani puri",
    "cracks a joke"
]

places = [
    "at Taj Mahal",
    "at Vijayawada Airport",
    "during the cricket match",
    "by declaring a W@r",
    "for the audience",
    "at India Gate"
]

# User makes a choice of random words for the fake headline

while True:
    
    subject1 = random.choice(subjects)
    action1 = random.choice(actions)
    place1 = random.choice(places)
    
    headline = f"BREAKING NEWS: {subject1} {action1} {place1}"
    print("\n",headline)
    print("_________________________________________")
    
    result = input("\nDo u want to another fake headline? (Yes/No): ").strip().lower()
    
    if result == "no": break
    

print("\nThanks and Have a fake day!!!\n")