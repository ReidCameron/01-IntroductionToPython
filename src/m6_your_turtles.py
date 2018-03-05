"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Cameron Reid.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', 2)
green_turtle.speed = 200  # Fast Drawing

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 3)
blue_turtle.speed = 200  # Fast Drawing

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 5)
red_turtle.speed = 200  # Fast Drawing

size = 300
rng = 100
for k in range(rng):
    #Draws a square.
    green_turtle.draw_square(size)
    #The pen is picked up and moved.
    green_turtle.pen_up()
    green_turtle.left(90)
    green_turtle.forward(1)
    # Put the pen down again (so drawing resumes).
    green_turtle.pen_down()
    size = size - 1.5

size = 150
for k in range(100):
    #Draws a circle.
    blue_turtle.draw_circle(size)
    # The pen is picked up and moved.
    blue_turtle.pen_up()
    blue_turtle.left(90)
    blue_turtle.forward(1)
    #Put the pen down again (so drawing resumes).
    blue_turtle.pen_down()
    # Make the size for the NEXT cicrle be 1 pixel smaller.
    size = size - 1

size = 600
#positions red turtle
red_turtle.pen_up()
red_turtle.left(180)
red_turtle.forward(300)
red_turtle.left(90)
red_turtle.forward(300)
red_turtle.left(90)
red_turtle.pen_down()
for k in range(25):
     #Draws a square.
     red_turtle.draw_square(size)
     #The pen is picked up and moved.
     red_turtle.pen_up()
     red_turtle.right(90)
     red_turtle.forward(1)
     red_turtle.left(90)
     red_turtle.right(180)
     red_turtle.forward(1)
     red_turtle.right(180)
     # Put the pen down again (so drawing resumes).
     red_turtle.pen_down()
     # Make the size for the NEXT square be 2 pixels larger.
     size = size + 2

#closes window on mouseclick
window.close_on_mouse_click()