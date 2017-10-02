from math import pi


def estimate_pi():
    k=0
    _pi = 0.0
    while formula(k) >= 1e-15:
        _pi += formula(k)
        k+=1
    return '{0:<19}'.format(1/_pi) + '{0:<19}'.format(pi)


def factorial(number):
    if number == 0:
        return 1
    result = 1
    for n in range(1,number+1):
        result *= n
    return float(result)


def formula(k):
    return (2*2**0.5/9801)*factorial(4*k)*(1103+26390*k)/(factorial(k)**4*396**(4*k))


print estimate_pi()