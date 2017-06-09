def is_triangle(a,b,c):
    if a+b>=c:
        return 'NO'
    return 'YES'


def input_abc():
    inputt = raw_input('Please input three lengths of triangle.\t FORMAT: a,b,c\n')
    inputt = inputt.strip().split(',')
    inputt = sorted(inputt,reverse=False)
    inputt = ''.join(inputt)
    a = int(inputt[0])
    b = int(inputt[1])
    c = int(inputt[2])
    return is_triangle(a,b,c)


print input_abc()