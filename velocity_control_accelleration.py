# control the position of a ball using the arrow keys

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]

# define event handlers
def draw(canvas):
    # Update ball position
   

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    acc = 1
    # velocity update here
        
    print (ball_pos)
    
# create frame 
frame = simplegui.create_frame("Velocity ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
