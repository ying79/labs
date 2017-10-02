from sys import float_info
from math import sqrt


def square_root(a):
    x = a / 2.0
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < float_info.epsilon:
            return x
        x = y


def test_square_root(list):
    for l in list:
        print '{0:<7}'.format(l/1.0),'{0:<19}'.format(str(square_root(int(l)))),'{0:<19}'.format(str(sqrt(int(l)))),'{0:<19}'.format(str(abs(square_root(int(l))-sqrt(int(l)))))


listt = range(1,10)+[79]+[224]
test_square_root(listt)