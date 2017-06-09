from swampy.TurtleWorld import *
from math import pi

def polygon(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t,360.0/n)
    wait_for_user()

def circle(t,r):
    n = int(2*pi*r/3)+1
    return polygon(t,(2*pi*r/n),n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
# square(bob,179)
circle(bob,79)

