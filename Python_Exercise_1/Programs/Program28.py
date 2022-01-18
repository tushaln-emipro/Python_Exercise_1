"""
    Program 28
    d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0} Sort this dictionary ascending and descending.
"""

# Way 1

d = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0}
lt1 = list(d.items())
lt1.sort()
print(lt1)

lt1.sort(reverse=True)
print(lt1)

# Way 2

x = {7: 2, 9: 4, 4: 3, 2: 1, 0: 0}
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1],reverse=True)})