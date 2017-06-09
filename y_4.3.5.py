from swampy.TurtleWorld import *
from math import pi


def polygon(t,length,n,angle):
    for i in range(n*angle/360):
        fd(t,length)
        lt(t,360.0/n)
    wait_for_user()


def arc(t,r,angle):
    n = int(2*pi*r/3)+1
    return polygon(t,(2*pi*r/n),n,angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
# square(bob,179)
arc(bob,79,180)