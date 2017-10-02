'''
compare to y_6_6.py
'''


def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

word = 'Kayak'
print is_palindrome(word)


'''
Single Word Palindromes:

Anna
Civic
Kayak
Level
Madam
Mom
Noon
Racecar
Radar
Redder
Refer
Repaper
Rotator
Rotor
Sagas
Solos
Stats
Tenet
Wow

'''
