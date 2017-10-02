def add_ing(string):
    while len(string) > 4:
        if string[-3:] == 'ing':
            return string + 'ly'
        else:
            return string + 'ing'
    return string

print add_ing('django')