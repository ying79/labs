from palindrome import *


def is_palindrome(word):
    word = word.lower()
    while first(word) == last(word):
        if len(middle(word)) < 2:
            return True
        else:
            word = middle(word)
    return False

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