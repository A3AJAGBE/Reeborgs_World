"""
This are some of the solution to Reeborg's world challenges. I used this to practice python functions
"""

# Hurdle 1 Solution

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
def jump():
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    move()
    turn_left()
    move()
    jump()
"""

# Hurdle 2 Solution

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
"""

# Hurdle 3 Solution

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()

    if wall_in_front():
        turn_left()
        move()
        jump()
"""