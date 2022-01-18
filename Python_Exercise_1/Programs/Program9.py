"""
    Program 9
    Write a Program which takes a statement as input from the user and counts occurrences of each vowel in it.
"""

# Way 1


def totalvowel(s):
    total = 0
    for ch in s:
        if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o'
                or ch == 'U' or ch == 'u'):
            total = total + 1
    print('Total Vowel :', total)


totalvowel('abcde')

# Way 2


def getcountvowel(s):
    _vowels = ('a', 'e', 'i', 'o', 'u')
    print('Total Vowel :', len([i for i in s if i.lower() in _vowels]))


getcountvowel('abcdeE')
