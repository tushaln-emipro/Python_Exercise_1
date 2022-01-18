"""
    Program 19
    Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing
    of any numbers that come after 237 in the sequence.
        a. Sample numbers list :
        b. numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758,
        219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767,
        553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527 ]
"""

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758,
           219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767,
           553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]

# Way 1

newlist1 = []
numbers.sort()
print(numbers)
for i in numbers:
    if ((i % 2) == 0) and (i < 237):
        newlist1.append(i)
    if 237 <= i:
        break

print(newlist1)

# Way 2

newlist2 = list(filter(lambda a: ((a % 2) == 0) and (a < 237), numbers))
print(newlist2)
