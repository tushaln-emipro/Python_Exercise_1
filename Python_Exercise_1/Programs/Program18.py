"""
    Program 18
    Write a Python program to print out a set containing all the colors from color_list_1 which are not present
    in color_list_2. Also find which values are common in both the lists.
        a. Test Data :
            i. color_list_1 = set(["White", "Black", "Red"])
            ii. color_list_2 = set(["Red", "Green"])
            iii. Expected Output :
            iv. {'Black', 'White'}
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))
print(set(color_list_1) & set(color_list_2))
print([i for i, j in zip(color_list_1, color_list_2) if i == j])