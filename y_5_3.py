def check_fermat(a,b,c,n):
    if n>1 and a>0 and b>0 and c>0 and (a**n + b**n == c**n):
        return 'Holy smokes,Fermat was wrong!'
    return "No, that doesn't work."


def input_abc():
    inputt = raw_input('Please input a,b,c and n \t FORMAT: a,b,c,n\n')
    inputt = inputt.strip().split(',')
    a = int(inputt[0])
    b = int(inputt[1])
    c = int(inputt[2])
    n = int(inputt[3])
    return check_fermat(a,b,c,n)


print input_abc()