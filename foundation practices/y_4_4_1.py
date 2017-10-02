from swampy.TurtleWorld import *

def square(t):
    for i in range(4):
        fd(t,79)
        lt(t)
    wait_for_user()


world = TurtleWorld()
bob = Turtle()
square(bob)

