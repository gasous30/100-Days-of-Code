# FINAL PROJECT

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    for x in range(0,3):
        turn_left()


while not at_goal():
    
    while(right_is_clear()):
        turn_right()
        move()
        
    while(wall_in_front()):
        turn_left()
        
    move()
