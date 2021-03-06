"""
This are some of the solution to Reeborg's world challenges. I used this to practice python functions
"""

# Home 1 and 2 Solution

"""
def home():
    move()
    move()

home()
"""

# Home 3 Solution

"""
def home():
    move()
    move()
    turn_left()
    move()

home()
"""

# Home 4 Solution

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()   
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()
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
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
"""

# Hurdle 4 Solution

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()
"""

# Maze Solution (It's the same as hurdle 3 solution

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# To prevent infinite loop
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()
        
"""