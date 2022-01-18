"""
    Program 8

    Write a Python program to test whether a passed letter is a vowel or not.

"""

# Way 1


def checkvowel(ch):
    if(ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o'
            or ch == 'U' or ch == 'u'):
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")


checkvowel('a')
checkvowel('b')

# Way 2

_vowels = ('a', 'e', 'i', 'o', 'u')
x = (lambda a: a in _vowels)
r = 'is a Vowel' if x('a') else 'is a Consonant'
print(r)


# Way 3


def isvowel(s):
    x1 = (lambda a: a in _vowels)
    r1 = 'is a Vowel' if x1(s) else 'is a Consonant'
    print(r1)


isvowel('b')
