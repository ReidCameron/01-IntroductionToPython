"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Cameron Reid.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
#########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

sam = rg.SimpleTurtle('turtle')
sam.pen = rg.Pen('orange', 3)
sam.speed = 2  # Slow

## creates a triangle path for sam
mult = 45 #adjusts size of triangle
sam.left(143)
sam.forward(5*mult)
sam.left(127)
sam.forward(3*mult)
sam.left(90)
sam.forward(4*mult)

window.close_on_mouse_click()