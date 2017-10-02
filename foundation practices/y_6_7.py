def is_power(a,b):
    while a <> 0 and b <> 0:
        return a % b == 0 and a/b > 0
    return False


print is_power(14,7)