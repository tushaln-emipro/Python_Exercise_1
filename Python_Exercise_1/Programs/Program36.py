"""
    Program 36
    Write a Python program to filter the height and width of students, which are stored in a dictionary.
    Height >= 6ft and Weight>= 70kg:
        a. Original Dictionary :
            {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
        b. Output :
            {'Cierra Vega': (6.2, 70)}
"""
OrgDict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

# Way 1

def myfun(lt):
    for i in lt:
        if lt[i][0] >= 6 and lt[i][1] >= 70:
            print(i, lt[i])


myfun(OrgDict)

# Way 2

print({k:v for k, v in OrgDict.items() if v[0] >= 6 and v[1] >= 70 })
