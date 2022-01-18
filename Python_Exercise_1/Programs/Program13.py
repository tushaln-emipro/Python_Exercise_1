"""
    Program 13
    Write a Python program to remove the first item from a specified list.
        a. color = ["Red", "Black", "Green", "White", "Orange"]
        b. num = [255,3678,95,158,759,157]
"""

from collections import deque
color = ["Red", "Black", "Green", "White", "Orange"]
num = [255, 3678, 95, 158, 759, 157]

# Way 1

res = deque(color)
res.popleft()
print("color list is : " + str(list(res)))

res1 = deque(num)
res1.popleft()
print("num list is : " + str(list(res1)))

# Way 2

del res[0]
del res1[0]
print(res)
print(res1)

# Way 3

color.pop(0)
num.pop(0)
print(color)
print(num)
