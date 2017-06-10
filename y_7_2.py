from sys import float_info


def square_root(a):
    x = a / 2.0
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < float_info.epsilon:
            return x
        x = y


print square_root(6.25)

