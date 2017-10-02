from swampy.TurtleWorld import *

def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)
    wait_for_user()

def polygon(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t,360.0/n)
    wait_for_user()

world = TurtleWorld()
bob = Turtle()
# square(bob,179)
polygon(bob,43,6)

