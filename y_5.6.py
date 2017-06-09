from swampy.TurtleWorld import *


def koch(t,length):
    if length < 3:
        fd(t,length)
        return
    koch(t,length/3)
    lt(t,60)
    koch(t,length/3)
    rt(t,120)
    koch(t,length/3)
    lt(t,60)
    koch(t,length/3)
    return


def snowflake(t,length):
    for i in range(3):
        koch(t,length)
        rt(t,120)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
# square(bob,179)
# koch(bob,210)
snowflake(bob,210)
wait_for_user()